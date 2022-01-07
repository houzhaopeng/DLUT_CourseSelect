from selenium import webdriver
import time
import threading

def xuanke(button):
    print(str(button) + " 创建成功")
    opt = webdriver.ChromeOptions()  # 创建浏览器
    opt.set_headless()  # 无窗口模式
    driver = webdriver.Chrome(options=opt)  # 创建浏览器对象
    driver.get('https://sso.dlut.edu.cn/cas/login?service=http://202.118.65.123/pyxx/LoginCAS.aspx?a=1')  # 打开网页
    # driver.maximize_window()                      #最大化窗口
    time.sleep(2)  # 加载等待
    driver.find_element_by_xpath('//*[@class="login_box_input person"]').send_keys(
        "xxxxxxxx")  # 利用xpath查找元素
    driver.find_element_by_xpath('//*[@class="login_box_input lock"]').send_keys(
        "xxxxxxxx")  # 利用xpath查找元素
    driver.find_element_by_xpath("//span[@class='landing_btn_bg']/input").click()  # 点击按钮

    driver.get('http://202.118.65.123/pyxx/pygl/pyjhxk.aspx?xh=22109051')
    # MainWork_dgData_Linkbutton2_30
    while (1):
        driver.find_element_by_xpath("//*[@id='MainWork_dgData_Linkbutton2_" + button + "']").click()  # 点击按钮
        time.sleep(1)
        ale = driver.switch_to_alert()
        ale.accept()
        time.sleep(1)
        ale = driver.switch_to_alert()
        text = ale.text
        print(str(button) + " " + text)
        if '成功' in text:
            ale.accept()
            time.sleep(1)
            break
        else:
            ale.accept()
            time.sleep(1)
    while (1):
        print(str(button) + ' 选课成功~！')
        time.sleep(1)

if __name__ == '__main__':
    # coding=utf-8 name='TestThread'
    for button in [30, 31, 35, 36, 37, 38, 39, 40]:
        thread = threading.Thread(target=xuanke, args=(str(button),))
        thread.start()
        print(str(button) + "创建代码运行成功")
    for button in range(42, 50):
        thread = threading.Thread(target=xuanke, args=(str(button),))
        thread.start()
        print(str(button) + "创建代码运行成功")

