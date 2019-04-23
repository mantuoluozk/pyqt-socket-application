# -*-coding:utf-8-*-
#服务端

import socketserver,json,time

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
        while not userIn:
            conn = self.request
            data = conn.recv(1024)
            if not data:
                continue
            dataobj = json.loads(data.decode('utf-8'))
            ret = ''
            if type(dataobj) == list:
                optype = dataobj[0]
                account = dataobj[1]
                password = dataobj[2]
                if optype == 'register':
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
                        break
                if optype == 'login':
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
                                        break
                        if ret == 'success':
                            break
                        if ret == '':
                            data = 'failed'
                            conn.sendall(data.encode('utf-8'))   
                    else:
                        data = 'failed'
                        conn.sendall(data.encode('utf-8'))

        while True:
        # 除登陆注册之外的请求的监听
            # try:
            conn = self.request
            data = conn.recv(1024)
            if not data:
                continue
            print(data)
            dataobj = data.decode('utf-8')
            if dataobj == 'quit' and userIn:
            # 有客户端退出
                for obj in connLst:
                    if obj.conObj == conn:
                        connlist.remove(obj.account)
                        obj.boolonline = 0
                        print (obj.account + "断开了连接")
                        break
                data_person = {'type': 'personList', 'data': connlist}

                for obj in connLst:
                    if obj.conObj != conn and obj.boolonline == 1:
                        obj.conObj.sendall((json.dumps(data_person)).encode('utf-8'))
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
                friendName = dataobj['friends']
                ownerName = dataobj['owner']
                ret = 'friendsFailed'
                s1 = 0
                s2 = 0
                for obj in friendsLst:
                    if ownerName == obj.owner:
                        obj.friends.append(friendName)
                        s1 = 1
                        # 更新好友列表
                        data_friends = {'type': 'friendsList', 'friends':obj.friends}
                        conn.sendall((json.dumps(data_friends)).encode('utf-8'))
                    elif friendName == obj.owner:
                        obj.friends.append(ownerName)
                        s2 = 1
                        # 更新好友列表
                        data_friends = {'type': 'friendsList', 'friends':obj.friends}
                        for obj in connLst:
                            if obj.account == friendName:
                                obj.conObj.sendall((json.dumps(data_friends)).encode('utf-8'))
                if s1 == 1 and s2 == 1:
                    print('{} friends with {}'.format(ownerName,friendName))
                    ret = 'friendsSucceed'
                conn.sendall(ret.encode('utf-8'))
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
                        person.conObj.sendall((json.dumps(data_group)).encode('utf-8'))
                else:
                    conn.sendall(('aleardyExist').encode('utf-8'))
                continue

            if dataobj["type"] == 'joinGroup' and userIn:
            #入群操作
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

            #客户端将数据发给服务器端然后由服务器转发给目标客户端
            if len(connLst) > 1:
                sendok = False
                if dataobj["type"] == 'P2M':
                # 群信息发送
                    print('group',data)
                    sendFrom = dataobj['from']
                    for obj in groupLst:
                        if obj.groupName == dataobj['to']:
                            if self.request in obj.members:# 如果发送者在群里
                                for user in obj.members:
                                    if user != self.request:
                                        user.sendall(data)
                            
                            else:
                                mess = 'notInGroup'
                                print (mess)
                                conn.snedall(mess.encode('utf-8'))
                    continue
                if dataobj["type"] == 'P2P':
                # 个人信息发送
                    sendFrom = dataobj['from']
                    sendTo = dataobj['to']
                    s1 = 0
                    for obj in friendsLst:
                        if sendFrom == obj.owner:
                            if sendTo in obj.friends:
                                s1 = 1 
                    for obj in connLst:
                        if dataobj['to'] == obj.account:
                            if s1 == 1:
                                obj.conObj.sendall(data)
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