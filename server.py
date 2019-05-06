# -*-coding:utf-8-*-
#服务端

import socketserver,json,time
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))# 当前目录
connLst = [] # 存对象的数组
connlist = [] # 存在线用户用户名的数组
groupLst = [] # 存群对象的数组
grouplist = [] # 存群名的数组
friendsLst = [] # 好友列表对象的数组

class Connector(object):# 连接对象类
    def __init__(self,account,password,addrPort,conObj,online):
        self.account = account
        self.password = password
        self.addrPort = addrPort
        self.conObj = conObj
        self.boolonline = online    # 1代表在线，0代表不在线

class Group(object):# 群组类
    def __init__(self,groupname,groupOwner,groupOwner_name):
        self.groupName = groupname
        self.groupOwner = groupOwner
        self.groupOwner_name = groupOwner_name
        self.members=[groupOwner]

class Friends(object):# 好友列表类
    def __init__(self, owner, ownerObj):
        self.owner = owner
        self.friends = []
        self.ownerObj = ownerObj

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        print("got connection from",self.client_address)
        global connLst
        global groupLst
        userIn = False
        # 登录注册部分
        while not userIn:
            q = False# 判断是否在登录页面退出的标志位
            conn = self.request
            data = conn.recv(1024)
            if not data:
                continue
            try:
                dataobj = json.loads(data.decode('utf-8'))
            except:
                q = True
                break
            ret = ''
            if type(dataobj) == list:
                optype = dataobj[0]
                account = dataobj[1]
                password = dataobj[2]
                if optype == 'register':
                # 注册
                    exist = 0
                    for obj in connLst:
                        if obj.account == account:
                            ret = 'failed'
                            print('{} failed to register({}),account existed!'.format(account, self.client_address))
                            conn.sendall(ret.encode('utf-8'))
                            exist = 1
                            break
                    if exist == 0:
                        conObj = Connector(account,password,self.client_address,self.request,1)
                        connLst.append(conObj)
                        connlist.append(account)
                        friObj = Friends(account, self.request)
                        friendsLst.append(friObj)
                        ret = 'success'
                        userIn = True
                        print('{} has registered to system({})'.format(account,self.client_address))
                        conn.sendall(ret.encode('utf-8'))
                        # 有人上线，就把在线用户列表更新
                        data_person = {'type': 'personList', 'data': connlist}
                        for person in connLst:
                            if person.boolonline == 1:
                                person.conObj.sendall((json.dumps(data_person)).encode('utf-8'))
                        time.sleep(0.3)
                        # 更新群组
                        group_name = []
                        group_owner = []
                        for obj in groupLst:
                            group_name.append(obj.groupName)
                            group_owner.append(obj.groupOwner_name)
                        mess = {'type': 'updategroup', 'groupname': group_name, 'groupowner': group_owner}
                        conn.sendall((json.dumps(mess)).encode('utf-8'))
                        print('群组发送成功')

                        break
                if optype == 'login':
                # 登录
                    if len(connLst) > 0:
                        for obj in connLst:
                            if obj.account == account:
                                if obj.boolonline == 1:
                                    ret = 'failed_online'
                                    print('{} failed to login({}),account was online'.format(account, self.client_address))
                                    conn.sendall(ret.encode('utf-8'))
                                    break
                                elif obj.boolonline == 0:
                                    if obj.password != password:
                                        ret = 'failed_wrong'
                                        print('{} failed to login({}),password is wrong'.format(account, self.client_address))
                                        conn.sendall(ret.encode('utf-8'))
                                        break
                                    else:
                                        userIn = True
                                        ret = 'success'
                                        print('{} has logged in system({})'.format(account,self.client_address))
                                        conn.sendall(ret.encode('utf-8'))
                                        for obj in connLst:
                                            if obj.account == account:
                                                connlist.append(obj.account)
                                                obj.boolonline = 1
                                                obj.conObj = conn
                                                obj.addrPort = self.client_address
                                        # 有人上线，就把在线用户列表更新
                                        data_person = {'type': 'personList', 'data': connlist}
                                        for person in connLst:
                                            if person.boolonline == 1:
                                                person.conObj.sendall((json.dumps(data_person)).encode('utf-8'))
                                                print('在线用户发送成功')
                                        time.sleep(0.3)
                                        
                                        # 有人上线，就把他的通讯录发送出去
                                        for obj in friendsLst:
                                            if obj.owner == account:
                                                obj.ownerObj = self.request# 每次登录sock会变
                                                L = []
                                                for i in obj.friends:
                                                    if i in connlist:
                                                        L.append('1')
                                                    else:
                                                        L.append('0')
                                                print(L)
                                                data_friends = {'type': 'friendsList', 'friends':obj.friends, 'online':L}
                                                obj.ownerObj.sendall((json.dumps(data_friends)).encode('utf-8'))
                                                print(obj.friends)
                                                print(obj.ownerObj)
                                                print('通讯录发送成功')
                                        # 有人上线，就把群列表发出去


                                        # 更新通讯录，给上线用户的好友发送新的通讯录
                                        for obj in friendsLst:
                                            if obj.ownerObj == self.request:
                                                for i in obj.friends:
                                                    for s in connLst:
                                                        if s.account == i and s.boolonline == 1:
                                                            data_friends = {'type': 'friendalter', 'name':account, 'online':'1'}
                                                            s.conObj.sendall((json.dumps(data_friends)).encode('utf-8'))
                                                            print('通讯录更新成功')
                                        
                                        # 更新群组
                                        group_name = []
                                        group_owner = []
                                        for obj in groupLst:
                                            group_name.append(obj.groupName)
                                            group_owner.append(obj.groupOwner_name)
                                        mess = {'type': 'updategroup', 'groupname': group_name, 'groupowner': group_owner}
                                        conn.send((json.dumps(mess)).encode('utf-8'))
                                        print('群组发送成功')

                        if ret == 'success':
                            break
                        if ret == '':
                            data = 'failed'
                            conn.sendall(data.encode('utf-8'))   
                    else:
                        data = 'failed'
                        conn.sendall(data.encode('utf-8'))

        # 除登陆注册之外的请求的监听
        while True and q == False:
            conn = self.request
            data = conn.recv(1024)
            if not data:
                continue
            print(data)
            dataobj = data.decode('utf-8')
            if dataobj == 'quit' and userIn:
            # 有客户端退出
                quitaccount = ''
                for obj in connLst:
                    if obj.conObj == conn:
                        connlist.remove(obj.account)
                        obj.boolonline = 0
                        print (obj.account + "断开了连接")
                        quitaccount = obj.account
                        break

                # 更新在线用户
                data_person = {'type': 'personList', 'data': connlist}
                for obj in connLst:
                    if obj.conObj != conn and obj.boolonline == 1:
                        obj.conObj.sendall((json.dumps(data_person)).encode('utf-8'))
                
                time.sleep(0.2)

                # 更新通讯录，给退出用户的好友发送新的通讯录
                for obj in friendsLst:
                    if obj.ownerObj == self.request:
                        L = []
                        for i in obj.friends:
                            for s in connLst:
                                if s.account == i and s.boolonline == 1:
                                    data_friends = {'type': 'friendalter', 'name':quitaccount, 'online':'0'}
                                    s.conObj.sendall((json.dumps(data_friends)).encode('utf-8'))

                conn.shutdown(2)
                conn.close()
                break

            dataobj = json.loads(dataobj)
            print(dataobj)

            if dataobj["type"] == 'personList' and userIn:
            # 刷新在线用户列表
                data_person = {'type': 'personList', 'data': connlist}
                for person in connLst:
                    if person.boolonline == 1:
                        person.conObj.sendall((json.dumps(data_person)).encode('utf-8'))
                continue

            if dataobj["type"] == 'addfriends' and userIn:
            # 添加好友
                sendFrom = dataobj['owner']
                sendTo = dataobj['friends']
                s0 = 0
                for friend in friendsLst:
                    if conn == friend.ownerObj:
                        if sendTo in friend.friends:
                            mess = 'aleardybefriends'
                            conn.sendall(mess.encode('utf-8'))
                            print('好友已经存在')
                            s0 = 1
                            break
                if s0 == 0:
                    s = 0
                    for obj in connLst:
                        if sendTo == obj.account:
                            s = 1
                            if obj.conObj == conn:
                                mess = 'noself'
                                conn.sendall(mess.encode('utf-8'))
                                break
                            if obj.boolonline == 1:
                                obj.conObj.sendall(data)
                            else:
                                mess = 'outline'
                                conn.sendall(mess.encode('utf-8'))

                    if s == 0:
                        mess = 'noexist'
                        conn.sendall(mess.encode('utf-8'))
                    continue

            if dataobj["type"] == 'addfriendVer' and userIn:
            # 好友验证消息接受并转发
                if dataobj["answer"] == 'yes':
                    print('同意加好友')
                    friendName = dataobj['to']
                    ownerName = dataobj['from']
                    ret = 'friendsFailed'
                    s1 = 0
                    s2 = 0
                    for obj in friendsLst:
                        if ownerName == obj.owner:
                            obj.friends.append(friendName)
                            s1 = 1
                            # 更新好友列表
                            L = []
                            for i in obj.friends:
                                if i in connlist:
                                    L.append('1')
                                else:
                                    L.append('0')
                            print(L)
                            data_friends = {'type': 'friendsList', 'friends':obj.friends, 'online':L}
                            conn.sendall((json.dumps(data_friends)).encode('utf-8'))
                            continue
                        if friendName == obj.owner:
                            obj.friends.append(ownerName)
                            s2 = 1
                            # 更新好友列表
                            L = []
                            for i in obj.friends:
                                if i in connlist:
                                    L.append('1')
                                else:
                                    L.append('0')
                            print(L)
                            data_friends = {'type': 'friendsList', 'friends':obj.friends, 'online':L}
                            for obj in connLst:
                                if obj.account == friendName:
                                    obj.conObj.sendall((json.dumps(data_friends)).encode('utf-8'))
                                    ret = 'friendsSucceed'
                                    obj.conObj.sendall(ret.encode('utf-8'))
                    if s1 == 1 and s2 == 1:
                        print('{} friends with {}'.format(ownerName,friendName))
                        # ret = 'friendsSucceed'
                    # conn.sendall(ret.encode('utf-8'))
                    continue
                else:
                    print('拒绝加好友')
                    for obj in connLst:
                        if obj.account == dataobj["to"]:
                            data_answer = 'friendnoagree'
                            obj.conObj.sendall(data_answer.encode('utf-8'))
                            break
                    continue

            if dataobj["type"] == 'creatGroup' and userIn:
            # 创建群组
                groupName = dataobj['groupName']
                if groupName not in grouplist:
                    for person in connLst:
                        if person.conObj == self.request:    
                            groupOwner_name = person.account
                    groupObj = Group(groupName,self.request,groupOwner_name)
                    groupLst.append(groupObj)
                    grouplist.append(groupName)
                    conn.sendall('creatSucceed'.encode('utf-8'))
                    print('%s created'%groupName)
                    # 有新的群，就把群列表更新
                    data_group = {'type': 'groupList', 'name': groupName, 'owner': groupOwner_name}
                    for person in connLst:
                        if person.boolonline == 1:
                            person.conObj.sendall((json.dumps(data_group)).encode('utf-8'))
                else:
                    conn.sendall(('aleardyExist').encode('utf-8'))
                continue

            if dataobj["type"] == 'joinGroup' and userIn:
            # 入群操作
                print(grouplist)
                groupName = dataobj['groupName']
                ret = 'joinFailed'
                for group in groupLst:
                    if groupName == group.groupName:
                        if self.request not in group.members:
                            group.members.append(self.request)
                            print('{} added into {}'.format(self.client_address,groupName))
                            ret = 'joinSucceed'
                            break
                        else:
                            ret = 'aleardyIn'
                conn.sendall(ret.encode('utf-8'))
                continue

            # 客户端将数据发给服务器端然后由服务器转发给目标客户端
            if len(connLst) > 1:
                sendok = False
                if dataobj["type"] == 'P2M':
                # 群信息发送
                    if 'filename' in dataobj.keys() :# 图片
                        sendFrom = dataobj['from']
                        sendTo = dataobj['to']
                        filename = dataobj['filename']
                        filesize = dataobj['filesize']
                        path = os.path.join(BASE_DIR, filename)
                        filesize = int(filesize)
                        f = open(path,'ab')
                        has_receive = 0
                        while has_receive != filesize:
                            data1 = conn.recv(1024)
                            f.write(data1)
                            has_receive += len(data1)
                        print('服务器图片接收完成')
                        f.close()
                        # 转发图片
                        if dataobj['to'] in grouplist:
                            for obj in groupLst:
                                if obj.groupName == sendTo:
                                    if self.request in obj.members:# 如果发送者在群里
                                        for user in obj.members:
                                            if user in connlist:
                                                if user != self.request:
                                                    # user.sendall(data)
                                                    try:
                                                        filesize = os.stat(path).st_size
                                                        file_info = {'type': 'P2M', 'to':sendTo, 'filename': filename, 'filesize':filesize, 'from':sendFrom}
                                                        user.send((json.dumps(file_info)).encode('utf-8'))
                                                        f = open(path,'rb')
                                                        has_sent = 0
                                                        while has_sent != filesize:
                                                            data = f.read(1024)
                                                            user.sendall(data)
                                                            has_sent += len(data)
                                                        f.close()
                                                    except:
                                                        print('有人不在线')
                                        print('转发成功')
                                    
                                    else:
                                        mess = 'notInGroup'
                                        print (mess)
                                        conn.sendall(mess.encode('utf-8'))
                        else:
                            mess = 'groupnoexist'
                            conn.sendall(mess.encode('utf-8'))
                        continue
                    else:
                        print('group',data)
                        sendFrom = dataobj['from']
                        if dataobj['to'] in grouplist:
                            for obj in groupLst:
                                if obj.groupName == dataobj['to']:
                                    if self.request in obj.members:# 如果发送者在群里
                                        for user in obj.members:
                                                if user != self.request:
                                                    try:
                                                        user.sendall(data)
                                                        print('发送成功')
                                                    except:
                                                        print('群里有人不在线')
                                    else:
                                        mess = 'notInGroup'
                                        print (mess)
                                        conn.sendall(mess.encode('utf-8'))
                        else:
                            mess = 'groupnoexist'
                            conn.sendall(mess.encode('utf-8'))
                        continue
                if dataobj["type"] == 'P2P':
                # 个人信息发送
                    if 'filename' in dataobj.keys() :# 图片
                        sendFrom = dataobj['from']
                        sendTo = dataobj['to']
                        filename = dataobj['filename']
                        filesize = dataobj['filesize']
                        path = os.path.join(BASE_DIR, filename)
                        filesize = int(filesize)
                        f = open(path,'ab')
                        has_receive = 0
                        while has_receive != filesize:
                            data1 = conn.recv(1024)
                            f.write(data1)
                            has_receive += len(data1)
                        print('服务器图片接收完成')
                        f.close()
                        # 转发图片
                        s1 = 0
                        for obj in friendsLst:
                            if sendFrom == obj.owner:
                                if sendTo in obj.friends:
                                    s1 = 1 
                        for obj in connLst:
                            if dataobj['to'] == obj.account:
                                if obj.boolonline == 1:
                                    if s1 == 1:
                                        # obj.conObj.sendall(data)
                                        filesize = os.stat(path).st_size
                                        file_info = {'type': 'P2P', 'to':sendTo, 'filename': filename, 'filesize':filesize, 'from':sendFrom}
                                        obj.conObj.send((json.dumps(file_info)).encode('utf-8'))
                                        f = open(path,'rb')
                                        has_sent = 0
                                        while has_sent != filesize:
                                            data = f.read(1024)
                                            obj.conObj.sendall(data)
                                            has_sent += len(data)
                                        print('转发成功')
                                        f.close()
                                    else:
                                        mess = 'outline'
                                        conn.sendall(mess.encode('utf-8'))
                        if s1 == 0:
                            mess = 'nofriends'
                            print(mess)
                            conn.sendall(mess.encode('utf-8'))
                        continue

                    else:# 消息
                        sendFrom = dataobj['from']
                        sendTo = dataobj['to']
                        s1 = 0
                        for obj in friendsLst:
                            if sendFrom == obj.owner:
                                if sendTo in obj.friends:
                                    s1 = 1 
                        for obj in connLst:
                            if dataobj['to'] == obj.account:
                                if obj.boolonline == 1:
                                    if s1 == 1:
                                        obj.conObj.sendall(data)
                                else:
                                    mess = 'outline'
                                    conn.sendall(mess.encode('utf-8'))
                        if s1 == 0:
                            mess = 'nofriends'
                            print(mess)
                            conn.sendall(mess.encode('utf-8'))
            else:
                conn.sendall('-1'.encode('utf-8'))
                continue
                     

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',1111),MyServer)
    print('waiting for connection...')
    server.serve_forever()
