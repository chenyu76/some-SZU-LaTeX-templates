# _*_ coding : utf-8 _*_
import socket
import requests  # 用于向目标网站发送请求
import time

# 注意：这个脚本仅在宿舍区可用
# 教学区的脚本见: loginSZUnetworkTeachingArea.py
# 如果学校在未来更改了校园网登录方式，脚本可能会失效。
cardID = "114514"  # 修改为你的校园卡号
loginPw = "1919810"  # 修改为你的登录密码

proxyValue = 0


def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def try_login():
    print("通过http://172.30.255.42:801连接")
    url = (
        "http://172.30.255.42:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=,1,"
        + cardID
        + "&user_password="
        + loginPw
        + "&wlan_user_ip="
        + get_host_ip()
        + "&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=2&lang=zh-cn&v=9847&lang=zh"
    )
    response = -1
    try:
        response = requests.get(
            url
        ).status_code  # 直接利用 GET 方式请求这个 URL 同时获取状态码
    except Exception as e:
        print("状态码{}".format(response))  # 打印状态码
        return "连接失败：\n" + str(e)

    if response == 200:
        return True

    return False


def exitAfter1s():
    print("即将自动关闭……")
    time.sleep(1)
    exit()


if __name__ == "__main__":
    try1 = try_login()
    if try1:
        print("连接成功")
    else:
        print("连接失败")
        print(try1)

    exitAfter1s()
