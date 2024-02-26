import json
import unittest
from validators import validate_input
from authentication.register import register

event = {
    "body": {
        "username": "devsid2023",
        "password": "abcdeA@123",
        "name": "Siddhant Dembi",
        "mobileNumber": "8600363676",
        "whatappNumber": "8600363676",
        "address": {
            "houseUnitNumber": "A1-602",
            "streetName": "DSK-vishwa-road",
            "area": "DSK-vishwa-road",
            "landmark": "DSK-vishwa-road",
            "cityOrVillage": "Pune",
            "state": "Maharashtra",
            "country": "India",
            "latitude": 18.4432,
            "longitude": 73.7987,
        },
    }
}


class TestValidation(unittest.TestCase):
    def test_username(self):
        self.assertTrue(validate_input("username", event["body"]["username"]))

    def test_password(self):
        self.assertTrue(validate_input("password", event["body"]["password"]))

    def test_name(self):
        self.assertTrue(validate_input("full_name", event["body"]["name"]))

    def test_mobile_number(self):
        self.assertTrue(validate_input("mobile_number", event["body"]["mobileNumber"]))

    def test_whatsapp_number(self):
        self.assertTrue(
            validate_input("whatsapp_number", event["body"]["whatappNumber"])
        )

    def test_address(self):
        self.assertTrue(validate_input("address", event["body"]["address"]))


class TestRegisteration(unittest.TestCase):
    def test_register(self):
        self.assertTrue(register(event, None))



#input example
# {
#     "username": "rajesh123",
#     "password": "abcdeA@123",
#     "name": "Siddhant Dembi",
#     "mobileNumber": "8600363676",
#     "whatsappNumber": "8600363676",
#     "address": {
#         "houseUnitNumber": "A1-602",
#         "streetName": "DSK-vishwa-road",
#         "area": "DSK-vishwa-road",
#         "landmark": "DSK-vishwa-road",
#         "cityOrVillage": "Pune",
#         "state": "Maharashtra",
#         "country": "India",
#         "latitude": 18.4432,
#         "longitude": 73.7987
#     }
# }