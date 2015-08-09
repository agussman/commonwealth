########### Python 2.7 #############
import httplib, urllib, base64


#-API KEY- 742e08c7b5324dfcb1a51cfbba70c8f8

#curl -v -X GET "https://api.wmata.com/Bus.svc/json/jStops?Lat=38.8995873500&Lon=-77.02773&Radius=3" -H "api_key: 742e08c7b5324dfcb1a51cfbba70c8f8"


headers = {
    # Request headers
    'api_key': '742e08c7b5324dfcb1a51cfbba70c8f8',
}

params = urllib.urlencode({
    # Request parameters
    'Lat': '38.89958735000000',
    'Lon': '-77.02773315',
    'Radius': '1000',
})

try:
    conn = httplib.HTTPSConnection('api.wmata.com')
    endpoint = "/Bus.svc/json/jStops?&%s" % params
    #print (endpoint)


    conn.request("GET", endpoint, "{body}", headers)
    response = conn.getresponse()

    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))