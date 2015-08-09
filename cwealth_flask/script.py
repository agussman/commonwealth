import unirest

# These code snippets use an open-source library. http://unirest.io/python
response = unirest.get(
    "https://jgentes-Crime-Data-v1.p.mashape.com/crime?enddate=6%2F25%2F2014&lat=42.343060293817736&long=-83.0579091956167&startdate=6%2F19%2F2014",
    headers={
        "X-Mashape-Key": "sm6t1jlrl2mshA8HWiFSYMJiskOCp1uzNCqjsnyro7XKbN0swx",
        "Accept": "application/json"
    }
)
