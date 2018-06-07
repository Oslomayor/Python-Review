# 23:12, June 7th, 2018 @ Dorm
# Note: 需要插上串口模块才能运行程序
# To do:
# 1.如何自动查询 COM 口编号

import serial

try:
    ser = serial.Serial('COM4',9600)
    if True == ser.isOpen():
        print("COM4 已打开")
    else:
        print('串口打开失败')
except serial.serialutil.SerialException:
    print('请插入USB串口模块')

s = 'Hello, 你好\n'
for item in s:
    # 貌似只能发送比特流
    ser.write(item.encode('utf-8'))

# readline 读到 '\n' 结束
print(ser.readline().strip().decode('utf-8'))






