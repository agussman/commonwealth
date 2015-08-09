from yelpclient import YelpClient
import json
import httplib
import urllib
from geopy.distance import great_circle

keys = {
    'consumer_key': 'jb_FCNZnRQUl-ZBYIC7AMQ',
    'consumer_secret': '9w2belyaG3TQljVJ3AFqAct2zsQ',
    'token': 'nwmC3CUV1Gq8W8idtT2SIhVsPEqYVVhj',
    'token_secret': 'PHG1XzFh0r5ZVQpDt74VN-TN5bs',
}

headers = {
    # Request headers
    'api_key': '742e08c7b5324dfcb1a51cfbba70c8f8',
}

client = YelpClient(keys)


def main():
    lat = 38.9048907
    lon = -77.0339064

    json_file = provide_stores_json(lat, lon)

    # print "Name:", json_file["businesses"][0]["name"]
    # print "ID:", json_file["businesses"][0]["id"]
    # print "Image URL:", json_file["businesses"][0]["image_url"]
    # print "Phone Number:", json_file["businesses"][0]["phone"]
    # print json_file["businesses"][0]["location"]["display_address"][0]
    # print json_file["businesses"][0]["location"]["display_address"][1]
    # print json_file["businesses"][0]["location"]["display_address"][2]

    lat = json_file["region"]["center"]["latitude"]
    lon = json_file["region"]["center"]["longitude"]

    f = open("food_search.json", "w")
    json.dump(json_file, f)
    f.close()

    distances = distance_to_buses_json(lat, lon)

    for i in distances["Stops"]:
        print (distance_calculator_two_coord(lat, lon, i["Lat"], i["Lon"]))

    j = open("bus_information.json", "w")

    json.dump(distances, j)

    j.close()


# Input: Lat, Long of the person using the app
# Output: Json file of stores
def provide_stores_json(lat, lon):
    return client.search_by_geo_coord(latlong=(lat, lon), term="food", limit=1, radius=2000)


# Provides the distance from the small business to public transportation
# Input: Requires the lat and long of the business
# Output: Returns a float for the shortest distance to public tranportation
def distance_to_buses_json(lat, lon):
    params = urllib.urlencode({
        # Request parameters
        'Lat': lat,
        'Lon': lon,
        # Hardcoded, can be changed
        'Radius': '500',
    })

    conn = httplib.HTTPSConnection('api.wmata.com')
    endpoint = "/Bus.svc/json/jStops?&%s" % params
    conn.request("GET", endpoint, "{body}", headers)
    response = conn.getresponse()

    data = json.loads(response.read())
    conn.close()

    return data


def distance_to_trains_json(lat, lon):
    params = urllib.urlencode({
        # Request parameters
        'Lat': lat,
        'Lon': lon,
        # Hardcoded, can be changed
        'Radius': '1000',
    })

    conn = httplib.HTTPSConnection('api.wmata.com')
    endpoint = "/Rail.svc/json/jStationEntrances?&%s" % params
    conn.request("GET", endpoint, "{body}", headers)
    response = conn.getresponse()

    data = json.loads(response.read())
    conn.close()

    return data


def distance_calculator_two_coord(business_lat, business_lon, bus_stop_lat, bus_stop_lon):
    first = (business_lat, business_lon)

    second = (bus_stop_lat, bus_stop_lon)

    return great_circle(first, second).miles


if __name__ == "__main__":
    main()
