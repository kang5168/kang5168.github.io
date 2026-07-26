import requests
from bs4 import BeautifulSoup

# 1. 百度热搜页面
url = "https://top.baidu.com/board?tab=realtime"

# 2. 伪装成真正的浏览器 header（防止被反爬拦截）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 3. 发送请求
response = requests.get(url, headers=headers)

# 4. 解析网页，提取热搜标题
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all("div", class_="c-single-text-ellipsis")

print("--- 今日百度热搜 ---")
for index, title in enumerate(titles[:10], start=1):
    print(f"{index}. {title.text.strip()}")
