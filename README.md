# pyqt-socket-简易微信

## 使用

先运行server.py,开启服务器(python server.py) 
再运行client.py,开启客户端(python client.py), 开启多个客户端相互通信 

## 功能
* 注册，登录
* 建群，加好友
* 好友上下线通知
* 私聊，群聊
* 发送文字，图片
> 因为没有使用数据库，所以每次服务器关闭后，所有信息都会消失 

> server和client之间的数据传输是通过json传输的
## 界面
* 注册登录界面 

<img src="https://github.com/mantuoluozk/pyqt-socket-application/blob/master/src/login.png" width="300" height="500" alt="登录界面"/>

* 主界面

<img src="https://github.com/mantuoluozk/pyqt-socket-application/blob/master/src/main.png" width="300" height="500" alt="主界面"/>
