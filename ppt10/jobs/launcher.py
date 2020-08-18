# Job统一入口文件

from flask_script import Command
import sys,argparse,traceback,importlib

# Job使用示例
# python manager.py runjob -m Test  表示执行（jobs/tasks/Test.py）文件
# python manager.py runjob -m test/index  表示执行（jobs/tasks/test/index.py）文件

class runJob( Command ):
  capture_all_args = True
  def run(self,*args,**kwargs):
    # 通过sys来获取参数
    args = sys.argv[2:]
    # 借助parser去解析参数
    parser = argparse.ArgumentParser(add_help=True)

    # job路径文件名
    parser.add_argument("-m","--name",dest="name",metavar="name",help="指定job名",required=True)
    # job动作名
    parser.add_argument("-a","--act",dest="act",metavar="act",help="job的动作",required=False)
    parser.add_argument("-p","--params",dest="params",nargs="*", metavar="params",help="业务参数",required=False)
    params = parser.parse_args(args)
    # 将params转换成字典的形式
    params_dict = params.__dict__
    if "name" not in params_dict or not params_dict["name"]:
      return self.tips()
    
    try:
      '''
      from jobs.tasks.test import JobTask
      '''
      module_name = params_dict["name"].replace("/",".")
      import_string = "jobs.tasks.%s"%(module_name)
      target = importlib.import_module(import_string)
      exit(target.JobTask().run(params_dict))
    except Exception as e:
      traceback.print_exc()


  def tips(self):
    tip_msg = '''
    请正确的调度Job
    python manager.py runjob -m Test  表示执行（jobs/tasks/Test.py）文件
    python manager.py runjob -m test/index  表示执行（jobs/tasks/test/index.py）文件
    '''
    print(tip_msg)
    return