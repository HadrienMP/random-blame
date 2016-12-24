# -*-coding: UTF-8 -*-
from application.hipchat_client import HipChatClient

hipchat_client = HipChatClient('MX2thj0LKMXwgSE0FxjdM4ZrEAypHSX70JQiAHff')


def test_should_return_room_members_in_a_public_room():
    members = hipchat_client.get_room_members("3377850")

    assert len(members) > 1  # A public room only has one "member" but maybe more participants


def test_should_return_room_members_in_a_private_room():
    members = hipchat_client.get_room_members("2247343")

    assert len(members) > 1  # A public room only has one "member" but maybe more participants


def test_should_return_empty_list_for_an_invalid_room_number():
    members = hipchat_client.get_room_members("-1")
    assert members == []
