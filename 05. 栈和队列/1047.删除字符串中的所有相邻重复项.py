#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
from collections import deque
class Solution:
    def removeDuplicates(self, s: str) -> str:
        s_queue = deque()
        res = []
        for item in s:
            if not s_queue:
                s_queue.append(item)
            else:
                top = s_queue.pop()
                if item != top:
                    s_queue.append(top)
                    s_queue.append(item)
        if s_queue:
            for i in range(len(s_queue)):
                res.append(s_queue.popleft())
            return "".join(res)
        else:
            return ""
            

# @lc code=end

