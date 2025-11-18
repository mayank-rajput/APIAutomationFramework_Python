# API testcase
# URL - API Constants.py
# headers - utils.py
# payload - payload_manager.py
# HTTP post - api_request_wrapper.py
# verification - common_verification.py


import allure
import pytest
from src.helpers.api_requests_wrapper import post_request
from src.helpers.payload_manager import payload_create_booking
from src.constants.api_constants import APIContants
from src.helpers.common_verification import *
from src.utils.utils import  utils
import logging

class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID Shouldn't null")
    @allure.description("Verify that Create Booking Status and Booking ID Shouldn't null")
    def test_create_booking_positive(self):
        logger = logging.getLogger(__name__)
        logger.info("Starting the TesCase - TC1 - Positive")

        response = post_request(
            url=APIContants().url_create_booking(),
            auth= None,
            headers=utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=200)
        verify_json_key_for_not_null(response.json()["bookingid"])
        logger.info("End of the Testcase TC1  - Positive")

    @pytest.mark.negative
    @allure.title("Verify that Create Booking Status and Booking ID Shouldn't null")
    @allure.description("Verify that Create Booking Status and Booking ID  Shouldn't null")
    def test_create_booking_negative(self):
        logger = logging.getLogger(__name__)
        logger.info("Starting the TesCase - TC2 - negative")

        response = post_request(
            url=().url_create_booking(),
            auth=None,
            headers=utils().common_headers_json(),
            payload={},
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=500)
