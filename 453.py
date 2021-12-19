
"""
Author：G3
Time: 2021/7/13 
Software: PyCharm
"""
# 该例程仅供学习使用

# 使用psutil来判断QQ是否登录
import psutil,time,os
import pyperclip
import pyautogui as gui

people = '清蒸桂皮'	# 好友全称
message = '为什么为什么'	# 发送的消息

QQ_dir = r'E:\Tencent\QQ\Bin\QQ.exe'	# QQ路径

# 判断QQ是否登录
def proc_exist(process_name):
    pl = psutil.pids()
    for pid in pl:  # 通过PID判断
        if psutil.Process(pid).name() == process_name:
            return isinstance(pid,int)

# 发送消息
def send_msg(people, msg):
    if proc_exist('QQ.exe'):
        # 打开QQ主界面
        gui.moveTo(1580, 1080, duration=0.2)
        gui.moveTo(1580, 1050, duration=0.2)
        gui.click()
        time.sleep(0.5)
    else:
        # 登录QQ
        QQ_login()

    # 搜索好友并打开聊天窗口
    gui.moveTo(1650, 285, duration=0.2)
    gui.click()
    time.sleep(0.5)
    pyperclip.copy(people)
    gui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    gui.hotkey('Enter')
    time.sleep(1)

    # 输入需要发送的信息
    gui.moveTo(600, 850, duration=0.2)
    gui.click()
    pyperclip.copy(msg)
    gui.hotkey('ctrl', 'v')
    gui.hotkey('Enter')

    # 隐藏主界面并退出聊天界面
    gui.moveTo(1850, 150, duration=0.5)
    gui.click()
    time.sleep(0.5)
    gui.hotkey('ctrl', 'w')

# 登录QQ
def QQ_login():
    os.startfile(QQ_dir)
    print('正在打开QQ')

    time.sleep(3)
    gui.moveTo(960, 695, duration=0.5)
    gui.click()
    time.sleep(10)


if __name__ == "__main__":


    send_msg(people,message)

# 查看鼠标位置
# while True:
#     last_position=gui.position()
#     if last_position!=gui.position():
#         print(gui.position())
