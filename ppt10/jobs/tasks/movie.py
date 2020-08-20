from flask_script import Command
from application import app,db
import requests,os,time,hashlib,json
from bs4 import BeautifulSoup
from common.libs.DateHelper import getCurrentTime
from urllib.parse import urlparse

class JobTask( Command ):
  def __init__(self):
    self.source = "btbtdy"
    self.url = {
      "num":3,
      "url":"http://btbtdy2.com/btfl/dy1-#d#.html",
      "path":"/tmp/%s/"%(self.source)
    }

  # 第一步，获取列表list html 回来，通过解析html获取详情的url信息，根据详情的url获取详情的html
  # 第二部，解析详情的html
  def run(self,params):
    self.date = getCurrentTime(frm="%Y%m%d")
    self.getList()

  # 获取列表
  def getList(self):
    config = self.url
    # 存放爬取资源的路径
    path_root=config['path'] + self.date
    path_list = path_root + "/list"
    path_info = path_root + "/info"
    path_json = path_root + "/json"
    self.makeSuredirs(path_root)
    self.makeSuredirs(path_list)
    self.makeSuredirs(path_info)
    self.makeSuredirs(path_json)

    # 获取的页码
    pages = range(1,config['num']+1)
    # 获取列表的信息
    for ind in pages:
      # 列表路径
      tmp_path = path_list + '/' + str(ind)
      tmp_url = config['url'].replace('#d#',str(ind))
      # 对已经获取的页面不再进行爬取
      if os.path.exists(tmp_path):
        continue
      tmp_content = self.getHttpContent(tmp_url)
      self.saveContent(tmp_path,tmp_content)
      # 每获取完一个页面，停顿0.3秒，防止反爬虫
      time.sleep(0.3)

    for ind in os.listdir(path_list):
      # 列表内容
      tmp_content = self.getContent(path_list + '/' + str(ind))
      # 获取列表内的影视信息
      items_data = self.parseList(tmp_content)
      if not items_data:
        continue
      # 将列表影视信息用json存起来
      for item in items_data:
        tmp_json_path = path_json + '/' + item['hash']
        tmp_info_path = path_info + '/' + item['hash']
        if not os.path.exists(tmp_json_path):
          self.saveContent(tmp_json_path,json.dumps(item,ensure_ascii=False))
        # 存储影视的详情信息
        if not os.path.exists(tmp_info_path):
          tmp_content = self.getHttpContent(item['url'])
          self.saveContent(tmp_info_path,tmp_content)

        time.sleep(0.3)

      # app.logger.info("tmp_content ：",tmp_content)

  # 解析列表数据
  def parseList(self,content):
    data = []
    config = self.url
    url_info = urlparse(config['url'])
    # 获取到域名，和列表数据提供的相对路径结合可以得到完整的url地址
    url_domain = url_info[0]+'://'+url_info[1]

    tmp_soup = BeautifulSoup(str(content),'html.parser')
    tmp_list = tmp_soup.select("div.list_su ul li")
    for item in tmp_list:
      tmp_target = item.select("a.pic_link")
      tmp_name = tmp_target[0]["title"]
      tmp_href = tmp_target[0]["href"]
      if 'http:' not in tmp_href:
        tmp_href = url_domain + tmp_href

      tmp_data = {
        'name':tmp_name,
        'url':tmp_href,
        'hash':hashlib.md5(tmp_href.encode('utf-8')).hexdigest(),
      }
      data.append(tmp_data)

    # print("data ：",data)
    return data

  # 获取文件内容
  def getContent(self,path):
    if os.path.exists(path):
      with open(path,mode='r',encoding='utf-8') as f:
        return f.read()
    return ''

  # 保存内容
  def saveContent(self,path,content):
    if content:
      with open(path,mode='w+',encoding='utf-8') as f:
        if type(content) != str:
          content = content.decode('utf-8')
        f.write(content)
        f.flush()
        f.close()
    
  def getHttpContent(self,url):
    try:
      r = requests.get(url)
      if r.status_code != 200:
        return None
      return r.content
    except Exception:
      return None

  # 确保某一路径是否存在
  def makeSuredirs(self,path):
    if not os.path.exists(path):
      os.makedirs(path)