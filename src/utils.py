import json

import joblib

__data = None
__wines = None
__cosine = None
__model = None


def load_data():
    global __wines

    with open("../models/columns.json", "r") as f:
        __wines = json.load(f)["data_columns"]

    global __cosine
    global __data

    (__cosine, __data) = joblib.load(
        "../models/content_based_recommender_model.pkl",
    )

    return (
        __wines,
        __data,
        __cosine,
    )


def get_wine_names():
    load_data()
    return __wines


def get_recommendations(wine):
    load_data()
    recommendation = {}

    idx = __data.index[__data["WineName"] == wine].tolist()[0]
    sim_scores = list(enumerate(__cosine[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    wine_indices = [i[0] for i in sim_scores]

    recommendation = {
        "WineName": __data["WineName"].iloc[wine_indices].tolist(),
        "Score": [i[1] for i in sim_scores],
    }

    return recommendation


if __name__ == "__main__":
    load_data()
