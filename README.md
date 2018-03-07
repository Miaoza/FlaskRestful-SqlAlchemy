
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