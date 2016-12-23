from application import app
from flask import json
from flask import request
from application import service


@app.route("/", methods=["POST"])
def blame():
    arguments = _get_arguments()
    guilty = _find_people_to_blame(arguments)
    message_format = _get_message_format(arguments)
    message = message_format % guilty
    return _build_response(message)


def _get_arguments():
    command = _get_command()
    arguments = command.split(" ")[1:]
    return arguments


def _get_command():
    return json.loads(request.data)['item']['message']['message']


def _get_message_format(arguments):
    if '--with-violence' in arguments:
        return "Hey %s! " + service.random_insult() + " (megusta)(thumbsup)"
    else:
        return "I blame %s! >:-("


def _find_people_to_blame(arguments):
    targeted_persons = _get_targeted_persons(arguments)
    if targeted_persons:
        return ' and '.join(targeted_persons)
    else:
        return '@' + service.random_person(from_room='toto')


def _get_targeted_persons(arguments):
    guilty_persons = set()
    for argument in arguments:
        if '@' in argument and len(argument) > 1:
            guilty_persons.add(argument)
    return guilty_persons


def _build_response(message):
    return json.jsonify({
        "color": "red",
        "message": message,
        "notify": False,
        "message_format": "text"
    })
