git#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#
from typing import *
# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        head, tail = 0, len(s)-1
        while head < tail:
            tmp = s[head]
            s[head] = s[tail]
            s[tail] = tmp
            head += 1
            tail -= 1
        return s
# @lc code=end

