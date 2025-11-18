# APIConstants - class which contains all the endpoints.
# Keep all the URLs.

class APIContants(object):

    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_creat_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    # Update - Put, Patch , Delete - BookingID

    def url_patch_put_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking" + str(booking_id)
