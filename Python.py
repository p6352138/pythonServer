import socket
import base64
import hashlib
import utility.websocketUtility.wsUtility

host = '127.0.0.1'
port = 50007
SEND_BUFF_SIZE = 4096
REV_BUFF_SIZE = 4096
magic_string = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
response_tpl = "HTTP/1.1 101 Switching Protocols\r\n" \
      "Upgrade:websocket\r\n" \
      "Connection: Upgrade\r\n" \
      "Sec-WebSocket-Accept: %s\r\n" \
      "WebSocket-Location: ws://%s%s\r\n\r\n"

s_handle = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_handle.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s_handle.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,SEND_BUFF_SIZE)
s_handle.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,SEND_BUFF_SIZE)

current_buff_size = s_handle.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
print('current_buff_size =',current_buff_size)

s_handle.bind((host,port))
s_handle.listen(5)

while 1 :
    conn,addr = s_handle.accept()
    data = conn.recv(REV_BUFF_SIZE)
    headers = utility.websocketUtility.wsUtility.get_headers(data)
    value = headers['Sec-WebSocket-Key'] + magic_string
    ac = base64.b64encode(hashlib.sha1(value.encode('utf-8')).digest())
    response_str = response_tpl % (ac.decode('utf-8'), headers['Host'], headers['url'])
   
    print('Connected by',addr,' data =',response_str)

    conn.sendall(bytes(response_str, encoding='utf-8'))