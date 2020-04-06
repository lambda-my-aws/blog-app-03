from datetime import datetime as dt

from flask import (
    Flask,
    jsonify,
    make_response,
)

App = Flask(__name__)
App.config.from_object("config")


@App.route("/", methods=["GET"])
def hello():
    """
    Simple Hello World function
    """
    answer = {'name': 'app03'}
    return make_response(jsonify(answer), 200)


@App.route('/time', methods=['GET'])
def get_time():
    return make_response(jsonify({'time': dt.utcnow().isoformat()}))
