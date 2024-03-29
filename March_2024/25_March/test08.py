import requests
import pytest

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

def create_booking():
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    data1 = response.json()
    booking_id = data1["bookingid"]
    assert response.status_code == 200
    return booking_id

def test_put_request():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    param = create_booking()
    put_url = base_url + base_path + str(param)
    cookie = "token=" + create_token()
    headers = {"Content-Type": "application/json",
               "Accept" : "application/json",
               "Cookie" : cookie}
    json_payload = {
    "firstname" : "Kalyani",
    "lastname" : "Potu",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2024-11-11",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Lunch"
    }
    response = requests.put(url=put_url, headers=headers, json=json_payload)
    data2 = response.json()
    first_name = data2["firstname"]
    last_name = data2["lastname"]
    total_price = data2["totalprice"]
    check_in = data2["bookingdates"]["checkin"]
    assert first_name == "Kalyani", "Failed message - Incorrect Firstname"
    assert last_name == "Potu"
    assert total_price == 111
    assert check_in == "2024-11-11"
    assert response.status_code == 200

def test_delete_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    booking_id = create_booking()
    delete_url = base_url + base_path + str(booking_id)
    cookie = "token=" + create_token()
    headers = {"Content-Type": "application/json",
               "Cookie" : cookie}
    response = requests.delete(url=delete_url, headers=headers)
    assert response.status_code == 201
