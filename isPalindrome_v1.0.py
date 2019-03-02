"""
    作者:北辰
    功能:判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数
    版本:2.0
    日期:24/06/2018
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        isPalindrome = False
        y = x      # 记录x的初始值
        if y < 0:
            return isPalindrome
        # 求出这个整数反转之后的整数
        res = 0
        while x != 0:
            res = res * 10 + x % 10
            x = int(x/10)        # 当跳出循环时x的值已经变为了0
        if y==res:
            isPalindrome = True
        return isPalindrome

s=Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))