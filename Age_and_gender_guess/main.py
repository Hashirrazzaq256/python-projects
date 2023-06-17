from flask import Flask, render_template
import requests

app = Flask(__name__)



@app.route('/guess/<names>')
def home(names):
    response_age = requests.get(f"https://api.agify.io?name={names}")
    response = requests.get(f"https://api.genderize.io?name={names}")
    data_gender = response.json()
    gender = data_gender["gender"]
    data = response_age.json()
    age = data["age"]
    return f'<h1>hey {names} </h1><br>' \
           f'<h2>I guess you are {age} years old </h2><br>'\
          f' <h3> And you are a {gender}</h3>'



if __name__ == "__main__":
    app.run(debug=True)
