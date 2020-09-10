from flask_script import Command
from application import app,db
import requests,os,time,hashlib,json,re
from bs4 import BeautifulSoup
from common.libs.DateHelper import getCurrentTime
from common.models.movie import Movie
from urllib.parse import urlparse

class JobTask( Command ):
  def __init__(self):
    self.source = "btbtdy"
    self.url = {
      "num":4,
      "url":"http://btbtdy2.com/btfl/dy1-#d#.html",
      "path":"/tmp/%s/"%(self.source)
    }

  # 第一步，获取列表list html 回来，通过解析html获取详情的url信息，根据详情的url获取详情的html
  # 第二部，解析详情的html
  def run(self,params):
    act = params['act']
    self.date = getCurrentTime(frm="%Y%m%d")
    if act == 'list':
      self.getList()
      self.parseInfo()
    elif act == 'parse':
      self.parseInfo()

  # 获取列表
  def getList(self):
    config = self.url
    # 存放爬取资源的路径
    path_root=config['path'] + self.date
    path_list = path_root + "/list"
    path_info = path_root + "/info"
    path_json = path_root + "/json"
    path_vid = path_root + "/vid"
    self.makeSuredirs(path_root)
    self.makeSuredirs(path_list)
    self.makeSuredirs(path_info)
    self.makeSuredirs(path_json)
    self.makeSuredirs(path_vid)

    # 获取的页码
    pages = range(0,config['num']+1)
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
        tmp_vid_path = path_vid + '/' + item['hash']
        if not os.path.exists(tmp_json_path):
          self.saveContent(tmp_json_path,json.dumps(item,ensure_ascii=False))
        # 存储影视的详情信息
        if not os.path.exists(tmp_info_path):
          tmp_content = self.getHttpContent(item['url'])
          self.saveContent(tmp_info_path,tmp_content)

        # 存储影视下载页面的信息(获取HTML失败返回空)
        if not os.path.exists(tmp_vid_path):
          tmp_content = self.getHttpContent(item['vid_url'])
          self.saveContent(tmp_vid_path,tmp_content)

        time.sleep(0.1)

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

      tmp_vid_url = tmp_href.replace('btdy/dy','vidlist/')

      tmp_data = {
        'name':tmp_name,
        'url':tmp_href,
        'vid_url':tmp_vid_url,
        'hash':hashlib.md5(tmp_href.encode('utf-8')).hexdigest(),
      }
      data.append(tmp_data)

    # print("data ：",data)
    return data

  # 解析详情信息
  def parseInfo(self):
    config = self.url
    path_root=config['path'] + self.date
    path_info = path_root + "/info"
    path_json = path_root + "/json"
    for filename in os.listdir(path_info):
      tmp_json_path = path_json + '/' + filename
      tmp_info_path = path_info + '/' + filename
      tmp_data = json.loads(self.getContent(tmp_json_path), encoding='utf-8')
      # 获取到详情页的HTML信息
      tmp_content = self.getContent(tmp_info_path)
      tmp_soup = BeautifulSoup(str(tmp_content),'html.parser')
      try:
        tmp_pub_date = tmp_soup.select('div.vod .vod_intro dl dd')[0].getText()
        tmp_desc = tmp_soup.select('div.vod .vod_intro .des')[0].getText()
        tmp_classify = tmp_soup.select('div.vod .vod_intro dl dd')[2].getText()
        tmp_actor = tmp_soup.select('div.vod .vod_intro dl dd')[6].getText()
        tmp_pic_list = tmp_soup.select('div.vod .vod_img img')
        tmp_pics = []
        for tmp_pic in tmp_pic_list:
          tmp_pics.append(tmp_pic['src'])
          break


        # 获取下载地址
        tmp_download_url = tmp_data['url'].replace('btdy/dy','vidlist/')
        
        if tmp_pics:
          tmp_data['cover_pic'] = tmp_pics[0]
        
        tmp_data['pub_date'] = tmp_pub_date
        tmp_data['desc'] = tmp_desc
        tmp_data['classify'] = tmp_classify
        tmp_data['actor'] = tmp_actor
        tmp_data['magnet_url'] = tmp_download_url
        tmp_data['source'] = self.source
        tmp_data['created_time'] = tmp_data['update_time'] = getCurrentTime()

        # print("tmp_data ：",tmp_data)
        # 存储前先查询是否有此条数据
        tmp_movie_info = Movie.query.filter_by(hash=tmp_data['hash']).first()
        if tmp_movie_info:
          continue
        tmp_model_movie = Movie(**tmp_data)
        db.session.add(tmp_model_movie)
        db.session.commit()

      except:
        pass

    return True
        

      

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