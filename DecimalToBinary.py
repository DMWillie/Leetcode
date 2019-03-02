# -*- coding:utf-8 -*-
__author__='Willie'

"""
由于字符串str并没有相加，例如''+1这样调用是错误的,
也并没str(1)将整数变为字符串这样的函数
所以将整数变为字符串可以利用格式化这样的方式
"""
#十进制转换为二进制
def dtob(n):
     result=''
     list1=[]
     while n>1:
         m=n%2
         n=n/2
         list1.append(m)
     list1.append(1)
     while list1!=[]:
         result=result+'%d' % list1.pop()
     return result

number=int(raw_input("请输入一个十进制数:"))
print '%d 对应的二进制数为: %s' %(number,dtob(number))

