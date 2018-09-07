class NetBase:
    host = '127.0.0.1'
    port = 50007
    SEND_BUFF_SIZE = 4096
    REV_BUFF_SIZE = 4096
    connectCount = 5

    def creatSocket(self):
        raise NotImplementedError