import geopy
from geopy.exc import GeocoderTimedOut
import time
geolocator = geopy.Nominatim()
address = "New Delhi"

# to avoid timeout, do multiple requests
def do_geocode(address):
    try:
        return print(geolocator.geocode(address).point)
    except GeocoderTimedOut:
        time.sleep(0.1)
        return do_geocode(address)
do_geocode(address)