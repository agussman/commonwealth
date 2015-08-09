import rauth
import time
import json


def main():
    locations = [(38.9048907, -77.0339064)]
    api_calls = []
    for lat, long in locations:
        params = get_search_parameters(lat, long)
        api_calls.append(get_results(params))
        # Be a good internet citizen and rate-limit yourself
        time.sleep(1.0)

    file = "testFile.txt"

    f = open(file, "w")

    json.dump(api_calls[0], f)


    f.close()


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


def get_search_parameters(lat, long):
    # See the Yelp API for more details

    params = {}
    params["term"] = "restaurant"
    params["ll"] = "{},{}".format(str(lat), str(long))
    params["radius_filter"] = "2000"
    params["limit"] = "10"

    return params

if __name__ == "__main__":
    main()
