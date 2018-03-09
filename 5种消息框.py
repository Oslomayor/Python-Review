# 9:47PM, Mar 8th, 2018 @ dorm
# Python Tkinter
# GUI 图形编程

import tkinter
from tkinter import messagebox

# 确定/取消 消息框
messagebox.askokcancel("提示框", "Hello!")

# 是/否 消息框
messagebox.askyesno("提示框", "Yes or No?")

# 是/否/取消
res = messagebox.askyesnocancel("提示框", "Yes, No or Cancel?")
print("Cancel = ", res)
# Cancel = None

# 重试/取消
messagebox.askretrycancel("提示框", "Retry or Cancel?")

# 问题 消息框
messagebox.askquestion("提示框", "问题")