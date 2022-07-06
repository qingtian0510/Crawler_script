import re

# # findAll 匹配字符串所有的符合正则的内容，返回list
# lst = re.findall(r"\d+", "phone number is 10010,10086")
# print(lst)
# print("---------------------\n")
#
# # finditer 匹配字符串中所有的内容，返回迭代器(效率更高)，从迭代器中拿到内容需要.group()
# it = re.finditer(r"\d+", "phone number is 10010,10086")
# for i in it:
#     print(i.group())
#
# print("---------------------\n")
#
# # search 全文找到一个结果就返回，返回的结果是match对象，拿到数据需要.group()
# s = re.search(r"\d+", "phone number is 10010,10086")
# print(s.group())
# print("---------------------\n")
#
# # match 从头开始匹配，返回的结果是match对象，拿到数据需要.group()
# s = re.match(r"\d+", "1 phone number is 10010,10086")
# print(s.group())
# print("---------------------\n")

# # 预加载正则表达式
# obj = re.compile(r"\d+")
# ret = obj.finditer("phone number is 10010,10086")
# for i in ret:
#     print(i.group())

s = """
<div class='jay'><span id='1'>周杰伦</span></div>
<div class='jj'><span id='2'>林俊杰</span></div>
<div class='jojin'><span id='3'>蔡依林</span></div>
<div class='tony'><span id='4'>托尼</span></div>
"""
# .* 贪婪匹配：尽可能多地匹配
# .*? 懒惰匹配，尽可能少地匹配
# (?P<分组名称>正则表达式) 可以将正则表达式匹配的内容提取出来
# (?P<name>.*?) -> 吧 .*? 匹配的内容赋给 name组
obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>")

result = obj.finditer(s)
for it in result:
    print(it.group("id"))
    print(it.group("name"))