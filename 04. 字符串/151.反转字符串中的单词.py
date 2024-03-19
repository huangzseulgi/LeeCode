# @before-stub-for-debug-begin
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s_list = s.split() 
        
        l, r = 0, len(s_list) - 1
        while l < r:
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1
        return ' '.join(s_list)
# @lc code=end

