# -*- coding: utf-8 -*-

# MainWindow implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import ctypes

from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QAbstractItemView

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")# 让Windows知道这是一个单独的窗口
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(392, 594)
        MainWindow.setFixedSize(392, 594)
        self.setWindowOpacity(0.9) # 设置窗口透明度
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('图标')
        self.setWindowIcon(QtGui.QIcon('src\交流.png')) 
# 上方三个按钮
        self.pushButton_search = QtWidgets.QPushButton(MainWindow)
        self.pushButton_search.setGeometry(QtCore.QRect(270, 0, 41, 41))
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_search.setStyleSheet('''QPushButton{background:transparent;border-image: url(src/放大镜.png);}QPushButton:hover{background:grey;}''')
        self.pushButton_insert = QtWidgets.QPushButton(MainWindow)
        self.pushButton_insert.setGeometry(QtCore.QRect(310, 0, 39, 39))
        self.pushButton_insert.setObjectName("pushButton_insert")
        self.pushButton_insert.setStyleSheet('''QPushButton{background:transparent;border-image: url(src/群聊.png);}QPushButton:hover{background:grey;}''')
        self.pushButton_others = QtWidgets.QPushButton(MainWindow)
        self.pushButton_others.setGeometry(QtCore.QRect(350, 0, 41, 41))
        self.pushButton_others.setObjectName("pushButton_others")
        self.pushButton_others.setStyleSheet('''QPushButton{background:transparent;border-image: url(src/通讯.png);}QPushButton:hover{background:grey;}''')
# 三个主界面
        self.pushButton_chat = QtWidgets.QPushButton(MainWindow)
        self.pushButton_chat.setGeometry(QtCore.QRect(0, 40, 131, 31))
        self.pushButton_chat.setObjectName("pushButton_chat")
        self.pushButton_chat.setCheckable(True)
        self.pushButton_chat.setAutoExclusive(True)
        self.pushButton_chat.setStyleSheet('''QPushButton{background: #3C79F2; border-color: #11505C; font-weight: bold; font-family:"Microsoft YaHei"; }''')
        self.pushButton_mchat = QtWidgets.QPushButton(MainWindow)
        self.pushButton_mchat.setGeometry(QtCore.QRect(130, 40, 131, 31))
        self.pushButton_mchat.setObjectName("pushButton_mchat")
        self.pushButton_mchat.setCheckable(True)
        self.pushButton_mchat.setAutoExclusive(True)
        self.pushButton_mchat.setStyleSheet('''QPushButton{background: #3C79F2; border-color: #11505C; font-weight: bold; font-family:"Microsoft YaHei"; }''')
        self.pushButton_list = QtWidgets.QPushButton(MainWindow)
        self.pushButton_list.setGeometry(QtCore.QRect(260, 40, 131, 31))
        self.pushButton_list.setObjectName("pushButton_list")
        self.pushButton_list.setCheckable(True)
        self.pushButton_list.setAutoExclusive(True)
        self.pushButton_list.setStyleSheet('''QPushButton{background: #3C79F2; border-color: #11505C; font-weight: bold; font-family:"Microsoft YaHei"; }''')
        self.app_name = QtWidgets.QLabel(MainWindow)
        self.app_name.setGeometry(QtCore.QRect(0, 0, 250, 41))
        self.app_name.setObjectName("app_name")
        self.stackedWidget = QtWidgets.QStackedWidget(MainWindow)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 70, 391, 521))
        self.stackedWidget.setObjectName("stackedWidget")
