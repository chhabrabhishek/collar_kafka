from flask import Flask
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/serve")
@cross_origin()
def serve():
    with open('coordinates.json', 'r+') as coordinates:
        coordinates = json.load(coordinates)
        return coordinates
