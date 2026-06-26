from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 注意：这个脚本仅在教学区可用
# 宿舍区的脚本见: loginSZUnetworkDormArea.py
# 如果学校在未来更改了校园网登录方式，脚本可能会失效。
#
# 这个脚本并非由我编写，在这里感谢cxy学长提供的帮助。
# 
# 配置账号和密码
USERNAME = "114514"
PASSWORD = "1919810"
URL = "https://net.szu.edu.cn"


# 检查和登录函数
def check_and_login():
    # 启动浏览器 (需要事先安装 Chrome 和 ChromeDriver)
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")  # 如果不需要显示浏览器窗口，可以启用这一行
    driver = webdriver.Chrome(options=options)

    try:
        # 打开网页
        driver.get(URL)
        time.sleep(3)  # 等待页面加载

        # 检查是否已登录
        if "登录" in driver.page_source or "login" in driver.page_source:
            print("未登录，开始登录流程...")
            
            # 输入账号
            username_field = driver.find_element(By.ID,"username")
            username_field.clear()
            username_field.send_keys(USERNAME)

            # 输入密码
            #password_field = driver.find_element(By.NAME, "password")
            password_field = driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys(PASSWORD)

            # 提交登录
            password_field.send_keys(Keys.RETURN)
            time.sleep(5)  # 等待登录结果

            if "登录成功" in driver.page_source or "success" in driver.current_url:
                print("登录成功！")
            else:
                print("登录失败，请检查账号或网络状态。")
        else:
            print("已登录，无需重复操作。")
    except Exception as e:
        print(f"出现错误: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    check_and_login()