# 信息红点
        self.label_newm_1 = QtWidgets.QLabel(MainWindow)
        self.label_newm_1.setGeometry(QtCore.QRect(115, 40, 14, 14))
        self.label_newm_1.setText("")
        self.label_newm_1.setObjectName("label_newm_1")
        self.label_newm_1.setStyleSheet('''QLabel{background:red;border-radius:5px;}''')
        self.label_newm_1.raise_()
        self.label_newm_1.hide()
        self.label_newm_2 = QtWidgets.QLabel(MainWindow)
        self.label_newm_2.setGeometry(QtCore.QRect(245, 40, 14, 14))
        self.label_newm_2.setText("")
        self.label_newm_2.setObjectName("label_newm_2")
        self.label_newm_2.setStyleSheet('''QLabel{background:red;border-radius:5px;}''')
        self.label_newm_2.raise_()
        self.label_newm_2.hide()
        self.label_newm_3 = QtWidgets.QLabel(MainWindow)
        self.label_newm_3.setGeometry(QtCore.QRect(375, 40, 14, 14))
        self.label_newm_3.setText("")
        self.label_newm_3.setObjectName("label_newm_3")
        self.label_newm_3.setStyleSheet('''QLabel{background:red;border-radius:5px;}''')
        self.label_newm_3.raise_()
        self.label_newm_3.hide()

# 第一页
        self.page_chat = QtWidgets.QWidget()
        self.page_chat.setObjectName("page_chat")
        self.lineEdit_P_message = QtWidgets.QLineEdit(self.page_chat)
        self.lineEdit_P_message.setGeometry(QtCore.QRect(0, 480, 191, 41))
        self.lineEdit_P_message.setObjectName("lineEdit_P_message")
        self.lineEdit_P_message.setStyleSheet(
        '''QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
        }''') 
        self.lineEdit_P_message.setFont(QtGui.QFont("微软雅黑", 10, QtGui.QFont.Bold))# 设置字体  
        self.lineEdit_P_message.setPlaceholderText("发送的内容")     
        self.lineEdit_P_target = QtWidgets.QLineEdit(self.page_chat)
        self.lineEdit_P_target.setGeometry(QtCore.QRect(190, 480, 121, 41))
        self.lineEdit_P_target.setObjectName("lineEdit_P_target")
        self.lineEdit_P_target.setStyleSheet(
        '''QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
        }''') 
        self.lineEdit_P_target.setFont(QtGui.QFont("微软雅黑", 10, QtGui.QFont.Bold))# 设置字体
        self.lineEdit_P_target.setPlaceholderText("发送的对象")
        self.lineEdit_P_target.raise_()
        self.pushButton_P_send = QtWidgets.QPushButton(self.page_chat)
        self.pushButton_P_send.setGeometry(QtCore.QRect(310, 480, 39, 39))
        self.pushButton_P_send.setObjectName("pushButton_P_send")
        self.pushButton_P_send.setStyleSheet('''QPushButton{background:transparent;border-image: url(src/纸飞机.png);}QPushButton:hover{background:grey;}''')
        self.pushButton_P_imgandfile = QtWidgets.QPushButton(self.page_chat)
        self.pushButton_P_imgandfile.setGeometry(QtCore.QRect(350, 480, 39, 39))
        self.pushButton_P_imgandfile.setObjectName("pushButton_P_imgandfile")
        self.pushButton_P_imgandfile.setStyleSheet('''QPushButton{background:transparent;border-image: url(src/图片.png);}QPushButton:hover{background:grey;}''')
        self.textEdit_P = QtWidgets.QTextEdit(self.page_chat)
        self.textEdit_P.setGeometry(QtCore.QRect(0, 0, 391, 481))
        self.textEdit_P.setObjectName("textEdit_P")
        self.textEdit_P.setFocusPolicy(QtCore.Qt.NoFocus)# 禁止编辑
        self.textEdit_P.setFont(QtGui.QFont("微软雅黑", 20, QtGui.QFont.Bold))# 设置字体
        self.stackedWidget.addWidget(self.page_chat)
