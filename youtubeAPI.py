### ref: https://medium.com/greyatom/youtube-data-in-python-6147160c5833
### 缺total影片量，upload date
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
from youtube_data import youtube_search

test = youtube_search("經常請吃飯的漂亮姐姐")
# print(test.keys())

# print(test['commentCount'][:10])

df = pd.DataFrame(data=test)
# print(df.head())

### Rearranging the columns in the below cell
df1 = df[['title','viewCount','channelTitle','commentCount','likeCount','dislikeCount','tags','favoriteCount','videoId','channelId','categoryId']]
df1.columns = ['Title','viewCount','channelTitle','commentCount','likeCount','dislikeCount','tags','favoriteCount','videoId','channelId','categoryId']
# print(df1.head())


# ### convert the numbers from string to integer.
numeric_dtype = ['viewCount','commentCount','likeCount','dislikeCount','favoriteCount']
for i in numeric_dtype:
    df1[i] = df[i].astype(int)

ImagineDragons = df1[df1['channelTitle']=='ImagineDragonsVEVO']
# print(ImagineDragons.head())

df2 = df[['title','viewCount','commentCount','likeCount','dislikeCount','videoId']]
# print(df2.head())

for i in range(10):
	print(df2['title'][i])
	print('觀看次數: ',df2['viewCount'].ix[i] ,'\t留言量:', df2['commentCount'][i], '\tLike:', df2['likeCount'][i], '\tDislike:', df2['dislikeCount'][i])

# ImagineDragons = ImagineDragons.sort_values(ascending=False,by='viewCount')
# plt.bar(range(ImagineDragons.shape[0]),ImagineDragons['viewCount'])
# plt.xticks(range(ImagineDragons.shape[0]),ImagineDragons['Title'],rotation=90)
# plt.ylabel('viewCount in 100 millions')

# plt.show()