from src.helpers.api_requests_wrapper import post_request
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.constants.api_constants import APIContants
from src.helpers.common_verification import *
from src.utils.utils import  utils
import logging

import allure
import pytest

@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url=APIContants().url_creat_token(),
        auth= None,
        headers=utils().common_headers_json(),
        payload=payload_create_token(),
        in_json=False
    )
    verify_http_status_code(response_data=response, expected_data=200)
    verify_json_key_for_not_null_token(response.json()["token"])
    return response.json()["token"]

@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(
    url=APIContants().url_create_booking(),
    auth= None,
    headers=utils().common_headers_json(),
    payload=payload_create_booking(),
    in_json=False
)
    booking_id = response.json()["bookingid"]
    verify_http_status_code(response_data=response, expected_data=200)
    verify_json_key_for_not_null(booking_id)
    return booking_id