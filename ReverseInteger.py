"""
    作者:北辰
    功能:反转整数
给定一个 32 位有符号整数，将整数中的数字进行反转
示例 1:                    示例 2:                  示例3：
输入: 123				   输入: -123				输入:120
输出: 321				   输出: -321               输出：21
注意:假设我们的环境只能存储32位有符号整数,其数值范围是[−2^31,2^31 − 1].根据这个假设,如果反转后的整数溢出,则返回0
    版本:1.0
    日期:04/05/2018
"""
import math

class ReverseInteger(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            x=abs(x)
            temp=[]
            resultLst=[]
            strx="%d" % x
            for n in strx:
                temp.append(n)
            #去除temp列表中末尾为0的数字
            while True:
                num=int(temp.pop())
                if num!=0:
                    break
            #temp末尾的第一个不为0的字符加入结果列表中
            resultLst.append(num)
            while temp!=[]:
                resultLst.append(int(temp.pop()))
            result='-'
            for number in resultLst:
                result+="%d" % number
            if int(result)<-math.pow(2,31):
                return 0
            else:
                return int(result)
        elif x>0:
            temp=[]
            resultLst=[]
            strx="%d" % x
            for n in strx:
                temp.append(n)
            #去除temp列表中末尾为0的数字
            while True:
                num=int(temp.pop())
                if num!=0:
                    break
            #temp末尾的第一个不为0的字符加入结果列表中
            resultLst.append(num)
            while temp!=[]:
                resultLst.append(int(temp.pop()))
            result=''
            for number in resultLst:
                result+="%d" % number
            if int(result)>math.pow(2,31)-1:
                return 0
            else:
                return int(result)
        else:
            return 0

s=ReverseInteger()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))