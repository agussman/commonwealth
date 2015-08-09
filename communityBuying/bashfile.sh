@ECHO OFF

curl -v -X GET "https://api.wmata.com/Rail.svc/json/jStationInfo?StationCode=A01"
-H "api_key: {7961aa3d40014056934b2a43c56fbaee}"

--data-ascii "{body}" 
