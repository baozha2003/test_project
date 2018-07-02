import requests

url = "http://sytest.54315.com/login"

querystring = {"mobile": "13727086330", "password": "qwe123"}

headers = {
    'Cache-Control': "no-cache"
}

response = requests.request("POST", url, headers=headers, params=querystring)
print(response.text)
#获取到cookie信息从中获取ucsid信息。
ucsid = response.cookies['ucsid']

url = "http://sytest.54315.com/codeprint/print"

querystring = {"packId": "363"}

headers = {
    'Cookie': "ucsid=%s" % ucsid
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
