# 正则表达式和 re 模块
# regular expression
# 一般字符
# '.' -> 匹配单个字符（不含换行符）
# '\' -> 转义字符
# '[abc...]' -> 匹配[...]中的任意1个字符
# 预定义字符集
# '\d' -> 匹配1个数字字符，等价于 [0-9]
# '\D' -> 匹配1个非数字的字符，等价于 [^0-9]
# '\s' -> 匹配空白字符，包括空格、制表、换行、换页，等价于 [\f\n\r\t\v]
# '\S' -> 匹配非空白字符，等价于 [^\f\n\r\t\v]
# '\w' -> 匹配单词字符，包括下划线，等价于 [A-Za-z0-9_]
# '\W' -> 匹配非单词字符，[^A-Za-z0-9_]
# 数量词
# '*' -> 匹配前一个字符 0 次或无限次
# '+' -> 匹配前一个字符 1 次或无限次
# '?' -> 匹配前一个字符 0 次或 1 次
# '{m}' -> 匹配前一个字符 m 次
# '{m,n}' -> 匹配前一个字符 m 至 n 次

# '(.*?)' -> 匹配任意字符, 返回 () 中的内容

# Python re 模块
# search()函数, 匹配第一个符合规律的内容
# sub()函数, 替换字符串中的匹配项
# findall()函数, 匹配所有符合规律的内容, 返回结果是列表

import re

sample_1 = 'one1two2three3four4five5'
sample_2 = 'xxIxxfahigihbarhxxLovexxdgraergeragrbbyuxxPythonxxfjhohjqqw'
# 提取数字12345
infos = re.findall('\d', sample_1)
print(infos)
# 提取单词 one two three four five
infos = re.findall('(.*?)\d', sample_1)
print(infos)
# 提取 xx...xx 夹的字符串
infos = re.findall('xx(.*?)xx', sample_2)
print(infos)













