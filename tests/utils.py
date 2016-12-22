from flask import json
import assertpy
import application


class BotClient:
    def __init__(self):
        self.app = application.app.test_client()

    def send_message(self, message, from_requester="Me", from_room="666"):
        data = self.build_message(requester=from_requester, room=from_room, message=message)
        return self.app.post("/", data=str(data))

    def build_message(self, requester, room, message):
        return {
            'event': 'room_message',
            'item': {
                'message': {
                    'date': '2015-01-20T22:45:06.662545+00:00',
                    'from': {
                        'id': 1661743,
                        'mention_name': requester,
                        'name': 'Blinky the Three Eyed Fish'
                    },
                    'id': '00a3eb7f-fac5-496a-8d64-a9050c712ca1',
                    'mentions': [],
                    'message': message,
                    'type': 'message'
                },
                'room': {
                    'id': room,
                    'name': 'The Weather Channel'
                }
            },
            'webhook_id': 578829
        }


def assert_that(response, is_equal_to):
    actual = json.loads(response.data)
    expected = build_response(is_equal_to)
    assertpy.assert_that(actual).is_equal_to(expected)


def build_response(message):
    return {
        "color": "red",
        "message": message,
        "notify": False,
        "message_format": "text"
    }
