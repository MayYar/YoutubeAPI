import urllib.parse
from bs4 import BeautifulSoup
import requests

# reference: https://www.codeproject.com/Articles/873060/Python-Search-Youtube-for-Video
# https://hiskio.com/courses/112

query_string = urllib.parse.urlencode({"search_query" : input("搜尋: ")})
response = requests.get("http://www.youtube.com/results?" + query_string)
soup = BeautifulSoup(response.text, 'lxml')
#影片連結
#<p class="num-results first-focus">約 1,250 項結果</p>
print('影片數量: ', soup.find('p', 'num-results first-focus').getText(),'\n')
#div class="yt-lockup-content"><h3 class="yt-lockup-title ">
search_results = soup.find_all('div', 'yt-lockup-content')

for all_mv in soup.select(".yt-lockup-video"):
    print(all_mv.select("a[rel='spf-prefetch']")[0].get("title"))
    data = all_mv.select(".yt-lockup-meta-info")
    time = data[0].get_text("#").split("#")[0]
    see = data[0].get_text("#").split("#")[1]
    print("上傳時間:", time, end = "  ")
    print(see,'\n')

