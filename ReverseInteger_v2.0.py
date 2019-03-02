"""
    作者:北辰
    功能:反转整数
    版本2.0
    日期:20/06/2018
    2.0改进之处:直接取模计算,提高程序运行效率
"""

import math

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = False
        if x<0:
            is_negative = True
        res=0
        if is_negative:
            x=abs(x)        # 负数对某个数取模和该负数对应的正数取模不一样
        while x!=0:
            res = res*10+x%10
            x = int(x/10)      # py3中两个整数相除是小数
        if is_negative:
            res = -res
        if res < -math.pow(2,31) or res > math.pow(2,31)-1:
            return 0
        else:
            return res

s=Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
print(s.reverse(12333333332))