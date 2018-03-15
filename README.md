
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

#error
如果执行$ python create.py
抛出错误：sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (2003, "Can't connect to MySQL server on 'localhost' ([Errno -2] Name or service not known)")
将config.py 中 localhost 改成 127.0.0.1

#error SyntaxError: Non-ASCII character '\xe8' in file
这里提示语法错误
因为没有指定文件的编码，默认情况下不能用中文
python 文件头加入： #-*- coding: utf-8 -*-
