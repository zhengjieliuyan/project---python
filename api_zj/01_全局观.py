import requests
requests.get()  #发送get请求
requests.post()   #发送post请求
requests.delete()  #发送delete请求
requests.put()   #发送put请求
requests.request()  #最核心的方法
#响应  response
rep = requests.request()
#返回字符串数据
print(rep.text)
#返回字节格式的数据---图片
print(rep.content)
#返回字典格式的数据
print(rep.json())
#状态码
print(rep.status_code)
#返回状态信息
print(rep.reason)
#返回cookie信息
print(rep.cookies)
#返回编码格式
print(rep.encoding)
#返回响应头信息
print(rep.headers)
#请求方式：get/post/delete/put
#请求参数类型  ：键值对,json格式，文件格式
#发送get请求
url = ''
params = ''
requests.get(url, params=None)


