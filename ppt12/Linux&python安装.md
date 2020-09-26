# Linux环境安装

安装基础环境
1. yum install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel  mysql-devel gcc gcc-devel python-devel  

下载python的安装包
2. wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz  

解压安装包
3. tar -zxvf Python-3.7.3.tgz

创建 /usr/local/python3目录
4. mkdir /usr/local/python3

进入python的解压路径
5. cd Python-3.7.3 

执行python安装包下的configure文件
6. ./configure --prefix=/usr/local/python3

进行源码编译安装
7. make && make install

在centos下安装python3.7.0以上版本时报错ModuleNotFoundError: No module named '_ctypes'的解决办法
	yum install libffi-devel

linux 建立软链（类似于Windows设置环境变量）
8. ln -s /usr/local/python3/bin/python3 /usr/bin/python3


# 安装pip3 和 virtualenv
1. ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
2. pip3 install virtualenv
3. ln -s /usr/local/python3/bin/virtualenv /usr/bin/virtualenv
4. virtualenv -p /usr/bin/python3  vir_python3


在centos下安装python3.7.0以上版本时报错ModuleNotFoundError: No module named '_ctypes'的解决办法
	yum install libffi-devel



# linux共享目录

1.mkdir /mnt/cdrom
2.mount /dev/cdrom /mnt/cdrom

cp -R /mnt/cdrom /usr/local/src/VBoxAdditions

yum install -y gcc gcc-devel gcc-c++ gcc-c++-devel make kernel kernel-devel bzip2

/usr/local/src/VBoxAdditions/VBoxLinuxAdditions.run install


mkdir /home/www

mount -t vboxsf  mooc  /home/www

