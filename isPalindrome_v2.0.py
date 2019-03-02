"""
    作者:北辰
    功能:判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数
    版本:1.0
    日期:22/06/2018
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        isPalindrome = False
        if str(x)==str(x)[::-1]:
            isPalindrome = True

        return isPalindrome

s=Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))