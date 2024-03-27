import pytest
import allure
import requests

@allure.testcase("TC#01")
@allure.description("Restful booker - Get BookingId")

@pytest.mark.apit
def test_request():
    response = requests.get("https://restful-booker.herokuapp.com/booking/1220")
    response_status = response.status_code
    assert response_status == 200
    print(response.json())
    print(response.text)
    #print(response.content)
    #print(response.headers)
    print(response.url)
    print(response.cookies)
