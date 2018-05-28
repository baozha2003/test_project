from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://python.org/')

# 获取页面上的所有链接。
all_links = r.html.links
print(all_links)

# 获取页面上的所有链接，以绝对路径的方式。
all_absolute_links = r.html.absolute_links
print(all_absolute_links)
