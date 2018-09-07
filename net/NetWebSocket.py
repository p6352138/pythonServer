import NetBase
import socket

class NetWebSocket(NetBase.NetBase):
    magic_string = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
    response_tpl = "HTTP/1.1 101 Switching Protocols\r\n" \
                    "Upgrade:websocket\r\n" \
                    "Connection: Upgrade\r\n" \
                    "Sec-WebSocket-Accept: %s\r\n" \
                    "WebSocket-Location: ws://%s%s\r\n\r\n"

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