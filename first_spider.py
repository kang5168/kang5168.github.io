import requests

# 1. 目标网址（这里以一个专门用来测试爬虫的公开网站为例）
url = ["https://www.blued.cn"]

# 2. 发送请求获取网页内容
response = requests.get(url)

# 3. 打印出抓取到的内容
print("抓取成功！网站返回的内容是：")
print(response.text)
