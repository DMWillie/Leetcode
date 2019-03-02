"""
    作者:北辰
    功能:反转整数
    版本3.0
    日期:21/06/2018
    2.0改进之处:直接取模计算,提高程序运行效率
    3.0改进之处:利用python的特性,直接在字符串上进行反转,简化代码,提高运行效率
"""

import math

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >=0:
            flag = 1
        else:
            flag = -1
            x = abs(x)
        temp = str(x)
        res = int(temp[::-1])*flag
        # if res < -math.pow(2,31) or res > math.pow(2,31)-1:
        #     return 0
        if res.bit_length() >= 32:  # 利用整数的bit_length()方法直接判断是否溢出
            return 0
        else:
            return res

s=Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
print(s.reverse(12333333332))