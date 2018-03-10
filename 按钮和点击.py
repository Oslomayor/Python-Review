# 10:05PM, Mar 8th, 2018 @ dorm
# Python Tkinter
# GUI 图形编程
# 8:02PM, Mar 10th, 2018 @ HDU_Wireless

import tkinter

# 定义点击按钮后地执行函数
def click1():
    print("Clicked 1!")

def click2():
    print("Clicked 2!")

def click3():
    print("Clicked img1!")

def click4():
    print("Clicked img2!")

# 创建主窗体, 命名为 "My Screen"
# tkinter.TK 有个bug, className 的第一个字母会“被”小写，可以加个空格绕开bug
top = tkinter.Tk(className="My Screen")
# 定义最小窗口 400x400
top.minsize(400,400)

# 创建按钮
# command 后面只要跟函数名即可
# 点击按钮之后会执行自定义函数
b1 = tkinter.Button(top, text="点我", command=click1)
b2 = tkinter.Button(top, text="点我", command=click2)
# 添加按钮图片
img = tkinter.PhotoImage(file="E:\AllPrj\PyCharmPrj\py-GUI\img.png")
b3 = tkinter.Button(top, image=img, command=click3)
# 在按钮上同时显示图片和文字
b4 = tkinter.Button(top, image=img,text="Frances", command=click4, compound="top")

# 用 pack 函数，放置按钮到主窗体上
# 如果要指定位置则使用 palce 函数
# -------> X
# |
# |  窗口
# |
# Y
b1.place(x=0,y=20)
b2.pack()
b3.pack()
b4.pack()
top.mainloop()
