"""
    作者:北辰
    功能:对一个非空整数数组最后一个元素加一
    版本:1.0
    日期:05/07/2018
"""
"""
问题描述:给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp=''
        for num in digits:
            temp+=str(num)
        result=str(int(temp)+1)
        result_list=[]
        for number in result:
            result_list.append(int(number))
        return result_list

solution=Solution()
print(solution.plusOne([1,2,9]))