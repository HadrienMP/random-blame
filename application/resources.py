from application import app
from flask import json
from flask import request
from application import service


@app.route("/", methods=["POST"])
def blame():
    
    command = json.loads(request.data)['item']['message']['message']
    arguments = command.split(" ")[1:]
    
    guilty_persons = set()
    for argument in arguments:
        if '@' in argument and len(argument) > 1:
            guilty_persons.add(argument)
    
    guilty = ' and '.join(guilty_persons) if guilty_persons else '@' + service.random_person(from_room='toto')
    
    message = "I blame %s! >:-(" % guilty
    
    return json.jsonify({
            "color": "red",
            "message": message,
            "notify": False,
            "message_format": "text"
        })
