# 启动文件

from application import app, manager,scheduler
from flask_script import Server, Command
from www import *

# web server
manager.add_command("runserver", Server(host='localhost', use_debugger=True, use_reloader=False))


# create table
@Command
def create_all():
  from application import db
  from common.models.user import User
  db.create_all()


manager.add_command("createall", create_all)


def aps_test():
  import datetime
  print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def main():
  app.apscheduler.add_job(func=aps_test,trigger="cron",second="*/5",id="aps_test")
  scheduler.start()
  manager.run()


if __name__ == "__main__":
  # app.run(host='localhost',debug=True)
  try:
    import sys

    sys.exit(main())
  except Exception as e:
    import traceback

    traceback.print_exc()
