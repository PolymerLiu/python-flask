# linux 建立软链（类似于Windows设置环境变量）
ln -s /usr/local/python3/bin/uwsgi /usr/bin/uwsgi

# linux 下查看某个服务是否启动
ps -ef |grep nginx


# Linux命令
ls 查看目录下的文件
mkdir 新建文件夹
touch 新建文件
mkdir 新建文件夹
cd 进入目录
rm 删除文件和目录
cp 复制
rm 移动
pwd 显示路径

# 开启一个uwsgi实例（通过命令行）
uwsgi --http-socket 44.77.111.95:5000 --wsgi-file manager.py --callable app --processes 4 --threads 2

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