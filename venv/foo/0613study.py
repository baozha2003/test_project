import requests

result = requests.get('http://www.baidu.com')
print(result.text)

requests.post()