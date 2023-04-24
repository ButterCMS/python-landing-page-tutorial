from flask import Flask, render_template, jsonify
import requests
app = Flask(__name__, static_folder='static')


# set up ButterCMS API credentials
auth_token = 'b6ac3b117c77cfb2dbddd09a8529fc1375aaf865'
api_url = 'https://api.buttercms.com/v2/pages/*/index-page/?auth_token='

# define the API endpoint to fetch content from
endpoint = 'pages/*/index-page/'

# app route


@app.route('/', methods=['GET'])
def index():

    # Make a GET request to the API endpoint
    response = requests.get(api_url + auth_token)
    # Convert the response to JSON format
    data = response.json()['data']['fields']
    hero = data['hero_component']
    pricing = data['pricing']
    features = data['features']
    footer = data['footer_component']

    print('data is', footer)
    return render_template('index.html', hero=hero, pricing=pricing, features=features, footer=footer)


if __name__ == '__main__':
    app.run(debug=True)
