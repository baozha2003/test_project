import requests

url = "http://sytest.54315.com/login"

querystring = {"mobile": "13727086330", "password": "qwe123"}

headers = {
    'Cache-Control': "no-cache"
}

response = requests.request("POST", url, headers=headers, params=querystring)
print(response.text)
print(response.cookies['ucsid'])
print(response.headers)