# @before-stub-for-debug-begin
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 判断 ransomNote 能不能由 magazine 里面的字符
        # 遍历 ransomNote 并检查 magazine 中是否有所有字母
        # 因此需要将 magazine 中的字符串整理为{字母：频次}的hash table

        hash_table = {}

        for i in magazine:
            hash_table[i] = hash_table.get(i, 0) + 1

        for j in ransomNote:
            # 注意要在这里检查频次是否为0
            if j in hash_table and hash_table[j]:
                hash_table[j] = hash_table.get(j) - 1
            else:
                return False
        return True


# @lc code=end

