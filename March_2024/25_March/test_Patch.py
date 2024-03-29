import pytest
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
def create_booking():
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
    "firstname" : "Jimem",
    "lastname" : "Brownie",
    "totalprice" : 1001,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2022-01-01",
        "checkout" : "2024-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    data1 = response.json()
    booking_id = data1["bookingid"]
    assert response.status_code == 200
    return booking_id

def test_patch_request():
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
    assert first_name == "Kalyani", "Failed message - Incorrect Firstname"
    assert last_name == "Potu"
    assert total_price == 1001
    assert deposit_paid == True
    assert check_in == "2022-01-01"
    assert check_out == "2024-01-01"
    assert additional_needs == "Breakfast"
    assert response.status_code == 200