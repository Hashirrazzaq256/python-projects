from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Define the endpoint and your API key
endpoint = 'https://api.openai.com/v1/chat/completions'
api_key = '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'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get user input from the HTML form
        user_input = request.form['user_input']

        # Define the headers and payload for the API request
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

        payload = {
            'model': 'gpt-3.5-turbo',
            'messages': [
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': user_input}
            ]
        }

        # Send the API request
        response = requests.post(endpoint, headers=headers, json=payload)

        # Process the response
        if response.status_code == 200:
            data = response.json()
            answer = data['choices'][0]['message']['content']
            return render_template('index.html', answer=answer)

        return f"Request failed with status code: {response.status_code}"

    return render_template('index.html', answer='')


if __name__ == '__main__':
    app.run(debug=True)
