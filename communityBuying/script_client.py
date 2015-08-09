from urllib import urlencode
from yelpclient import YelpClient

import logging
import oauth2
import requests
import time

keys = {
    'consumer_key': 'jb_FCNZnRQUl-ZBYIC7AMQ',
    'consumer_secret': '9w2belyaG3TQljVJ3AFqAct2zsQ',
    'token': 'nwmC3CUV1Gq8W8idtT2SIhVsPEqYVVhj',
    'token_secret': 'PHG1XzFh0r5ZVQpDt74VN-TN5bs',
}

client = YelpClient(keys)


def main():
    lat = 38.9048907
    long = -77.0339064
    provideJsonList(lat, long)


def provideJsonList(lat, long):
    return client.search_by_geo_coord(latlong=(lat, long), term="restaurants", limit=40)


if __name__ == "__main__":
    main()
