import unittest
from events.create_event import create


class TestCreateEvent(unittest.TestCase):
    def test_no_body():
        event = {}
        context = {}
        response = create(event, context)
        unittest.assertEqual(response["statusCode"], 400)

    def test_no_token():
        event = {"body": {}}
        context = {}
        response = create(event, context)
        unittest.assertEqual(response["statusCode"], 400)
