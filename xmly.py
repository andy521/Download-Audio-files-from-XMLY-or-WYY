#coding:utf-8  
import requests
from bs4 import BeautifulSoup
import re
import os
import random
import time
import json

download_pool = []
def gethtml(url):    # 获取网站 html 信息
    headers = {

        "Host": "www.ximalaya.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0",

        }
    # 用的代理 ip，如果被封的，在http://www.xicidaili.com/换一个
    html = requests.get(url, headers=headers)   # 请求网页信息
    return html


def getNumOfEpisodes(book_Id):
    req = gethtml('https://www.ximalaya.com/'+'jiaoyu'+'/'+str(book_Id)+'/p'+str(1))

    result = req.text

    b = re.findall (u"专辑里的声音\(<!-- -->([\d]*)",result)

    return int(b[0])


def getid(keyword=''): 
    albumurl = 'https://www.ximalaya.com/search/album/{}/sc/p1'.format(keyword)    # 输入关键字，拼接链接
    html = gethtml(albumurl)
    soup = BeautifulSoup(html.text, 'lxml')
    info = soup.select('#searchPage div.search-type div.common-tab-content div.xm-loading ul div '
                       'a.xm-album-title.ellipsis-2')    # 提取音频文件的信息
    idinfo = re.compile('href="/.*?"').findall(str(info))     # 提取专辑中 id
    titleinfo = re.compile('title=".*?"').findall(str(info))     # 提取专辑中标题信息

    ids = []
    titles = []
    NumsOfEpisodes = []

    for j in idinfo:
        ids.append(str(j))
    for t in titleinfo:
        # 处理下标题，防止创建文件夹失败
        title = str(t).split('"')[1].replace('\\', ' ').replace('/', ' ').replace(':', ' ').replace('*', ' ')\
            .replace('?', ' ').replace('"', ' ').replace('<', ' ').replace('>', ' ').replace('|', ' ')
        titles.append(title)
    for k in ids:
        NumsOfEpisodes.append(getNumOfEpisodes(k.split('/')[2]))
    
    for i in range(len(titles)):
        yield (titles[i]+' id:'+ids[i]+' 集数：'+str(NumsOfEpisodes[i]))

def download(url, path):
    if url not in download_pool:
        req = gethtml(url)
        result = req.text
        result = json.loads(result)
        title = result['title']
        data_url = result['play_path_64']

        try:
            with open(path+'/'+'%s.m4a'%title,'wb') as f:
                data = requests.get(data_url).content
                f.write(data)
            download_pool.append(url)
            return title
        except Exception as e:
            return str(e)
            


def get_EpisodeId(bookID, page):

    req = gethtml('https://www.ximalaya.com/'+str(bookID)+'/p'+str(page))

    result = req.text

    id_number = re.findall('/'+str(bookID)+'/([\d]*)',result)

    id_number = set(id_number)  

    id_number.remove('')
    numbers = [ int(x) for x in id_number ] 
    numbers = sorted(numbers)
    '''
    numbers_fixed = numbers[:]

    for i in range(len(numbers)):
        print(len(numbers))
        if numbers[i] in ID_pool:
            #print('Same')
            numbers_fixed.remove(numbers[i])
        else :
            #print('Add')
            ID_pool.append(numbers[i])

    print(len(numbers_fixed))
    '''
    id_number = [ str(x) for x in numbers ] 

    id = []
    for number in id_number:
        id.append('http://www.ximalaya.com/tracks/' + number + '.json')  # 这样构造url是不太严谨的，当然在这里是可以的，以后再探讨 url 的构造方法
    print(len(id))

    return id

