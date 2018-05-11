import requests
import re

url = "https://api.douban.com/v2/book/search?q=python&fields=id,title"
reponse = requests.get(url)
print(reponse)
list_1 = reponse.text
print(list_1)
# ls_1 ={"count":20,"start":0,"total":1594,"books":[
#     {"id":"10561367","title":"Head First Python（中文版）"},
#     {"id":"6025284","title":"Python灰帽子"},
#     {"id":"2152386","title":"Python网络编程基础"},
#     {"id":"4866934","title":"Python基础教程"},
#     {"id":"4915945","title":"Python Algorithms"},
#     {"id":"26005639","title":"父与子的编程之旅"},
#     {"id":"3112503","title":"Python核心编程（第二版）"},
#     {"id":"25779298","title":"利用Python进行数据分析"},
#     {"id":"26340992","title":"贝叶斯思维"},
#     {"id":"3740086","title":"Django Web开发指南"},
#     {"id":"3117898","title":"Python源码剖析"},
#     {"id":"3948354","title":"Python学习手册"},
#     {"id":"26829016","title":"Python编程：从入门到实践"},
#     {"id":"11610789","title":"Python入门经典"},
#     {"id":"1426816","title":"学习Python"},
#     {"id":"26702570","title":"python绝技：运用python成为顶级黑客"},
#     {"id":"3285148","title":"Expert Python Programming"},
#     {"id":"26264642","title":"\"笨办法\"学Python"},
#     {"id":"26709315","title":"Effective Python"},
#     {"id":"26675127","title":"Python语言及其应用"}]}