# 上方添加好友界面
        self.stackedWidget_2 = QtWidgets.QStackedWidget(MainWindow)
        self.stackedWidget_2.setGeometry(QtCore.QRect(60, 100, 281, 411))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.stackedWidget_2.setStyleSheet('''QStackedWidget{background:#3C79F2; border:2px solid blue;border-radius:8px;}''')
        self.page_addFriends = QtWidgets.QWidget()
        self.page_addFriends.setObjectName("page_addFriends")
        self.widget = QtWidgets.QWidget(self.page_addFriends)
        self.widget.setGeometry(QtCore.QRect(0, 0, 281, 411))
        self.widget.setObjectName("widget")
        self.lineEdit_addFriends = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_addFriends.setGeometry(QtCore.QRect(30, 41, 121, 20))
        self.lineEdit_addFriends.setObjectName("lineEdit_addFriends")
        self.lineEdit_addFriends.setPlaceholderText("要添加的好友名")    
        self.pushButton_addFriends = QtWidgets.QPushButton(self.widget)
        self.pushButton_addFriends.setGeometry(QtCore.QRect(160, 40, 41, 21))
        self.pushButton_addFriends.setObjectName("pushButton_addFriends")
        self.pushButton_addFriends.setStyleSheet('''QPushButton{background:#6DDF6D;}QPushButton:hover{background:green;}''')
        self.pushButton_refresh = QtWidgets.QPushButton(self.widget)
        self.pushButton_refresh.setGeometry(QtCore.QRect(210, 40, 41, 21))
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.pushButton_refresh.setStyleSheet('''QPushButton{background:#6DDF6D;}QPushButton:hover{background:green;}''')
        self.tableWidget_person = QtWidgets.QTableWidget(self.widget)
        self.tableWidget_person.setGeometry(QtCore.QRect(0, 70, 281, 341))
        self.tableWidget_person.setObjectName("tableWidget_person")
        self.tableWidget_person.setColumnCount(2)
        self.tableWidget_person.setHorizontalHeaderLabels(['账号','状态'])
        # 表头自适应
        self.tableWidget_person.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # 表禁止编辑
        self.tableWidget_person.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.tableWidget_person.verticalHeader().setDisabled(True)
        self.tableWidget_person.verticalHeader().setVisible(False)     #把标号取消
        self.tableWidget_person.setSelectionBehavior(QAbstractItemView.SelectRows)    #选择时每次选择一行
        self.tableWidget_person.doubleClicked.connect(self.choose_one_person)


        self.label_addFriends = QtWidgets.QLabel(self.widget)
        self.label_addFriends.setGeometry(QtCore.QRect(30, 20, 81, 21))
        self.label_addFriends.setObjectName("label_addFriends")
        self.pushButton_addFriends_q = QtWidgets.QPushButton(self.widget)
        self.pushButton_addFriends_q.setGeometry(QtCore.QRect(260, 0, 51, 23))
        self.pushButton_addFriends_q.setFixedSize(15,15) # 设置关闭按钮的大小
        self.pushButton_addFriends_q.setObjectName("pushButton_addFriends_q")
        self.pushButton_addFriends_q.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.stackedWidget_2.addWidget(self.page_addFriends)
