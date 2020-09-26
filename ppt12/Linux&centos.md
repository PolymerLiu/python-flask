# 为centos设置IP
## 查看Ip
ifconfig
ip addr
vi /etc/sysconfig/network-scripts/ifcfg-xx
vi /etc/resolv.conf   (添加 nameserver 114.114.114.114)
yum install net-tools
service network restart

然后把virtualbox的网络设置为桥接网卡，重启centos机器，centos机器即可拥有自己的IP



# linux基础知识
软件包管理器：yum 
安装软件：yum install  xxx	
卸载软件：yum remove xxx
搜索软件：yum serach xxx
清理缓存：yum clean packages
列出已安装：yum list
软件包信息 ： yum info xxx


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

