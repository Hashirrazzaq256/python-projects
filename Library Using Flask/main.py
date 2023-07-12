from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", books=all_books)



@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        print(request.form)  # Print the form data for debugging
        if 'title' in request.form:
            new_book = {
                "title": request.form["title"],
                "author": request.form["author"],
                "rating": request.form["rating"],
            }
            all_books.append(new_book)
            return redirect(url_for('home'))
        else:
            # Handle case when 'title' key is missing
            return "Error: Book title is missing."
    return render_template("add.html")



if __name__ == "__main__":
    app.run(debug=True)

