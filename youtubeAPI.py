### ref: https://medium.com/greyatom/youtube-data-in-python-6147160c5833
### ref video resource: https://developers.google.com/youtube/v3/docs/videos#resource

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
from youtube_data import youtube_search

import urllib.parse
from bs4 import BeautifulSoup
import requests



# query_string = urllib.parse.unquote(query_string)
# print(query_string)
query_string = input("搜尋:")
test = youtube_search(query_string)
# print(test.keys())

query_string2 = urllib.parse.urlencode({"search_query" : query_string})
response = requests.get("http://www.youtube.com/results?" + query_string2)
soup = BeautifulSoup(response.text, 'lxml')
 
#<p class="num-results first-focus">約 1,250 項結果</p>
print('影片數量: ', soup.find('p', 'num-results first-focus').getText(),'\n')


# print(test['commentCount'][:10])

df = pd.DataFrame(data=test)
# print(df.head())

### Rearranging the columns in the below cell
df1 = df[['title','publishedAt','viewCount','channelTitle','commentCount','likeCount','dislikeCount','tags','favoriteCount','videoId','channelId','categoryId']]
df1.columns = ['Title','publishedAt','viewCount','channelTitle','commentCount','likeCount','dislikeCount','tags','favoriteCount','videoId','channelId','categoryId']
# print(df1.head())


# ### convert the numbers from string to integer.
numeric_dtype = ['viewCount','commentCount','likeCount','dislikeCount','favoriteCount']
for i in numeric_dtype:
    df1[i] = df[i].astype(int)

# ImagineDragons = df1[df1['channelTitle']=='ImagineDragonsVEVO']
# print(ImagineDragons.head())

df2 = df[['title','publishedAt','viewCount','commentCount','likeCount','dislikeCount','videoId']]
# print(df2.head())

for i in range(20):
	print(df2['title'][i])
	print('發布時間:',df2['publishedAt'][i], '\t觀看次數:',df2['viewCount'].ix[i], '\t留言量:', df2['commentCount'][i], '\tLike:', df2['likeCount'][i], '\tDislike:', df2['dislikeCount'][i])
	print()
# ImagineDragons = ImagineDragons.sort_values(ascending=False,by='viewCount')
# plt.bar(range(ImagineDragons.shape[0]),ImagineDragons['viewCount'])
# plt.xticks(range(ImagineDragons.shape[0]),ImagineDragons['Title'],rotation=90)
# plt.ylabel('viewCount in 100 millions')

# plt.show()