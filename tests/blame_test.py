import unittest
from tests.utils import BotClient
from tests.utils import assert_that, get_message
from unittest.mock import patch
from unittest import mock
import assertpy

class Blame(unittest.TestCase):
    def setUp(self):
        self.bot_client = BotClient()


    @patch("application.service.random_person")
    def test_should_blame_someone_from_the_room_by_default(self, random_person_mock=None):
        random_person_mock.return_value = "someone"

        response = self.bot_client.send_message("/blame")

        assert_that(response, is_equal_to="I blame @someone! >:-(")
    
    
    
    def test_should_blame_the_person_given_after_the_command(self):
        response = self.bot_client.send_message("/blame @you")
        
        assert_that(response, is_equal_to="I blame @you! >:-(")
          
      
    def test_should_blame_all_the_persons_given_after_the_command(self):
        response = self.bot_client.send_message("/blame @you @youtoo @youalso @andyou")
        
        assertpy.assert_that(get_message(response)).contains("@you", "@youtoo", "@youalso", "@andyou")
          
      
    def test_should_blame_all_the_persons_given_after_the_command_only_once(self):
        response = self.bot_client.send_message("/blame @andyou @andyou @andyou")
        
        assert_that(response, is_equal_to="I blame @andyou! >:-(")
          
      
    @patch("application.service.random_person")
    def test_should_blame_someone_from_the_room_when_only_an_at_is_present(self, random_person_mock):
        random_person_mock.return_value = "someone"
        
        response = self.bot_client.send_message("/blame @")
        
        assert_that(response, is_equal_to="I blame @someone! >:-(")
        
    
    