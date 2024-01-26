# @before-stub-for-debug-begin
from python3problem209 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        left, right = 0, 0
        min_len = float('inf')
        sum = 0

        while right < length:
            sum += nums[right]
            
            while sum >= target:
                min_len = min(min_len, right-left+1)
                sum -= nums[left]
                left += 1
            
            right += 1
        
        return min_len if min_len != float('inf') else 0
            


            



# @lc code=end

