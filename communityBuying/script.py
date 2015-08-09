import json

import rauth


def main():

    json_data = get_results(get_search_parameters(38.9048907, -77.0339064))

    print "Name:", json_data["businesses"][0]["name"]
    print "ID:", json_data["businesses"][0]["id"]
    print "Image URL:", json_data["businesses"][0]["image_url"]
    print "Phone Number:", json_data["businesses"][0]["phone"]
    print json_data["businesses"][0]["location"]["display_address"][0]
    print json_data["businesses"][0]["location"]["display_address"][1]
    print json_data["businesses"][0]["location"]["display_address"][2]


# Requests to Yelp API - Function
# Input: parameters to call API Function
# Output: json Query
def get_results(params):
    # Obtain these from Yelp's manage access page
    consumer_key = "jb_FCNZnRQUl-ZBYIC7AMQ"
    consumer_secret = "9w2belyaG3TQljVJ3AFqAct2zsQ"
    token = "nwmC3CUV1Gq8W8idtT2SIhVsPEqYVVhj"
    token_secret = "PHG1XzFh0r5ZVQpDt74VN-TN5bs"

    session = rauth.OAuth1Session(
        consumer_key=consumer_key
        , consumer_secret=consumer_secret
        , access_token=token
        , access_token_secret=token_secret)

    request = session.get("http://api.yelp.com/v2/search", params=params)

    # Transforms the JSON API response into a Python dictionary
    data = request.json()

    session.close()

    return data


# Input: Requires Latitude & Longitude
# Output: Returns Param String for Calling YELP API
def get_search_parameters(lat, long):
    # See the Yelp API for more details
    params = {}

    # Hardcoded Term Searches, can be changed
    params["term"] = "restaurant"
    params["ll"] = "{},{}".format(str(lat), str(long))
    params["radius_filter"] = "2000"
    params["limit"] = "1"

    return params




if __name__ == "__main__":
    main()
