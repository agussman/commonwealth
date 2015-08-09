########### Python 2.7 #############
import httplib, urllib, base64


#-API KEY- 742e08c7b5324dfcb1a51cfbba70c8f8

headers = {
    # Request headers
    'api_key': '{subscription key}',
}

params = urllib.urlencode({
    # Request parameters
    'Lat': '{number}',
    'Lon': '{number}',
    'Radius': '{number}',
})

try:
    conn = httplib.HTTPSConnection('api.wmata.com')
    endpoint = "/Bus.svc/json/jStops&%s" % params
    print conn


    conn.request("GET", endpoint, "{body}", headers)
    response = conn.getresponse()

    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))