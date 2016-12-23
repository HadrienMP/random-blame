from application import app
from flask import json
from application import service


@app.route("/", methods=["POST"])
def blame():
    message = "I blame @" + service.random_person(from_room='toto') + "! >:-("
    return json.jsonify({
            "color": "red",
            "message": message,
            "notify": False,
            "message_format": "text"
        })
