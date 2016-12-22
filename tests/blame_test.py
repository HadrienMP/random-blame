import unittest

import application
from tests.utils import BotClient
from tests.utils import assert_that
# from unittest.mock import patch
from unittest import mock

application.random_person = mock.MagicMock(return_value="someone")


class MyTest(unittest.TestCase):
    def setUp(self):
        self.bot_client = BotClient()

    # @patch("application.random_person")
    def test_blame_someone_from_the_room(self, random_person_mock=None):
        # random_person_mock.return_value = "someone"

        response = self.bot_client.send_message("/blame")

        # random_person_mock.assert_called_with("toto")
        assert_that(response, is_equal_to="I blame @someone! >:-(")