# 上方添加群组界面
        self.page_addGroup = QtWidgets.QWidget()
        self.page_addGroup.setObjectName("page_addGroup")
        self.widget_GroupChat = QtWidgets.QWidget(self.page_addGroup)
        self.widget_GroupChat.setGeometry(QtCore.QRect(0, 0, 281, 411))
        self.widget_GroupChat.setObjectName("widget_GroupChat")
        self.pushButton_joinGroup = QtWidgets.QPushButton(self.widget_GroupChat)
        self.pushButton_joinGroup.setGeometry(QtCore.QRect(170, 20, 61, 21))
        self.pushButton_joinGroup.setObjectName("pushButton_joinGroup")
        self.pushButton_joinGroup.setStyleSheet('''QPushButton{background:#6DDF6D;}QPushButton:hover{background:green;}''')
        #self.pushButton_joinGroup.setStyleSheet('''QPushButton{background:transparent;border-image: url(src/图片.png);}QPushButton:hover{background:grey;}''')


        self.pushButton_creatGroup = QtWidgets.QPushButton(self.widget_GroupChat)
        self.pushButton_creatGroup.setGeometry(QtCore.QRect(170, 50, 61, 21))
        self.pushButton_creatGroup.setObjectName("pushButton_creatGroup")
        self.pushButton_creatGroup.setStyleSheet('''QPushButton{background:#6DDF6D;}QPushButton:hover{background:green;}''')
        self.lineEdit_group = QtWidgets.QLineEdit(self.widget_GroupChat)
        self.lineEdit_group.setGeometry(QtCore.QRect(20, 30, 131, 31))
        self.lineEdit_group.setObjectName("lineEdit_group")
        self.lineEdit_group.setPlaceholderText("创建/加入的群名") 
        self.label_group = QtWidgets.QLabel(self.widget_GroupChat)
        self.label_group.setGeometry(QtCore.QRect(20, 10, 51, 21))
        self.label_group.setObjectName("label_group")
        self.pushButton_addGroup_q = QtWidgets.QPushButton(self.widget_GroupChat)
        self.pushButton_addGroup_q.setGeometry(QtCore.QRect(260, 0, 41, 23))
        self.pushButton_addGroup_q.setObjectName("pushButton_addGroup_q")
        self.pushButton_addGroup_q.setFixedSize(15,15) # 设置关闭按钮的大小
        self.pushButton_addGroup_q.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')

        self.tableWidget_group = QtWidgets.QTableWidget(self.widget_GroupChat)
        self.tableWidget_group.setGeometry(QtCore.QRect(0, 80, 281, 331))
        self.tableWidget_group.setObjectName("tableWidget_group")
        self.tableWidget_group.setColumnCount(2)
        self.tableWidget_group.setHorizontalHeaderLabels(['群名','群主'])
        # 表头自适应
        self.tableWidget_group.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # 表禁止编辑
        self.tableWidget_group.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.stackedWidget_2.addWidget(self.page_addGroup)
        self.stackedWidget_2.raise_()

        self.tableWidget_group.verticalHeader().setDisabled(True)
        self.tableWidget_group.verticalHeader().setVisible(False)     #把标号取消
        self.tableWidget_group.setSelectionBehavior(QAbstractItemView.SelectRows)    #选择时每次选择一行
        self.tableWidget_group.doubleClicked.connect(self.choose_one_group)
        
# 第二页
        self.page_mchat = QtWidgets.QWidget()
        self.page_mchat.setObjectName("page_mchat")
        self.lineEdit_M_message = QtWidgets.QLineEdit(self.page_mchat)
        self.lineEdit_M_message.setGeometry(QtCore.QRect(0, 480, 191, 41))
        self.lineEdit_M_message.setObjectName("lineEdit_M_message")
        self.lineEdit_M_message.setStyleSheet(
        '''QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
        }''')
        self.lineEdit_M_message.setFont(QtGui.QFont("微软雅黑", 10, QtGui.QFont.Bold))# 设置字体
        self.lineEdit_M_message.setPlaceholderText("发送的内容")    
        self.lineEdit_M_target = QtWidgets.QLineEdit(self.page_mchat)
        self.lineEdit_M_target.setGeometry(QtCore.QRect(190, 480, 121, 41))
        self.lineEdit_M_target.setObjectName("lineEdit_M_target")
        self.lineEdit_M_target.setStyleSheet(
        '''QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
        }''')  
        self.lineEdit_M_target.setFont(QtGui.QFont("微软雅黑", 10, QtGui.QFont.Bold))# 设置字体
        self.lineEdit_M_target.setPlaceholderText("发送给的群组")
        self.lineEdit_M_target.raise_()             #lpk  提升边框
        self.pushButton_M_send = QtWidgets.QPushButton(self.page_mchat)
        self.pushButton_M_send.setGeometry(QtCore.QRect(310, 480, 41, 41))
        self.pushButton_M_send.setObjectName("pushButton_M_send")
        self.pushButton_M_send.setStyleSheet('''QPushButton{background:transparent;border-image: url(src/纸飞机.png);}QPushButton:hover{background:grey;}''')
        self.pushButton_M_imgandfile = QtWidgets.QPushButton(self.page_mchat)
        self.pushButton_M_imgandfile.setGeometry(QtCore.QRect(350, 480, 41, 41))
        self.pushButton_M_imgandfile.setObjectName("pushButton_M_imgandfile")
        self.pushButton_M_imgandfile.setStyleSheet('''QPushButton{background:transparent;border-image: url(src/图片.png);}QPushButton:hover{background:grey;}''')
        self.textEdit_M = QtWidgets.QTextEdit(self.page_mchat)
        self.textEdit_M.setGeometry(QtCore.QRect(0, 0, 391, 481))
        self.textEdit_M.setObjectName("textEdit_M")
        self.textEdit_M.setFocusPolicy(QtCore.Qt.NoFocus)# 禁止编辑
        self.textEdit_M.setFont(QtGui.QFont("微软雅黑", 20, QtGui.QFont.Bold))# 设置字体  
        self.stackedWidget.addWidget(self.page_mchat)
