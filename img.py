# -*- coding: utf-8
import json
import time

import requests
from PIL import Image
from io import BytesIO
from docx import Document

text = """125 分值：0.70 归类：资料分析
正确答案：C
A项，由表格可知，2020年前三季度，全国居民人均可支配收入平均数比上年增长3.9%，2019年前三季度，全国居民人均可支配收入平均数比上年增长8.8%，则所求为1+3.9%+8.8%+3.9%×8.8%&gt;1+3.9%+8.8%=1.127倍，正确；<br/> B项，由饼形图可知，2020年前三季度，人均衣着支出和生活用品及服务支出在人均消费支出中的占比均为6%，即两者相等，正确；<br/> C项，由表可知，2019年前三季度，全国居民人均可支配收入平均数22882元，同比增长8.8%，所求为<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_a57d58b42b2be82f.gif" align="bottom"/> ×8.8%≈<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_ebb379280793e838.gif" align="bottom"/> =<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_7081fa6796001786.gif" align="bottom"/> =18XX元，错误，直接选择C项。<br/> 验证D项，由第二段可知，2020年前三季度，全国居民人均消费支出14923元，城镇居民人均消费支出19247元，农村居民人均消费支出9430元，根据十字交叉法可得，<br/><img src="https://s.eoffcn.com/tiku/question/20210226/9a19bcf2d392aa806c47b4921403d794.jpg" title="1614325557252006.png" width="326" height="134" alt="微信截图_20210226154318.png"/> <br/> 城镇人口是农村人口的<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_f773554e930b5ff0.gif" align="bottom" hspace="8"/> =<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_79771e9c5b25d347.gif" align="bottom" hspace="8"/> ≈<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_1f10537ef31a897e.gif" align="bottom" hspace="8"/> ≈1.27倍，正确。

126 分值：0.70 归类：资料分析
正确答案：D
由图2可知，2019年，12月实物商品网上零售额累计值为85239.5亿元，6月累计值为38164.9亿元，则2019年下半年，实物商品网上零售额环比增长85239.5-38164.9-38164.9=8909.7亿元，排除A、B项；环比增速为<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_874f03c29780c503.gif" align="bottom" hspace="8"/> ≈<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_84db613a6ebd0600.gif" align="bottom" hspace="8"/> =23.X%，故选择D项。

127 分值：0.70 归类：资料分析
正确答案：A
由图可知，2019年10月，非实物商品网上零售额占网上零售额的比重为1-<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_56a582fe65cc08a6.gif" align="bottom"/> =1-<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_be095701e8aa895c.gif" align="bottom"/> ≈1-<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_e7bc260a75bd2c08.gif" align="bottom"/> =1-8X%=1X%<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_a8768e5b46e1c193.gif" align="bottom"/> 20%；同理，11月的比重为1-<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_345f4bb3bc2b8dea.gif" align="bottom"/> =1-<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_5258def619136365.gif" align="bottom"/> ≈1-<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_5a44cf9e6e3559cd.gif" align="bottom"/> =1-8X%=1X%<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_a8768e5b46e1c193.gif" align="bottom"/> 20%；12月的比重为1-<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_65c52feaac0939fd.gif" align="bottom"/> =1-<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_bd8ac88101a1cea3.gif" align="bottom"/> ≈1-<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_c1af74765fff41a8.gif" align="bottom"/> =1-8X%=1X%<img src="https://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_a8768e5b46e1c193.gif" align="bottom"/> 20%。综上所述，2019年10-12月份，非实物商品网上零售额占网上零售额的比重均不超过20%，故选择A项。"""

# def download(img_url):
#     r = session.get(img_url)
#     print(r.status_code)
#     img = Image.open(BytesIO(r.content))
#     img.save('dsfads.gif')
#
if __name__ == '__main__':
    # session = requests.session()
    # raw_headers = """Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNzY1ODE5NiIsInBob25lIjoiMTg5Njg5OTU4ODEiLCJjcmVhdGVfdGltZSI6MTYyMDQ0MTEzNSwidXBkYXRlX3RpbWUiOjE2MjA0NDExMzUsInN5c3RlbSI6IjI5IiwicGxhdGZvcm0iOiJBbmRyb2lkIiwidmVyc2lvbiI6IjQuMTIuMCIsInNka192ZXJzaW9uIjoiNC4xMi4wIiwibmlja25hbWUiOiIxODk2ODk5NTg4MSIsImF2YXRhciI6IiIsImdlbmRlciI6ImYiLCJzc29faWQiOjIwNjMyOTkyLCJ3ZWlib19pZCI6IiIsInFxX2lkIjoiIiwid2VpeGluX2lkIjoiIiwid2VpYm9fbmlja25hbWUiOiIiLCJxcV9uaWNrbmFtZSI6IiIsIndlaXhpbl9uaWNrbmFtZSI6IiIsImxvZ2luX3R5cGUiOiJwaG9uZSIsInVzZXJfZnJvbSI6MTUsImNvZGUiOiJHQ1RTVCIsImlhdCI6MTYyMDQ0MTEzNSwibmJmIjoxNjIwNDQxMTM1LCJleHAiOjE2NTE5NzcxMzV9.TQp3Y4KD-o_X_8TL-LNeKCyQ0ZIMsIXWsrAZLETDm4A
    # Referer: http://tiku.eoffcn.com/apiv3/
    # Content-Type: application/x-www-form-urlencoded
    # Accept-Encoding: gzip
    # User-Agent: okhttp/4.2.2"""
    # for s in raw_headers.split("\n"):
    #     key, val = list(map(str.strip, s.split(": ")))
    #     session.headers[key] = val
    #
    # r = session.get(
    #     'http://s.eoffcn.com/tiku/html/2021022417551775/25ed69b110a1a82038c41c93ed01237c_html_56a582fe65cc08a6.gif')
    # print(r.status_code)
    # img = Image.open(BytesIO(r.content))
    # img.save('dsfads.gif')
    text = text.replace('<br/> ', '\n')
    print(text)
