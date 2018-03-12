
#install by requirements.txt
$ pip install -r requirements.txt

#creare or update requirements.txt
$ pip freeze > requirements.txt   

#安装virtualenv
$ pip install virtualenv

#创建一个名为env的虚拟环境
$ virtualenv env

#####
enter 虚拟环境
evn   虚拟环境名称
进入虚拟环境目录
#####
$ source env/bin/active

#退出虚拟环境
$ deactivate

#启动服务
$ python run.py

#进入MySql shell命令行
$ mysql -u root -p
password: your password

#查看已创建数据库
-> show databases;

#创建新数据库
-> create database db_name;

#删除数据库
-> drop database db_name;

#使用数据库
-> use db_name;

#退出mysql命令行
-> quit
