import requests

from bs4 import BeautifulSoup

URL = 'https://adzhp.cn'

def crawler():
  r = requests.get(URL)
  r.raise_for_status()
  return r.text

def query(list):
  str = ''
  for item in list:
    if(item.get('data-url')):
      str += '网站名称: ' + item.get('title') + '\n网站地址: ' + item.get('data-url') + '\n'
  return str

def writeFile(text):
  f = open('./text.txt', 'w')
  f.write(str)
  f.close()   

try:
  soup = BeautifulSoup(crawler(), features='html.parser')

  list = soup.find_all('a')

  str = query(list)

  writeFile(str)

  print('爬取成功')
except:
  print('爬取失败')