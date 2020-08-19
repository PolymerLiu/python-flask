from flask_script import Command
from application import app,db
import requests,os,time
from bs4 import BeautifulSoup
from common.libs.DateHelper import getCurrentTime

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
    for ind in pages:
      # 列表路径
      tmp_path = path_list + '/' + str(ind)
      tmp_url = config['url'].replace('#d#',str(ind))
      # 对已经获取的页面不再进行爬取
      if os.path.exists(tmp_path):
        continue
      tmp_content = self.getHttpContent(tmp_url)
      self.saveContent(tmp_path,tmp_content)
      # app.logger.info("tmp_content：",tmp_content)
      # 没获取完一个页面，停顿0.3秒，防止反爬虫
      time.sleep(0.3)

    for ind in os.listdir(path_list):
      tmp_content = self.getContent(path_list + '/' + str(ind))
      # app.logger.info("tmp_content：",tmp_content)
      # print("tmp_content：",tmp_content)

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
    pass
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