from flask import Flask
from flask import json
from flask import jsonify
from flask import request
import os
import random
import hipchat_client

INSULTS = [
    "Is your ass jealous of the amount of shit that just came out of your mouth?",
    "I bet your brain feels as good as new, seeing that you never use it.",
    "I'd like to see things from your point of view but I can't seem to get my head that far up my ass.",
    "I could eat a bowl of alphabet soup and shit out a smarter statement than that.",
    "If I wanted to kill myself I'd climb your ego and jump to your IQ.",
    "If you're gonna be a smartass, first you have to be smart. Otherwise you're just an ass.",
    "It's better to let someone think you are an Idiot than to open your mouth and prove it.",
    "I have neither the time nor the crayons to explain this to you.",
    "Why don't you slip into something more comfortable -- like a coma.",
    "I may love to shop but I'm not buying your bullshit.",
    "Well I could agree with you, but then we'd both be wrong.",
    "You're the reason the gene pool needs a lifeguard.",
    "You have two brains cells, one is lost and the other is out looking for it.",
    "If I gave you a penny for your thoughts, I'd get change.",
    "You're as bright as a black hole, and twice as dense.",
    "If you spoke your mind, you'd be speechless.",
    "Shock me, say something intelligent.",
    "So you've changed your mind, does this one work any better?",
    "If your brain was made of chocolate, it wouldn't fill an M&M.",
    "I can explain it to you, but I can't understand it for you.",
    "You are proof that evolution CAN go in reverse.",
    "You do realize makeup isn't going to fix your stupidity?",
    "Some drink from the fountain of knowledge; you only gargled.",
    "It's kinda sad watching you attempt to fit your entire vocabulary into a sentence.",
    "You're a person of rare intelligence. It's rare when you show any.",
    "I thought you were attractive, but then you opened your mouth.",
    'You stare at frozen juice cans because they say, "concentrate".',
    "You're so stupid you tried to wake a sleeping bag.",
    "I don't know what makes you so stupid, but it really works!",
    "Aww, it's so cute when you try to talk about things you don't understand.",
    "Am I getting smart with you? How would you know?",
    "I'm not saying I hate you, but I would unplug your life support to charge my phone.",
    "You must have been born on a highway because that's where most accidents happen.",
    "You bring everyone a lot of joy, when you leave the room.",
    "You shouldn't play hide and seek, no one would look for you.",
    "I have neither the time nor the crayons to explain this to you."
]
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route("/", methods=['POST'])
def blame():
    request_data = to_json(request)
        
    requesters_room = _extract_requesters_room(request_data)
    arguments = _extract_arguments(request_data)
    requester = _extract_requester(request_data)
    
    guilty = None
    for argument in arguments:
        if '@' in argument:
            guilty = argument
    
    if not guilty:
        members = hipchat_client.get_room_members(requesters_room)
        
        guilty = '@' + random.choice(members) if members else 'all'
    
    if '--with-violence' in arguments:
        message = 'Hey ' + guilty + ' ! ' + random.choice(INSULTS) + ' (megusta)'
    elif '-h' in arguments or '--help' in arguments:
        message = "@" + requester + " I have neither the time nor the crayons to explain this to you."
    elif 'why' in arguments:
        message = "Because !!!!! https://labibliothequedaelinel.files.wordpress.com/2016/10/image.gif?w=656"
    else:
        message = 'I blame ' + guilty + ' ! >:-('
    
    return jsonify({
        "color": "red",
        "message": message,
        "notify": False,
        "message_format": "text"
    })
    
def to_json(request):
    return json.loads(request.data)

def _extract_arguments(request_data):
    command = request_data['item']['message']['message']

    return command.split(' ')[1:]


def _extract_requester(request_data):
    return request_data['item']['message']['from']['mention_name']


def _extract_requesters_room(request_data):
    return request_data['item']['room']['id']

if __name__ == "__main__":
    app.debug = True
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', '8080')))