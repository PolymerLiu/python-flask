# 移除mariadb数据库
CentOS7默认安装mariadb数据库:
yum remove mariadb-libs.x86_64

# 下载源
wget https://repo.mysql.com/mysql57-community-release-el7-8.noarch.rpm

# 安装源（为了能够搜索并下载到MySQL这个软件）
yum localinstall mysql57-community-release-el7-8.noarch.rpm

# 安装MySQL:
yum install mysql-community-server

# 启动：
sudo service mysqld start

# 查看默认密码:
cat /var/log/mysqld.log | grep "password"

# 重置密码，查看文章
http://blog.sina.com.cn/s/blog_a0d71a9d0102wlz3.html


# 设置root可以远程连接
update  mysql.`user` set Host = '%' where User = 'root' and Host = 'localhost';

# 接着或者重启服务 
sudo service mysqld restart


# 关闭防火墙 
sudo service firewalld stop

# 忘记root 密码

在 /etc/my.cnf 加入 skip-grant-tables
use mysql;
update user set authentication_string=password('456789') where user='root';


 
