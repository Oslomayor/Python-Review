# Python-Review

#### 6:20 PM, Feb 10th, 2018 @ home, Shangyu

### 正则表达式 regular expression

#### 一般字符

1. '.' -> 匹配单个字符（不含换行符）
2. '\' -> 转义字符
3. '[abc...]' -> 匹配[...]中的任意1个字符

####  预定义字符集

1. '\d' -> 匹配1个数字字符，等价于 [0-9]
2. '\D' -> 匹配1个非数字的字符，等价于 [^0-9]
3. '\s' -> 匹配空白字符，包括空格、制表、换行、换页，等价于 [\f\n\r\t\v]
4. '\S' -> 匹配非空白字符，等价于 [^\f\n\r\t\v]
5. '\w' -> 匹配单词字符，包括下划线，等价于 [A-Za-z0-9_]
6. '\W' -> 匹配非单词字符，[^A-Za-z0-9_]

####  数量词

1. '*' -> 匹配前一个字符 0 次或无限次
2. '+' -> 匹配前一个字符 1 次或无限次
3. '?' -> 匹配前一个字符 0 次或 1 次
4. '{m}' -> 匹配前一个字符 m 次
5. '{m,n}' -> 匹配前一个字符 m 至 n 次

__'(.*?)' -> 匹配任意字符, 返回 () 中的内容__

### Python re 模块

#### re 函数

1. search()函数, 匹配第一个符合规律的内容
2. sub()函数, 替换字符串中的匹配项
3. findall()函数, 匹配所有符合规律的内容, 返回结果是列表

#### re 模块修饰符
re.S 可以跨行匹配

```python
sample_3 = '''<div>Denis
</div>'''
infos = re.findall('<div>(.*?)</div>', sample_3, re.S)
print(infos)
```

输出：

```python
['Denis\n']
```

### Python GUI

##### 使用Python自带的图形库Tkinter,可以方便地制作窗口程序

#### 消息框

代码

```python
from tkinter import messagebox
# 确定/取消 消息框
messagebox.askokcancel("提示框", "Hello!")
```

效果

![](https://github.com/Oslomayor/Markdown-Imglib/blob/master/Imgs/tkinter%E6%B6%88%E6%81%AF%E6%A1%86.PNG?raw=true)

点击确定返回一个 True, 点击取消返回 False

#### 按钮

代码

```python
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
```

效果

![](https://github.com/Oslomayor/Markdown-Imglib/blob/master/Imgs/tkinter%E6%8C%89%E9%92%AE.PNG?raw=true)

### Python xlwt-Excel 储存
```python
import xlwt
book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('Sheet1')
# sheet.write(#行，#列，#内容)
sheet.write(0,0,'Python')
sheet.write(0,1,'Excel')
book.save('E:\AllPrj\PyCharmPrj\py-crawler\Excel 存储\Excel 储存测试.xls')
```

### Python 多进程库
[Python multiprocessing](https://github.com/Oslomayor/Python-Multiprocessing-Test)
