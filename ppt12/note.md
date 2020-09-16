BeautifulSoup 使用说明
def run(self,params):
    url = "http://btbtdy2.com/btfl/dy1.html"
    res = requests.get(url)
    soup = BeautifulSoup(res.content,"html.parser")

    tmp_list = soup.select("div.list_su ul li")
    for item in tmp_list:
      tmp_target = item.select("a.pic_link")
      tmp_name = tmp_target[0]["title"]
      tmp_url = tmp_target[0]["href"]
      
      app.logger.info(tmp_name)
      app.logger.info(tmp_url)
      break