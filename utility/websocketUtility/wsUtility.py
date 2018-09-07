"""
websocket 工具类
"""

"""
将请求头格式化成字典
:param data:
:return :
"""
def get_headers(data):
    header_dict = {}
    data = str(data,encoding='utf-8')

    for i in data.split('\r\n'):
        print(i)
    header,body = data.split('\r\n\r\n',1)
    header_list = header.split('\r\n')
    for i in range(0,len(header_list)):
        if i == 0 :
            if len(header_list[i].split(' ')) == 3:
                header_dict['method'],header_dict['url'], header_dict['protocol'] = header_list[i].split(' ')
        else:
            k, v = header_list[i].split(':', 1)
            header_dict[k] = v.strip()
    return header_dict

