# _*_ coding : utf-8 _*_
import socket
import requests    # 用于向目标网站发送请求
import time

cardID = "114514"  # 修改为你的校园卡号
loginPw= "1919810" # 修改为你的登录密码

proxyValue=0

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


# 2025年1月11信息中心更新网络登陆页面后失效
def try_login1():
    print('通过https://drcom.szu.edu.cn/a70.htm连接')
    url = 'https://drcom.szu.edu.cn/a70.htm'#?isReback=1'
    data = {
        'DDDDD': cardID,
        'upass': loginPw,
        'R1':"0",
        'R2':"",
        'R6':"0",
        'para':"00",
        '0MKKey':"123456",
        'buttonClicked':"",
        'redirect_url':"",
        'err_flag':"",
        'username':"",
        'password':"",
        'user':"",
        'cmd':"",
        'Login':"",
        'R7':"0"
    }

    header = {
        'POST': '/a70.htm?isReback=1 HTTP/1.1',
        'Host': 'drcom.szu.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '148',
        'Origin': 'https://drcom.szu.edu.cn',
        'Connection': 'keep-alive',
        'Referer': 'https://drcom.szu.edu.cn/a70.htm?isReback=1',
        'Cookie': 'program=szdx_wlan0718; vlan=3440; ip=' + get_host_ip() + '; md5_login2='+cardID+'%7C'+loginPw+'; save_DDDDD='+cardID+'; save_upass='+loginPw,
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1'
    }
    #response = requests.post(url, data, headers=header).status_code  # POST 方式向 URL 发送表单，同时获取状态码
    response2 = -1
    try:
        response2 = requests.post(url, data, headers=header).status_code  # POST 方式向 URL 发送表单，同时获取状态码
    except Exception as e:
        print(str(e))
    print("状态码{}".format(response2))  # 打印状态码
    
    if response2 == 200:
        return True
    
    return False

def try_login2():
    #换一个方法
    print('通过http://172.30.255.42:801连接')
    url = 'http://172.30.255.42:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=,1,'+cardID+'&user_password='+loginPw+'&wlan_user_ip='+get_host_ip()+'&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=2&lang=zh-cn&v=9847&lang=zh'    
    response = -1
    try:
        response = requests.get(url).status_code  # 直接利用 GET 方式请求这个 URL 同时获取状态码
    except Exception as e:
        print("状态码{}".format(response))  # 打印状态码 
        return '连接失败：\n' + str(e)    

    if response == 200:
        return True

    return False
    #url = 'https://drcom.szu.edu.cn:801/eportal/extern/szdx_wlan0718/ip/1/loginbox.js?version=1.4_1677723729742'  # 这行是你需要根据自己的情况修改的地方
    
def exitAfter1s():   
    print('即将自动关闭……')
    time.sleep(1)
    exit()


if __name__ == '__main__':
    #print(get_host_ip())
    
    # if try_login1():
    #     print('连接成功')
    #     exitAfter1s()
    
    print('连接失败，尝试方法2')
    try2 = try_login2()
    if try2:
        print('连接成功')
    else: 
        print('连接失败')
        print(try2)

    exitAfter1s()
    #os.system('pause')
