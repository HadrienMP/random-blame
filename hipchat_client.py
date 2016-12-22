import requests


def get_room_members(room):
    r = _authenticated_get('https://api.hipchat.com/v2/room/{room}/participant'.format(room=room))

    if r.status_code is 200:
        return [member['mention_name'] for member in r.json()['items']]
    else:
        print(r.url)
        print(r.status_code)
        print(r.text)
        return []


def _authenticated_get(url):
    return requests.get(url + '?auth_token=MX2thj0LKMXwgSE0FxjdM4ZrEAypHSX70JQiAHff')
