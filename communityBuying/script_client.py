from yelpclient import YelpClient
import json

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
    json_file = provide_json_list(lat, long)

    f = open("food_search.json", "w")
    json.dump(json_file, f)
    f.close()


# Provide Json List: Create List for Local businesses in the surrounding area
# Input: Lat, Long both in float value
# Output: Json file of stores
def provide_json_list(lat, long):

    return client.search_by_geo_coord(latlong=(lat, long), term="food", limit=1, radius=2000)



if __name__ == "__main__":
    main()
