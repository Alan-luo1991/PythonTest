from websocket import *
from google.protobuf.json_format import *
from google.protobuf.internal import encoder, decoder
from google.protobuf import *
import match_pb2
import numpy as np


def testsockt():
    ws = create_connection("ws://echo.websocket.org/")
    print("Sending 'Hello, World'...")
    ws.send("123, World")
    print("Sent")
    print("Receiving...")
    result = ws.recv()
    print("Received '%s'" % result)


def connect_maj():
    url_maji = 'ws://10.0.0.32:8800/BIWQFTVIPZYN6IWN83IQ5UREVGRPPVFO3SVR9ZBMLNUIKT6JJC9I3MH6J35U6PUW/600101'
    ws = create_connection(url_maji, timeout=5)
    # ws = create_connection("ws://echo.websocket.org/")
    UserInfo = UserInfoREQ()
    user_info_req_num = (17902).to_bytes(2, byteorder='big', signed=False)
    print(user_info_req_num)
    ws.send(user_info_req_num + UserInfo)
    print('>> ', user_info_req_num + UserInfo)
    MatchInfo = MatchInfoREQ()
    match_info_req_num = (22492).to_bytes(2, byteorder='big', signed=False)
    ws.send(match_info_req_num+MatchInfo)
    print(user_info_req_num+UserInfo)
    print(match_info_req_num+MatchInfo)
    result = ws.recv_data()
    print(result)



def UserInfoREQ():
    UserInfo = match_pb2.UserInfoREQ()
    # UserInfo.token = 'BIWQFTVIPZYN6IWN83IQ5UREVGRPPVFO3SVR9ZBMLNUIKT6JJC9I3MH6J35U6PUW'
    UserInfo.userId = 8040
    return UserInfo.SerializeToString()


def MatchInfoREQ():
    MatchInfo = match_pb2.MatchInfoREQ()
    MatchInfo.gameId = 600101
    return MatchInfo.SerializeToString()


def SignupREQ():
    Signup = match_pb2.SignupREQ()
    Signup.matchId = 1
    return Signup.SerializeToString()


if __name__ == '__main__':
    connect_maj()