# 第三页
        self.page_list = QtWidgets.QWidget()
        self.page_list.setObjectName("page_list")
        self.tableWidget_friends = QtWidgets.QTableWidget(self.page_list)
        self.tableWidget_friends.setGeometry(QtCore.QRect(0, 0, 391, 521))
        self.tableWidget_friends.setObjectName("tableWidget_friends")
        self.tableWidget_friends.setColumnCount(2)
        self.tableWidget_friends.setHorizontalHeaderLabels(['昵称','状态'])
        # 表头自适应
        self.tableWidget_friends.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # 表禁止编辑
        self.tableWidget_friends.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.tableWidget_friends.verticalHeader().setDisabled(True)
        self.tableWidget_friends.verticalHeader().setVisible(False)     #把标号取消
        self.tableWidget_friends.setSelectionBehavior(QAbstractItemView.SelectRows)    #选择时每次选择一行
        self.tableWidget_friends.doubleClicked.connect(self.choose_one)

        self.stackedWidget.addWidget(self.page_list)
# 登录注册界面
        self.scrollArea = QtWidgets.QScrollArea(MainWindow)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 391, 591))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 389, 589))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.lineEdit_account = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_account.setGeometry(QtCore.QRect(120, 350, 190, 20))
        self.lineEdit_account.setObjectName("lineEdit_account")
        self.lineEdit_account.setPlaceholderText("输入你的账号")
        self.lineEdit_account.setStyleSheet(
        '''QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
        }''')    
        self.label_account = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_account.setGeometry(QtCore.QRect(90, 350, 31, 21))
        self.label_account.setObjectName("label_account")

        self.gif = QMovie('src\GIF.gif')
        self.label_picture = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_picture.setGeometry(QtCore.QRect(0, 0, 391, 301))
        self.label_picture.setObjectName("label_account")
        self.label_picture.setMovie(self.gif)
        self.gif.start()

        self.lineEdit_password = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_password.setGeometry(QtCore.QRect(120, 390, 190, 20))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setPlaceholderText("输入你的密码")
        self.lineEdit_password.setStyleSheet(
        '''QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
        }''')    
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_password = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_password.setGeometry(QtCore.QRect(90, 390, 31, 21))
        self.label_password.setObjectName("label_password")

        self.pushButton_login = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_login.setGeometry(QtCore.QRect(130, 430, 51, 23))
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_login.setStyleSheet('''QPushButton{background:#6DDF6D;}QPushButton:hover{background:green;}''')
        self.pushButton_register = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_register.setGeometry(QtCore.QRect(220, 430, 51, 23))
        self.pushButton_register.setObjectName("pushButton_register")
        self.pushButton_register.setStyleSheet('''QPushButton{background:#6DDF6D;}QPushButton:hover{background:green;}''')
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        # 按钮事件
        self.stackedWidget_2.hide()# 默认关闭

        self.pushButton_addFriends_q.clicked.connect(self.stackedWidget_2.hide)
        self.pushButton_addGroup_q.clicked.connect(self.stackedWidget_2.hide)
        self.pushButton_search.clicked.connect(self.on_pushButton_search_clicked)    
        self.pushButton_insert.clicked.connect(self.on_pushButton_insert_clicked)

        self.pushButton_chat.clicked.connect(self.on_pushButtonchat_clicked)
        self.pushButton_mchat.clicked.connect(self.on_pushButtonmchat_clicked)
        self.pushButton_list.clicked.connect(self.on_pushButtonlist_clicked)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # 切换翻页
    def on_pushButton_insert_clicked(self):
        self.stackedWidget_2.show()
        self.stackedWidget_2.setCurrentIndex(1)
    def on_pushButton_search_clicked(self):
        self.stackedWidget_2.show()
        self.stackedWidget_2.setCurrentIndex(0)

    def on_pushButtonchat_clicked(self):
        self.stackedWidget.setCurrentIndex(0)
        self.label_newm_1.hide()
    def on_pushButtonmchat_clicked(self):
        self.stackedWidget.setCurrentIndex(1)
        self.label_newm_2.hide()
    def on_pushButtonlist_clicked(self):
        self.stackedWidget.setCurrentIndex(2)
        self.label_newm_3.hide()

    def choose_one(self):
        self.stackedWidget.setCurrentIndex(0)
        self.lineEdit_P_target.setText(self.tableWidget_friends.item(self.tableWidget_friends.currentRow(),0).text())

    def choose_one_person(self):
        self.lineEdit_addFriends.setText(self.tableWidget_person.item(self.tableWidget_person.currentRow(),0).text())

    def choose_one_group(self):
        self.lineEdit_group.setText(self.tableWidget_group.item(self.tableWidget_group.currentRow(),0).text())
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TinyChat"))
        #self.pushButton_search.setText(_translate("MainWindow", "搜索"))
        #self.pushButton_insert.setText(_translate("MainWindow", "添加"))
        #self.pushButton_others.setText(_translate("MainWindow", "其他"))
        self.pushButton_chat.setText(_translate("MainWindow", "聊天"))
        self.pushButton_mchat.setText(_translate("MainWindow", "群聊"))
        self.pushButton_list.setText(_translate("MainWindow", "通讯录"))
        # self.app_name.setText(_translate("MainWindow", "love you three thousands"))
        #self.pushButton_P_send.setText(_translate("MainWindow", "发送"))
        #self.pushButton_P_imgandfile.setText(_translate("MainWindow", "+"))
        #slef.pushButton_M_send.setText(_translate("MainWindow", "发送"))
        #self.pushButton_M_imgandfile.setText(_translate("MainWindow", "+"))
        self.label_account.setText(_translate("MainWindow", "账号"))
        self.label_password.setText(_translate("MainWindow", "密码"))
        self.pushButton_login.setText(_translate("MainWindow", "登录"))
        self.pushButton_register.setText(_translate("MainWindow", "注册"))
        self.pushButton_addFriends.setText(_translate("MainWindow","添加"))
        # self.pushButton_addFriends_q.setText(_translate("MainWindow","关闭"))
        self.label_addFriends.setText(_translate("MainWindow","请输入用户名"))
        self.pushButton_creatGroup.setText(_translate("MainWindow","创建群聊"))
        self.pushButton_joinGroup.setText(_translate("MainWindow","加入群聊"))
        # self.pushButton_addGroup_q.setText(_translate("MainWindow","关闭"))
        self.label_group.setText(_translate("MainWindow","群聊名称"))
        self.pushButton_refresh.setText(_translate("MainWindow", "刷新"))
