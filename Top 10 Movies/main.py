from flask import Flask, render_template ,request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired
import requests
API_KEY = "89ec13b98e4c32b797332ab52d73b49e"
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# IMAGE_URL = 'https://image.tmdb.org/t/p/w500'

# USING THE API TO FETCH MOVIE DATA (YEAR-IMAGE-RATING)

url = "https://api.themoviedb.org/3/search/movie"








class Movieform(FlaskForm):
    rating = FloatField('rating')
    review = StringField('review')
    submit = SubmitField('Done')

class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    def __init__(self, title, year, description, rating, ranking, review, img_url):
        self.title = title
        self.year = year
        self.description = description
        self.rating = rating
        self.ranking = ranking
        self.review = review
        self.img_url = img_url

def initialize_data_base():
    with app.app_context():
        db.create_all()

        # Check if the movie with the title already exists
        movie = Movie.query.filter_by(title="Phone Booth 2").first()

        if not movie:
            new_movie = Movie(
                title="Phone Booth 2",
                year=2002,
                description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
                rating=7.3,
                ranking=10,
                review="My favourite character was the caller.",
                img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
            )
            db.session.add(new_movie)
        else:
            # Update the movie attributes
            movie.year = 2002
            movie.description = "Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax."
            movie.rating = 7.3
            movie.ranking = 10
            movie.review = "My favourite character was the caller."
            movie.img_url = "https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"

        db.session.commit()

@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/update", methods=["GET", "POST"])
def update():
        form = Movieform()

        movie_id = request.args.get('id')
        movie_to_update = Movie.query.get(movie_id)
        if form.validate_on_submit():
            movie_to_update.rating = form.rating.data
            movie_to_update.review = form.review.data
            db.session.commit()
            return redirect(url_for('home'))
        return render_template("edit.html",movie = movie_to_update, form=form)

@app.route('/delete', methods = ["GET","POST"])
def delete():
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods = ["GET","POST"])
def add():

    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(url, params={"api_key":API_KEY, "query":movie_title})
        data = response.json()['results']
        return render_template('select.html', options=data)
    return render_template('add.html', form = form)


@app.route('/find')
def find_movie():
    movie_api_id = request.args.get('id')
    if movie_api_id:
        URL = f"https://api.themoviedb.org/3/movie/{movie_api_id}"
        IMG_URL = "https://image.tmdb.org/t/p/w500"
        response = requests.get(URL, params={"api_key":API_KEY})
        data = response.json()
        new_movie = Movie(
            title =  data['title'],
            year = data['release_date'].split("-")[0],
            img_url = f"{IMG_URL}{data['poster_path']}",
            description=data["overview"],
            ranking = 9,
            rating=9.2,
            review="it was so good"

        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))

@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


if __name__ == '__main__':
    # Initialize the database first before running the app
    initialize_data_base()
    app.run(debug=True)
