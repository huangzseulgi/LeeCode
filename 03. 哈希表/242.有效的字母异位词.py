#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        s_cnt = Counter(s)
        t_cnt = Counter(t)
        return True if s_cnt == t_cnt else False
        
# @lc code=end

