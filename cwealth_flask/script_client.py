import datetime
import json
import httplib
import urllib
from yelpclient import YelpClient
from geopy.distance import great_circle
<<<<<<< HEAD
from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError
=======
import sys
from pprint import pprint
import time

import requests
>>>>>>> fab8796978f738d31e0bf2f2d4c64d0043400629

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

conn = httplib.HTTPSConnection('api.wmata.com')




def main():
    # local lat & lon
    local_lon = -77.0339064
    local_lat = 38.9048907

    json_file = client.search_by_geo_coord(latlong=(local_lat, local_lon), term="food", limit=20, radius=2000)

    fout = open("yelp_results.json", "w")
    json.dump(json_file, fout)
    fout.close()


    f = open("sample_data.json", "w")

    for i in json_file["businesses"]:
        business_lat = json_file["region"]["center"]["latitude"]
        business_lon = json_file["region"]["center"]["longitude"]

        new_json = {

            "yelp_id": i["id"],
            "business_name": i["name"],
            "lat": business_lat,
            "lon": business_lon,
            "address": i["location"]["display_address"][0],
            "image_url": i["image_url"],
            "wage_score": 14.84
            # ,"transportation_score": compute_transportation_score(business_lat, business_lon)
        }

<<<<<<< HEAD
        f = open("sample_data.json", "w")
        json.dump(new_json, f)
        f.close()




# def compute_transportation_score(lat, lon):
#     train_data = distance_to_trains_json(lat, lon)
#     bus_date = distance_to_buses_json(lat, lon)
#     return smallest_distance(lat, lon, bus_date, train_data)
=======
        #transportation_score = compute_transportation_score(bus_lat, bus_lon)


        #pprint(new_json)
        time.sleep(1)
        #sys.exit(22)

#    f = open("sample_data.json", "w")
        #json.dump(new_json, f)

        # push to ENDPOINT
        endpoint = "http://52.2.225.70:8000/businesses/"
        r = requests.post(endpoint, data=new_json)
        print r
        print r.text
        #sys.exit(22)

    f.close()


def compute_transportation_score(lat, lon):
    print "Lat: %s, Lon: %s" % (lat, lon)
    train_dist = distance_to_trains_json(lat, lon)
    #print train_dist
    bus_dist = distance_to_buses_json(lat, lon)
    #print bus_dist
    #sys.exit(22)
    #return smallest_distance(lat, lon, bus_data, train_data)
    return min(train_dist, bus_dist)
>>>>>>> fab8796978f738d31e0bf2f2d4c64d0043400629


# Provides the distance from the small business to public transportation
# Input: Requires the lat and long of the business
# Output: Returns a float for the shortest distance to public transportation
<<<<<<< HEAD
# def distance_to_buses_json(lat, lon):
#     params = urllib.urlencode({
#         # Request parameters
#         'Lat': lat,
#         'Lon': lon,
#         # Hardcoded, can be changed
#         'Radius': '250',
#     })
#
#     conn = httplib.HTTPSConnection('api.wmata.com')
#     endpoint = "/Bus.svc/json/jStops?&%s" % params
#     conn.request("GET", endpoint, "{body}", headers)
#     response = conn.getresponse()
#
#     data = json.loads(response.read())
#
#     conn.close()
#
#     return data
#
#
# def distance_to_trains_json(lat, lon):
#     params = urllib.urlencode({
#         # Request parameters
#         'Lat': lat,
#         'Lon': lon,
#         # Hardcoded, can be changed
#         'Radius': '250',
#     })
#
#     conn = httplib.HTTPSConnection('api.wmata.com')
#     endpoint = "/Rail.svc/json/jStationEntrances?&%s" % params
#     conn.request("GET", endpoint, "{body}", headers)
#     response = conn.getresponse()
#
#     data = json.loads(response.read())
#
#     conn.close()
#
#     return data
#
#
# # def distance_calculator_two_coord(business_lat, business_lon, bus_stop_lat, bus_stop_lon):
# #     first = (business_lat, business_lon)
# #     second = (bus_stop_lat, bus_stop_lon)
# #     return great_circle(first, second).miles
#
#
# # def smallest_distance(business_lat, business_lon, bus_data, train_data):
# #
# #     temp_array = []
# #
# #     for i in bus_data["Stops"]:
# #         temp_array.append(distance_calculator_two_coord(business_lat, business_lon, i["Lat"], i["Lon"]))
# #
# #     for i in train_data["Entrances"]:
# #         temp_array.append(distance_calculator_two_coord(business_lat, business_lon, i["Lat"], i["Lon"]))
# #
# #     return min(temp_array)
=======
def distance_to_buses_json(lat, lon):

    endpoint = "https://api.wmata.com//Bus.svc/json/jStops"

    params = {
        'Lat': lat,
        'Lon': lon,
        'Radius': '1000',
    }

    r = requests.get(endpoint, headers=headers, params=params)
    #print r.text

    temp_array = []
    for i in r.json()["Stops"]:
        temp_array.append(distance_calculator_two_coord(lat, lon, i["Lat"], i["Lon"]))

    print min(temp_array)

    #sys.exit(33)

    return min(temp_array)


def distance_to_trains_json(lat, lon):

    #endpoint = "https://api.wmata.com//Bus.svc/json/jStops"
    endpoint = "https://api.wmata.com/Rail.svc/json/jStationEntrances"

    params = {
        'Lat': lat,
        'Lon': lon,
        'Radius': '1000',
    }

    r = requests.get(endpoint, headers=headers, params=params)
    print r.text

    #data = simplejson.loads(response.read())
#    conn.close()

    #pprint(data)


    temp_array = []
    #for i in data["Entrances"]:
    for i in r.json()["Entrances"]:
        temp_array.append(distance_calculator_two_coord(lat, lon, i["Lat"], i["Lon"]))

    print min(temp_array)

    #sys.exit(22)

    return min(temp_array)


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
>>>>>>> fab8796978f738d31e0bf2f2d4c64d0043400629


if __name__ == "__main__":
    main()
