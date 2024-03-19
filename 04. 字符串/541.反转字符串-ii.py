# @before-stub-for-debug-begin

from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(left, right, s_list):
            while left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1  
            
        s_list = list(s)
        n = len(s_list)
        for i in range(0, n, 2*k):
            reverse(i, min(i + k - 1, n - 1), s_list)
        return ''.join(s_list)

             

# @lc code=end

