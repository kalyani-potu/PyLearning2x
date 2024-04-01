import pytest
import allure
import requests
from conftest import create_token, create_booking


# from conftest file we are importing fixture methods create_booking and create_token
@allure.title("TC#01 - Create Booking")
def test_create_booking():
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Drithi",
        "lastname": "Pen",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
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
    assert first_name == "Drithi", "Failed message - Incorrect firstname"  # when the firstname is incorrect, failed message is printed
    assert last_name == "Pen"
    assert total_price == 100
    assert deposit_paid == True
    assert additional_needs == "Breakfast"
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"


@allure.title("TC#02 - Get Booking")
def test_get_booking(create_booking):
    base_url = "https://restful-booker.herokuapp.com/booking/"
    id = create_booking
    url = base_url + str(id)
    headers = {"Accept": "application/json"}
    response = requests.get(url=url, headers=headers)
    response_json = response.json()
    assert response.status_code == 200
    print(response_json)
    first_name = response_json["firstname"]
    last_name = response_json["lastname"]
    total_price = response_json["totalprice"]
    deposit_paid = response_json["depositpaid"]
    additional_needs = response_json["additionalneeds"]
    checkin = response_json["bookingdates"]["checkin"]
    checkout = response_json["bookingdates"]["checkout"]
    assert first_name == "Jimem"
    assert last_name == "Brownie"
    assert total_price == 1234
    assert deposit_paid == True
    assert additional_needs == "Breakfast"
    assert checkin == "2022-01-01"
    assert checkout == "2024-01-01"


@allure.title("TC#03 - Put Request")
def test_put_request(create_booking, create_token):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    param = create_booking
    put_url = base_url + base_path + str(param)
    cookie = "token=" + create_token
    headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               "Cookie": cookie}
    json_payload = {
        "firstname": "Kalyani",
        "lastname": "Potu",
        "totalprice": 1234,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-11-11",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Lunch"
    }
    response = requests.put(url=put_url, headers=headers, json=json_payload)
    data2 = response.json()
    print(data2)
    first_name = data2["firstname"]
    last_name = data2["lastname"]
    total_price = data2["totalprice"]
    deposit_paid = data2["depositpaid"]
    check_in = data2["bookingdates"]["checkin"]
    check_out = data2["bookingdates"]["checkout"]
    additional_needs = data2["additionalneeds"]
    assert first_name == "Kalyani", "Failed message - Incorrect Firstname"
    assert last_name == "Potu"
    assert total_price == 1234
    assert deposit_paid == True
    assert check_in == "2024-11-11"
    assert check_out == "2019-01-01"
    assert additional_needs == "Lunch"
    assert response.status_code == 200

@allure.title("TC#04 - Patch Request")
def test_patch_request(create_booking, create_token):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    param = create_booking
    put_url = base_url + base_path + str(param)
    cookie = "token=" + create_token
    headers = {"Content-Type": "application/json",
               "Accept" : "application/json",
               "Cookie" : cookie}
    json_payload = {
    "firstname" : "Krithi",
    "lastname" : "Pen",
     }
    response = requests.patch(url=put_url, headers=headers, json=json_payload)
    data2 = response.json()
    print(data2)
    first_name = data2["firstname"]
    last_name = data2["lastname"]
    total_price = data2["totalprice"]
    deposit_paid = data2["depositpaid"]
    check_in = data2["bookingdates"]["checkin"]
    check_out = data2["bookingdates"]["checkout"]
    additional_needs = data2["additionalneeds"]
    assert first_name == "Krithi", "Failed message - Incorrect Firstname"
    assert last_name == "Pen"
    assert total_price == 1234
    assert deposit_paid == True
    assert check_in == "2022-01-01"
    assert check_out == "2024-01-01"
    assert additional_needs == "Breakfast"
    assert response.status_code == 200

@allure.title("TC#05 - Delete Booking")
def test_delete_booking(create_booking, create_token):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    booking_id = create_booking
    delete_url = base_url + base_path + str(booking_id)
    cookie = "token=" + create_token
    headers = {"Content-Type": "application/json",
               "Cookie" : cookie}
    response = requests.delete(url=delete_url, headers=headers)
    assert response.status_code == 201