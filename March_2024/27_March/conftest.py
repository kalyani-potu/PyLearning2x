import pytest
import  requests

@pytest.fixture
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type" : "application/json"}
    json_payload = {
        "username" : "admin",
        "password" : "password123"
        }
    response = requests.post(url=url,headers=headers,json=json_payload)
    data = response.json()
    token = data["token"]
    print(token)
    return token

@pytest.fixture
def create_booking():
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
    "firstname" : "Jimem",
    "lastname" : "Brownie",
    "totalprice" : 1234,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2022-01-01",
        "checkout" : "2024-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    data1 = response.json()
    print(data1)
    booking_id = data1["bookingid"]
    assert response.status_code == 200
    return booking_id
