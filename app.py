"""Simple Flask API taht can be used to get the root of a real number.

To start the api, cd in the directory of containing this file and run in a terminal :

    `flask run`

To query the API, open another terminal anywhere and run

    `curl "localhost:5000/racine?x=X"

Where you replace X by the real number you need the square root of.
"""

from flask import Flask, jsonify, request

from racine import racine
app = Flask(__name__)


@app.route('/')
def hello_world():
    response = jsonify('Home page')
    response.status_code = 200
    return response


@app.route("/racine", methods=["GET"])
def get_racine():
    if request.method != 'GET':
        response = jsonify(f"Can only get racine, not {request.method}")
        response.status_code = 200
        return response
    args = request.args
    try:
        x = args.get("x", default=None, type=float)
        if x is None:
            raise ValueError("Argument x must be specified")
        y = racine(x)
        response = jsonify(y)
        response.status_code = 200
    except (ValueError, TypeError) as e:
        response = jsonify(str(e))
        response.status_code = 400
    return response


if __name__ == "__main__":
    app.run(debug=True)
