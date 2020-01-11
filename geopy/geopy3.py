import geopy, time
from geopy.exc import GeocoderTimedOut
from geopy import distance

geolocator = geopy.Nominatim()
address1 = "Palla, Delhi"
address2 = "Faridabad"

# to avoid timeout, do multiple requests
def do_geocode(address):
    try:
        return geolocator.geocode(address)
    except GeocoderTimedOut:
        time.sleep(0.1)
        return do_geocode(address)
location1 = do_geocode(address1)
location2 = do_geocode(address2)
print("location1: ", location1)
print("location2: ", location2)
print("Distance between: ", distance.distance(location1.point, location2.point).kilometers, "km")