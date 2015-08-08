from flask import Flask, request
from flask_restful import Resource, Api
from rauth import OAuth1Session
import time

app = Flask(__name__)
api = Api(app)

consumer_key = "jb_FCNZnRQUl-ZBYIC7AMQ"
consumer_secret = "9w2belyaG3TQljVJ3AFqAct2zsQ"
token = "nwmC3CUV1Gq8W8idtT2SIhVsPEqYVVhj"
token_secret = "PHG1XzFh0r5ZVQpDt74VN-TN5bs"

def get_search_parameters(lat, long):

    params = {}
    params["term"] = "restaurant"
    params["ll"] = "{},{}".format(str(lat), str(long))
    params["radius_filter"] = "2000"
    params["limit"] = "40"


if __name__ == '__main__':

    app.run(debug=True)



class yelp_api_call(Resource):

    def get(self, params):

        session = OAuth1Session ()

    def put(self, todo_id):

        return

    def get_results(params):

        session = OAuth1Session(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=token,
            access_token_secret=token_secret
        )

        request_api = session.get(
            "http://api.yelp.com/v2/search",
            params=params
        )

        data = request_api.json()
        session.close()
        return data