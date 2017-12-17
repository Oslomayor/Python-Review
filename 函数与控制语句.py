# 函数与控制语句

# 函数
# 根据直角边计算直角三角形面积
def fun(a,b):
    return 1/2*a*b

print(fun(3,4))

# 电话号码保密
def change_number(num):
    hiding_num = num.replace(num[3:7], '*'*4)
    print(hiding_num)
change_number('13255712816')

# # 判断登陆密码
# def count_login():
#     password = input('password: ')
#     if password == 'Leavez':
#         print('输入成功！')
#     else :
#         print('输入错误！')
# count_login()

# 判断登陆密码，三次错误退出程序
def count_login():
    for i in range(0, 3):
        password = input('password:')
        if password == 'Leavez':
            print('输入正确！')
            # return退出函数，不带参数返回None
            return
        else:
            print('输入错误！')
    print('机会用完了！')
count_login()

# 计算1-100的和
sum = 0
for i in range(1, 101):
    sum = i+sum
print('1-100的和是', sum)
