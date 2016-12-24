from application import app
import requests


class HipChatClient:
    def __init__(self, token):
        self.token = token
        self.room_member_url_format = 'https://api.hipchat.com/v2/room/{room}/participant'

    
    def get_room_members(self, room):
        response = self._authenticated_get(self.room_member_url_format.format(room=room))
    
        if response.status_code is 200:
            return [member['mention_name'] for member in response.json()['items']]
        else:
            print(response.url)
            print(response.status_code)
            print(response.text)
            return []
    
    
    def _authenticated_get(self, url):
        return requests.get(url + '?auth_token=' + self.token)
