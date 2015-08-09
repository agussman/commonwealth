########### Python 2.7 #############
import httplib, urllib, base64

headers = {
    'api_key': '{742e08c7b5324dfcb1a51cfbba70c8f8}',
}

params = urllib.urlencode({

    'StationCode': 'A01',
})

conn = httplib.HTTPSConnection('api.wmata.com')
conn.request("GET", "/Rail.svc/json/jStationInfo?&%s" % params, "{body}", headers)
response = conn.getresponse()
data = response.read()
print(data)
conn.close()
print("[Errno {0}] {1}".format(e.errno, e.strerror))
