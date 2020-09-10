from flask_script import Command

class JobTask( Command ):
  def __init__(self):
    pass

  def run(self,params):
    print(params)