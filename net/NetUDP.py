import NetBase
import socket

class NetUdp(NetBase.NetBase):
    #并未实现还是websocket copy 过来的
    def creatSocket(self):
        s_handle = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s_handle.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            s_handle.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,NetBase.NetBase.SEND_BUFF_SIZE)
            s_handle.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,NetBase.NetBase.SEND_BUFF_SIZE)
            s_handle.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
            s_handle.bind((NetBase.NetBase.host,NetBase.NetBase.port))
            s_handle.listen(NetBase.NetBase.connectCount)
        except Exception as e:
            print(e)
            return
        else : 
            print('running ...')

        return s_handle

    