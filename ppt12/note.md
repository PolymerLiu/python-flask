# 开启一个uwsgi实例（通过命令行）
uwsgi --http-socket 44.77.111.95:5000 --wsgi-file manager.py --callable app 

# 开启一个uwsgi实例（通过加载配置文件）
uwsgi --ini uwsgi.ini


# 停止uwsgi实例
uwsgi --stop /tmp/logs/movie.pid

# 重载uwsgi实例

uwsgi --reload /tmp/logs/movie.pid

# 杀死所有uwsgi进程
killall -s INT uwsgi

# 安装killall命令
yum install psmisc -y 