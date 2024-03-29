import pytest
import allure
import requests

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

@allure.title("TC#01 - Create Booking")
def test_create_booking():
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
    "firstname" : "Drithi",
    "lastname" : "Pen",
    "totalprice" : 100,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    response = requests.post(url = url, headers= headers, json=json_payload)
    assert response.status_code == 200
    response_json = response.json()
    booking_id = response_json["bookingid"]
    assert booking_id is not None
    assert booking_id > 0
    assert type(booking_id) == int
    first_name = response_json["booking"]["firstname"]
    last_name = response_json["booking"]["lastname"]
    total_price = response_json["booking"]["totalprice"]
    deposit_paid = response_json["booking"]["depositpaid"]
    additional_needs = response_json["booking"]["additionalneeds"]
    checkin = response_json["booking"]["bookingdates"]["checkin"]
    checkout = response_json["booking"]["bookingdates"]["checkout"]
    assert first_name == "Drithi"
    assert last_name == "Pen"
    assert total_price == 100
    assert deposit_paid == True
    assert additional_needs == "Breakfast"
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"


