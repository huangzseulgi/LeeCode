#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:  
        record = set()      
        while n not in record:
            record.add(n)
            n_str = str(n)
            new_sum = 0
            for i in n_str:
                new_sum += int(i) ** 2
            if new_sum == 1:
                return True
            if new_sum in record:
                return False
            else:
                n = new_sum
            
# @lc code=end

