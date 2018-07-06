import requests

url = "http://sytest.54315.com/login"

querystring = {"mobile": "13727086330", "password": "qwe123"}

headers = {
    'Cache-Control': "no-cache"
}

response = requests.request("POST", url, headers=headers, params=querystring)
ucsid = response.cookies['ucsid']

url = "http://sytest.54315.com/codeprint/print"

querystring = {"packId": "396"}

headers = {
    'Cookie': "ucsid=%s" % ucsid
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
