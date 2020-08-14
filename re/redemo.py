#正则表达式
import re

#1、"."通配符------只代表一个元素
res1 = re.findall('s.','sonqinsio')         #1、只需要2个必填的参数（正则表达式，处理的字符串） 2、返回类型：列表
print(res1)

#2、"*"出现0次或者多次
res2 = re.findall('o.*','ssongqinsio')
print(res2)

#3、"+"出现1次或者多次
res3 = re.findall('o.+','ssongqinsio')
print(res3)

#4、"?" 出现0次或1次，非贪婪     常用方式(.+?)，(.*?)
res4 = re.findall('so(.+?)','ssongqinsio')
print(res4)

#5、"\w" 匹配所有字母 数字 下划线 表示一个元素
res5 = re.findall('\w','ssong#qin')
print(res5)

#6、"{n}"重复n次
res6 = re.findall('\w{3}','ssong#qin')
print(res6)

#7、"\W" 匹配所有非（字母 数字 下划线） 表示一个元素
res7 = re.findall('\W','ssong##qin')
print(res7)

#8、匹配任意非空字符
res8 = re.findall('\S','s song##qin')
print(res8)

#9、"\d"匹配所有的数字0-9
res9 = re.findall('\d{3}','s so1245ng54##qin')
print(res9)


#10、"\D"匹配所有的非（数字0-9）
res10 = re.findall('\D{3}','s so1245ng54##qin')
print(res10)

#11、"^"匹配字符串的开头
#12、"$"匹配字符串的结尾


"""
re 模块的常用方法
1、re.match(pattern,str,flages=0)
   从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
   
   
2、re.search(pattern,str,flages=0)
    扫描整个字符串并返回第一个成功匹配的
    
3、re.sub(pattern,repl,str,count=0)
    用于替换字符串中的匹配项，repl:替换的字符串，也可以是一个函数
    
4、re.complie(pattern[,flags])
    用于编译正则表达式，生成一个正则表达式对象，供match（）和search（）这两个函数使用
    
5、findall（str[,pos[,endpos]]）
    在字符串中找到正则表达式所匹配的所有子串，并返回一个列表如果没有找到匹配的，则返回空列表
    
6、re.split(pattern,str[,maxsplit=0,flags=0])
    能够匹配的子串将字符串分割后返回列表
"""

#re.compile
reobject = re.compile('\d{3}')
aaa = reobject.findall('asdewr24346543263thdh')
print(aaa)

#13、装饰符 re.I 忽略大小写
res13 = re.findall('s.','so1245Sng54##qin',re.I)
print(res13)

#14、装饰符 re.S
res14 = re.findall('s.','so1245Sng54##qinS\n',re.I|re.S)
print(res14)

#15、re.L 做本地化识别匹配
#16、re.M 多行匹配，影响^和$
#17、re.U 根据Unicode字符集解析字符。这个标志影响\w \W \B \b
#18、re.X 该标志通过给予你灵活的格式以便你将正则表达式写个更易理解

