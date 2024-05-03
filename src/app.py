from flask import Flask, jsonify, request

import utils

app = Flask(__name__)


@app.route("/get_wine_names", methods=["GET"])
def get_wine_names():
    response = jsonify(
        {
            "wines": utils.get_wine_names(),
        }
    )
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/recommend_wines", methods=["POST"])
def recommend_wines():
    wine = request.form["wine"]
    response = jsonify(
        {
            "recommendations": utils.get_recommendations(
                wine,
            ),
        }
    )
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    print("Starting server...")
    app.run(port=5050)
