# -*-coding:utf-8-*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread,pyqtSignal
from ui import Ui_MainWindow
import sys
import socket
import os
import json
from time import ctime

HOST = '127.0.0.1'
PORT = 1111
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建套接字,默认为ipv4
Account = None # 全局变量


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_login.clicked.connect(self.start_login)# 登录
        self.pushButton_register.clicked.connect(self.start_register)# 注册
        self.pushButton_P_send.clicked.connect(self.read_input_p)# 读取单人聊天发送内容        
        self.pushButton_M_send.clicked.connect(self.read_input_m)# 读取群聊发送内容
        self.pushButton_creatGroup.clicked.connect(self.creat_group)# 创建群聊
        self.pushButton_joinGroup.clicked.connect(self.join_group)# 加入群聊
        self.pushButton_refresh.clicked.connect(self.list_refresh)# 刷新局域网用户
        self.pushButton_addFriends.clicked.connect(self.add_friends)# 添加好友

    def closeEvent(self, event):# 重写退出按钮，目的是退出时关掉所有线程
        """
        对MainWindow的函数closeEvent进行重构
        退出软件时结束所有进程
        :param event:
        :return:
        """
        reply = QtWidgets.QMessageBox.question(self,
                                               'tinychat',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            data = 'quit'
            sock.send(data.encode('utf-8'))
            sock.shutdown(2)
            sock.close()
            event.accept()
            os._exit(0)
        else:
            event.ignore()

    def refresh(self):# 刷新通讯录
        data = {'type': 'Refresh'}
        sock.send((json.dumps(data)).encode('utf-8'))

    def read_input_p(self):# 读取一对一聊天输入并发送
        message = self.lineEdit_P_message.text()
        target = self.lineEdit_P_target.text()
        self.lineEdit_P_message.clear()
        self.lineEdit_P_target.clear()
        data = {'type': 'P2P', 'to': target, 'message': message, 'from': Account}
        sock.send((json.dumps(data)).encode('utf-8'))
        self.textEdit_P.setTextColor(QtCore.Qt.blue)
        self.textEdit_P.setCurrentFont(QtGui.QFont("Times New Roman", 10, QtGui.QFont.Bold))# 设置字体
        self.textEdit_P.append('[%s]' % ctime())
        self.textEdit_P.setTextColor(QtCore.Qt.black)
        self.textEdit_P.setCurrentFont(QtGui.QFont("微软雅黑", 20, QtGui.QFont.Bold))# 设置字体
        self.textEdit_P.append('%s: %s' % (Account, message))

    def read_input_m(self):# 读取一对群聊输入并发送
        message = self.lineEdit_M_message.text()
        target = self.lineEdit_M_target.text()
        self.lineEdit_M_message.clear()
        self.lineEdit_M_target.clear()
        data = {'type': 'P2M', 'to': target, 'message': message, 'from': Account}
        sock.send((json.dumps(data)).encode('utf-8'))
        self.textEdit_M.setTextColor(QtCore.Qt.blue)
        self.textEdit_M.setCurrentFont(QtGui.QFont("Times New Roman", 10, QtGui.QFont.Bold))# 设置字体
        self.textEdit_M.append('[%s]' % ctime())
        self.textEdit_M.setTextColor(QtCore.Qt.black)
        self.textEdit_M.setCurrentFont(QtGui.QFont("微软雅黑", 20, QtGui.QFont.Bold))# 设置字体
        self.textEdit_M.append('%s: %s' % (Account, message))

    def start_login(self):# 登录
        global Account
        account = self.lineEdit_account.text()
        pwd = self.lineEdit_password.text()
        Account = account
        if account and pwd:
            print('账户:',account)
            print('密码',pwd)
            loginInFo = ['login', account, pwd]
            sock.send((json.dumps(loginInFo)).encode('utf-8'))
            data = sock.recv(1024).decode('utf-8')
            if data == 'success':
                print('login Succeed')
                self.scrollArea.hide()
                self.cRun(account)
            elif data == 'failed_online':
                print('failed to login,account was online')
                self.slotAbout('failed to login,account was online')
            elif data == 'failed_wrong':
                print('failed to login,password is wrong')
                self.slotAbout('failed to login,password is wrong')
            else:
                print('the account is not registered')
                self.slotAbout('the account is not registered')

    def start_register(self):# 注册
        global Account
        account = self.lineEdit_account.text()
        pwd = self.lineEdit_password.text()
        Account = account
        if account and pwd:
            print('账户:',account)
            print('密码:',pwd)
            regInFo = ['register', account, pwd]
            sock.send((json.dumps(regInFo)).encode('utf-8'))
            data = sock.recv(1024).decode('utf-8')
            if data == 'success':
                print ('register Succeed')
                self.scrollArea.hide()
                self.cRun(account)
            elif data == 'failed':
                print ('register Failed,account existed!')
                self.slotAbout('register Failed,account existed!')

    def creat_group(self):# 创建群组
        group_name = self.lineEdit_group.text()
        if group_name:
            data = {'type': 'creatGroup', 'groupName': group_name}
            sock.send((json.dumps(data)).encode('utf-8'))
    
    def join_group(self):# 加入群组
        group_name = self.lineEdit_group.text()
        if group_name:
            data = {'type': 'joinGroup', 'groupName': group_name}
            sock.send((json.dumps(data)).encode('utf-8'))

    def list_refresh(self):# 刷新局域网内用户
        data = {'type': 'personList'}
        sock.send((json.dumps(data)).encode('utf-8'))

    def add_friends(self):# 添加好友
        friends_name = self.lineEdit_addFriends.text()
        if friends_name:
            data = {'type': 'addfriends', 'owner': Account,'friends': friends_name}
            sock.send((json.dumps(data)).encode('utf-8'))

    def cRun(self, account):# 主函数
        #多线程
        self.threadIn = DealIn()
        self.threadIn.sinIn_friends.connect(self.update_friends_list)
        self.threadIn.sinIn_textm.connect(self.update_text_m)
        self.threadIn.sinIn_text.connect(self.update_text_p)
        self.threadIn.sinIn_person.connect(self.update_text_person)
        self.threadIn.sinIn_group.connect(self.update_text_group)
        self.threadIn.exception.connect(self.slotAbout)
        self.threadIn.start()

    def update_friends_list(self, inList):# 更新好友列表
        row = self.tableWidget_friends.rowCount()
        for i in range(0, row):
            self.tableWidget_friends.removeRow(0)
        for friendname in inList:
            if friendname != "":
                RowCount = self.tableWidget_friends.rowCount()
                self.tableWidget_friends.insertRow(RowCount)
                newItem1 = QtWidgets.QTableWidgetItem(friendname)
                newItem2 = QtWidgets.QTableWidgetItem('在线')
                # 设置文本对齐方式
                newItem1.setTextAlignment(QtCore.Qt.AlignCenter)
                newItem2.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_friends.setItem(RowCount,0,newItem1)
                self.tableWidget_friends.setItem(RowCount,1,newItem2)
                # 按账户名首字母排序
                self.tableWidget_friends.sortItems(0, QtCore.Qt.AscendingOrder)
                self.label_newm_3.show()

    def update_text_m(self, inString):# 更新群聊
        self.textEdit_M.setTextColor(QtCore.Qt.blue)
        self.textEdit_M.setCurrentFont(QtGui.QFont("Times New Roman", 10, QtGui.QFont.Bold))# 设置字体
        self.textEdit_M.append('[%s]' % ctime())
        self.textEdit_M.setTextColor(QtCore.Qt.black)
        self.textEdit_M.setCurrentFont(QtGui.QFont("微软雅黑", 20, QtGui.QFont.Bold))# 设置字体
        self.textEdit_M.append('%s' % (inString))
        self.label_newm_2.show()

    def update_text_p(self, inString):# 更新单人聊天
        self.textEdit_P.setTextColor(QtCore.Qt.blue)
        self.textEdit_P.setCurrentFont(QtGui.QFont("Times New Roman", 10, QtGui.QFont.Bold))# 设置字体
        self.textEdit_P.append('[%s]' % ctime())
        self.textEdit_P.setTextColor(QtCore.Qt.black)
        self.textEdit_P.setCurrentFont(QtGui.QFont("微软雅黑", 20, QtGui.QFont.Bold))# 设置字体
        self.textEdit_P.append('%s' % (inString))
        self.label_newm_1.show()

    def update_text_person(self, inList):# 更新局域网好友列表
        row = self.tableWidget_person.rowCount()
        for i in range(0, row):
            self.tableWidget_person.removeRow(0)
        for name in inList:
            if name != "":
                RowCount = self.tableWidget_person.rowCount()
                self.tableWidget_person.insertRow(RowCount)
                newItem1 = QtWidgets.QTableWidgetItem('在线')
                newItem2 = QtWidgets.QTableWidgetItem(name)
                # 设置文本对齐方式
                newItem1.setTextAlignment(QtCore.Qt.AlignCenter)
                newItem2.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_person.setItem(RowCount,0,newItem2)
                self.tableWidget_person.setItem(RowCount,1,newItem1)
                # 按账户名首字母排序
                self.tableWidget_person.sortItems(0, QtCore.Qt.AscendingOrder)

    def update_text_group(self, groupname, owner):# 更新群组列表
        RowCount = self.tableWidget_group.rowCount()
        self.tableWidget_group.insertRow(RowCount)
        newItem1 = QtWidgets.QTableWidgetItem(groupname)
        newItem2 = QtWidgets.QTableWidgetItem(owner)
        # 设置文本对齐方式
        newItem1.setTextAlignment(QtCore.Qt.AlignCenter)
        newItem2.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_group.setItem(RowCount,0,newItem1)
        self.tableWidget_group.setItem(RowCount,1,newItem2)
        # 按账户名首字母排序
        self.tableWidget_group.sortItems(0, QtCore.Qt.AscendingOrder)

    def slotAbout(self, message):  # 提示信息
        QtWidgets.QMessageBox.about(self,"About",self.tr(message))    

#接收信息的线程
class DealIn(QThread):
    # 信号
    sinIn_friends = pyqtSignal(list)
    sinIn_textm = pyqtSignal(str)
    sinIn_text = pyqtSignal(str)
    sinIn_person = pyqtSignal(list)
    sinIn_group = pyqtSignal(str, str)
    exception = pyqtSignal(str)
    def booljson(self, data):
        try:
            data = json.loads(data)
            return True
        except:
            return False
    def run(self):
        while True:
            data = sock.recv(1024).decode('utf-8')
            if data == 'friendsFailed':
                print('can not be friends')
                self.exception.emit('can not be friends')
                continue
            if data == 'friendsSucceed':
                print('add the friends')
                self.exception.emit('add the friends')
                continue
            if data == 'joinFailed':
                print('do not exist the group')
                self.exception.emit('do not exist the group')
                continue
            if data == 'aleardyIn':
                print('you are aleardy in the group')
                self.exception.emit('you are aleardy in the group')
                continue
            if data == 'joinSucceed':
                print('join the group succeed')
                self.exception.emit('join the group succeed')
                continue
            if data == 'notInGroup':
                print('you are not in the group')
                self.exception.emit('you are not in the group')
                continue
            if data == 'aleardyExist':
                print('group aleardy exist')
                self.exception.emit('group aleardy exist')
                continue
            if data == 'creatSucceed':
                print('creat the group succeed')
                self.exception.emit('creat the group succeed')
                continue
            if data == 'nofriends':
                print('your target is not your friend')
                self.exception.emit('your target is not your friend')
                continue
            if data == '-1':
                print('can not communication, not exist')
                self.exception.emit('can not communication, not exist')
                continue
            if self.booljson(data):
                data = json.loads(data)
                if data["type"] == 'P2P':
                    output = '{} ->{} :{}'.format(data['from'], data['to'], data['message'])
                    print (output)
                    self.sinIn_text.emit(output)
                    continue
                if data["type"] == 'P2M':
                    output = '{} ->group({}) :{}'.format(data['from'], data['to'], data['message'])
                    print (output)
                    self.sinIn_textm.emit(output)
                    continue
                if data["type"] == 'friendsList':
                    output = data['friends']
                    print (output)
                    self.sinIn_friends.emit(output)
                    continue
                if data["type"] == 'personList':
                    output = data['data']
                    self.sinIn_person.emit(output)
                    continue
                if data["type"] == 'groupList':
                    output1 = data['name']
                    output2 = data['owner']
                    print ('groupname:',output1)
                    print ('owner:',output2)
                    self.sinIn_group.emit(output1, output2)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()# 调用重写的方法
    MainWindow.show()
    try:
        sock.connect((HOST,PORT)) #发起请求，接收的是一个元组
        print('connected with server')
    except Exception:
        print('connected error')
        sock.close()
    sys.exit(app.exec_())    