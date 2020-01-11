import geopy
from geopy.exc import GeocoderTimedOut
import time
geolocator = geopy.Nominatim()
address = "Palla, Delhi"

# to avoid timeout, do multiple requests
def do_geocode(address):
    try:
        return geolocator.geocode(address)
    except GeocoderTimedOut:
        time.sleep(0.1)
        return do_geocode(address)
location = do_geocode(address)
print("location: ", location)
print("point: ", location.point)
print("latitude: ", location.latitude)
print("longitude: ", location.longitude)