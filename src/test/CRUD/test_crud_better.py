# Conftest
# Create Booking
# Create booking ID
# Update Booking(PUT) - Booking ID, Token
# Delete Booking
from symtable import Class

import allure
import pytest

from src.constants.api_constants import APIContants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import utils


class TestCRUDBooking(object):
    @pytest.mark.put
    @allure.title("Test CRUD operation Update(PUT).")
    @allure.description(
        "Verify that Full Update with the booking ID and Token is working.")
    def test_update_booking_id_token(self, create_token, get_booking_id):
        put_url = APIContants.url_patch_put_delete(booking_id=get_booking_id)
        print(put_url)
        response = put_requests(
            url=put_url,
            headers=utils().common_header_put_delete_patch_cookie(token=create_token),
            payload=payload_update_booking(),
            auth=None,
            in_json=False
        )


        # Verification here & more
        verify_response_key(response.json()["firstname"], "Amit")
        verify_response_key(response.json()["lastname"], "Brown")
        verify_http_status_code(response_data=response, expected_data=200)









