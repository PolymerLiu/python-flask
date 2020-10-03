# 移除mariadb数据库
CentOS7默认安装mariadb数据库:
yum remove mariadb-libs.x86_64

cd /tmp
# 下载源
wget https://repo.mysql.com/mysql57-community-release-el7-8.noarch.rpm

# 安装源（为了能够搜索并下载到MySQL这个软件）
yum localinstall mysql57-community-release-el7-8.noarch.rpm

# 安装MySQL:
yum install mysql-community-server

# 启动：
sudo service mysqld start

# 查看服务状态
ps -ef |grep mysql

# 查看默认密码:
cat /var/log/mysqld.log | grep "password"


# 登录mysql
mysql -uroot -p

# 退出mysql
quit

# 重置密码，查看文章
http://blog.sina.com.cn/s/blog_a0d71a9d0102wlz3.html

set global validate_password_policy=0;
set global validate_password_length=1;

SET PASSWORD = PASSWORD('123456');



# 设置root可以远程连接
update  mysql.`user` set Host = '%' where User = 'root' and Host = 'localhost';

# 接着重启服务 
service mysqld restart


# 关闭防火墙 
service firewalld stop

# 忘记root 密码

在 /etc/my.cnf 加入 skip-grant-tables
use mysql;
update user set authentication_string=password('456789') where user='root';


 
