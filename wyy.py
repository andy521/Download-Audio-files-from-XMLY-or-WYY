#coding:utf-8  
import requests
import re
from multiprocessing import Pool
from bs4 import BeautifulSoup
import os

headers = {
    'Referer': 'https://music.163.com/',
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"}

def get_list(data, dir):
    playlist_url = "https://music.163.com/playlist?id=%s" % data
    res = requests.get(playlist_url, headers=headers)
    fil = open('file.txt', 'w', encoding='UTF-8')
    fil.write(res.text)

    name = re.findall(r'<h2 class="f-ff2 f-brk">(.*?)</h2>', res.text)
    os.mkdir(dir+'/'+name[0])
    for i in re.findall(r'<a href="/song\?id=(\d+)">(.*?)</a>', res.text):
        download_url = "http://music.163.com/song/media/outer/url?id=%s" % i[0]

        try:
            with open(dir+'/'+name[0]+'/' + i[1]+'.mp3', 'wb') as f:
                f.write(requests.get(download_url, headers=headers).content)
        except FileNotFoundError:
            pass
        except OSError:
            pass
        yield i[1] + ' download successfully!'
    
def get_song(data, dir):
    song_url = "https://music.163.com/song?id=%s" % data
    res = requests.get(song_url, headers=headers)
    name = re.findall(r'<em class="f-ff2">(.*?)</em>', res.text)
    download_url = "http://music.163.com/song/media/outer/url?id=%s" % data
    try:
        with open(dir+'/' + name[0]+'.mp3', 'wb') as f:
            f.write(requests.get(download_url, headers=headers).content)
    except FileNotFoundError:
        pass
    except OSError:
        pass
    return name[0]+' downloaded successfully!'