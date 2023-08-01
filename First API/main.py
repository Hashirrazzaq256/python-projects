from flask import Flask, jsonify, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import random as rand

app = Flask(__name__)

#Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=True)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = rand.choice(cafes)
    # Simply convert the random_cafe data record to a dictionary of key-value pairs.
    return jsonify(cafe=random_cafe.to_dict())

## HTTP GET - Read Record

@app.route('/all')
def all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes = [cafe.to_dict() for cafe in cafes])

@app.route('/find')
def find():
    query_location = request.args.get('loc')
    query_location=query_location.capitalize()
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})

## HTTP POST - Create Record
def str_to_bool(arg_from_url):
    if arg_from_url in ['True', 'true', 'T', 't', 'Yes', 'yes', 'y', '1']:
        return True
    else:
        return False


@app.route("/add", methods=["POST"])
def add_a_cafe():
    if request.method == "POST":
        data = request.json  # Get the JSON data from the request
        print("Data received:", data)

        # Extract the individual values from the data
        name = data.get("name")
        map_url = data.get("map_url")
        img_url = data.get("img_url")
        location = data.get("loc")
        seats = data.get("seats")
        has_toilet = data.get("toilet")
        has_wifi = data.get("wifi")
        has_sockets = data.get("sockets")
        can_take_calls = data.get("calls")
        coffee_price = data.get("coffee_price")

        # Check if 'name' is present in the JSON data
        if not name:
            return jsonify(error={"message": "Name is required"}), 400

        # Create a new Cafe object with the extracted values
        new_cafe = Cafe(name=name,
                        map_url=map_url,
                        img_url=img_url,
                        location=location,
                        seats=seats,
                        has_toilet=has_toilet,
                        has_wifi=has_wifi,
                        has_sockets=has_sockets,
                        can_take_calls=can_take_calls,
                        coffee_price=coffee_price)

        # Add the new cafe to the database
        db.session.add(new_cafe)
        db.session.commit()

        return jsonify(response={"success": "Successfully added the new cafe"})

    # Return an error response if the request method is not POST
    return jsonify(error={"message": "Method not allowed"}), 405

## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<cafe_id>', methods=["PATCH", "GET"])
def update(cafe_id):
    new_price = request.args.get("new_price")
    print(f"Received request with cafe_id: {cafe_id}, new_price: {new_price}")

    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."})

## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,threaded=False)
