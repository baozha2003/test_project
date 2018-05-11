import requests
import re

url = "http://www.521609.com/daxuexiaohua/list3%s.html"

for i in range(1, 15):
    html = url % i
    # print(temp)
    response = requests.get(html)
    # print(response)
    temp = response.text
    # print(temp)
    img_urls = re.findall(r'/uploads/.*?\.jpg', temp)
    for img_url in img_urls:
        img_reponse = requests.get('http://www.521609.com%s' % img_url)
        # print(img_reponse)
        img_data = img_reponse.content
        mingzi = img_url.split('/')[-1]
        print(mingzi)
        with open(mingzi, 'wb') as f:
            f.write(img_data)