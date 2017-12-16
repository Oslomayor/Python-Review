# split()方法分离字符串, 转成列表
a = 'www.baidu.com'
print(a.split('.'))
b = 'www-baidu-com'
print(b.split('-'))

# replace()方法, 替换字符
c = '杜镇涛很帅'
print(c)
print(c.replace('很', '非常'))

# strip()方法, 除去两端空格或指定字符, 爬虫常用
d = '    python is cool   '
print(d)
print(d.strip())
e = '####@#!!## python is cool#######@!'
print(e)
print(e.strip('#!@'))

# format方法, 字符串中用{}留空待填
content = input('请输入搜素内容')
url_path = 'https://www/baidu.com/search/{}/'.format(content)
print(url_path)
