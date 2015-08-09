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

client = YelpClient(keys)

headers = {
    'api_key': '742e08c7b5324dfcb1a51cfbba70c8f8',
}

def main():
    # local lat & lon
    local_lon = -77.0339064
    local_lat = 38.9048907

    json_file = client.search_by_geo_coord(latlong=(local_lat, local_lon), term="food", limit=20, radius=2000)

    tempList1 = []

    for i in json_file["businesses"]:
        tempList2 = [i["id"], i["name"], i["image_url"], i["location"]["display_address"][0],
                     json_file["region"]["center"]["latitude"], json_file["region"]["center"]["longitude"]]
        tempList1.append(tempList2)

    f = open("sample_data.json", "w")
    json.dump(tempList1, f)


# Provides the distance from the small business to public transportation
# Input: Requires the lat and long of the business
# Output: Returns a float for the shortest distance to public transportation
def distance_to_buses_json(lat, lon):
    params = urllib.urlencode({
        # Request parameters
        'Lat': lat,
        'Lon': lon,
        # Hardcoded, can be changed
        'Radius': '250',
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
        'Radius': '500',
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


def smallest_distance(business_lat, business_lon, bus_data, train_data):
    temp_array = []

    for i in bus_data["Stops"]:
        temp_array.append(distance_calculator_two_coord(business_lat, business_lon, i["Lat"], i["Lon"]))

    for i in train_data["Entrances"]:
        temp_array.append(distance_calculator_two_coord(business_lat, business_lon, i["Lat"], i["Lon"]))

    return min(temp_array)


if __name__ == "__main__":
    main()
