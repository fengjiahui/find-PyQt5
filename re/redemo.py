#正则表达式
import re

#"."通配符------只代表一个元素
res = re.findall('s.','sonqin')
#1、只需要2个必填的参数（正则表达式，处理的字符串） 2、返回类型：列表
print(res)
