import unittest
from unittest.mock import MagicMock, patch
from events.get_event import get

class TestGetFunction(unittest.TestCase):
    @patch('events.get_event.boto3.resource')
    def test_successful_response(self, boto3_resource_mock):
        # Mock DynamoDB Table
        table_mock = MagicMock()
        boto3_resource_mock.return_value.Table.return_value = table_mock

        # Mock DynamoDB scan method to return test data
        table_mock.scan.return_value = {'Items': [
            {
                "eventId": "2024-0001",
                "attendees": ["09828416-9fbd-11ee-af45-c9586254f505"],
                "participant_amount": 100,
                "organiser": "09828416-9fbd-11ee-af45-c9586254f505",
                "dateandtime": "2023-12-15T08:03:47+0000",
                "creater": "09828416-9fbd-11ee-af45-c9586254f505",
                "eventType": "Vastushant,Satyanarayan",
                "address": {
                    "houseUnitNumber": "A1-602",
                    "area": "DSK-vishwa-road",
                    "country": "India",
                    "streetName": "DSK-vishwa-road",
                    "cityOrVillage": "Pune",
                    "latitude": 18.4432,
                    "state": "Maharashtra",
                    "landmark": "DSK-vishwa-road",
                    "longitude": 73.7987,
                },
                "id": "22225a3d-9fbd-11ee-b3f3-412e96ffee3d",
                "requiredParticipants": 0,
            }
        ]}

        # Call the 'get' function with mocked dependencies
        result = get({}, {})

        # Assert the expected result for the provided test case
        expected_result = {
            'statusCode': 200,
            'body': '[{"eventId": "2024-0001", "attendees": ["09828416-9fbd-11ee-af45-c9586254f505"], "participant_amount": 100, "organiser": "09828416-9fbd-11ee-af45-c9586254f505", "dateandtime": "2023-12-15T08:03:47+0000", "creater": "09828416-9fbd-11ee-af45-c9586254f505", "eventType": "Vastushant,Satyanarayan", "address": {"houseUnitNumber": "A1-602", "area": "DSK-vishwa-road", "country": "India", "streetName": "DSK-vishwa-road", "cityOrVillage": "Pune", "latitude": 18.4432, "state": "Maharashtra", "landmark": "DSK-vishwa-road", "longitude": 73.7987}, "id": "22225a3d-9fbd-11ee-b3f3-412e96ffee3d", "requiredParticipants": 0}]'
        }
        self.assertEqual(result, expected_result)

        # Assert that the DynamoDB resource and table were called as expected
        boto3_resource_mock.assert_called_once_with('dynamodb')
        boto3_resource_mock.return_value.Table.assert_called_once_with('godswork-api-dev-events')
        table_mock.scan.assert_called_once()

if __name__ == '__main__':
    unittest.main()

# python -m unittest ./testing/get_event_test.py