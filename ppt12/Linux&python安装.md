# Linux环境安装python

将python安装到/tmp文件夹
cd /tmp

1. 安装基础环境
yum install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel  mysql-devel gcc gcc-devel python-devel  

2. 下载python的安装包
wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz  

3. 解压安装包
tar -zxvf Python-3.7.3.tgz

4. 创建 /usr/local/python3目录
mkdir /usr/local/python3

6. 执行python安装包下的configure文件
Python-3.7.3/configure --prefix=/usr/local/python3

7. 进行源码编译安装
make && make install

在centos下安装python3.7.0以上版本时报错ModuleNotFoundError: No module named '_ctypes'的解决办法
yum install libffi-devel

8. linux 建立软链（类似于Windows设置环境变量）
ln -s /usr/local/python3/bin/python3 /usr/bin/python3


# 安装pip3 和 virtualenv
1. ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
2. pip3 install virtualenv
3. ln -s /usr/local/python3/bin/virtualenv /usr/bin/virtualenv

建立一个虚拟环境
cd ~
4. virtualenv -p /usr/bin/python3  imooc_env

cd imooc_env
激活python3
source bin/activate


cd ~
# linux共享目录

1.mkdir /mnt/cdrom
2.mount /dev/cdrom /mnt/cdrom

cp -R /mnt/cdrom /usr/local/src/VBoxAdditions

yum install -y gcc gcc-devel gcc-c++ gcc-c++-devel make kernel kernel-devel bzip2

/usr/local/src/VBoxAdditions/VBoxLinuxAdditions.run install


mkdir /home/www

mount -t vboxsf  order  /home/www

