# @before-stub-for-debug-begin
from python3problem977 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, new_right = 0, len(nums) - 1, len(nums) - 1
        new_nums = [0] * len(nums)  # 生成一个和nums大小相同的数组

        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2: 
                new_nums[new_right] = nums[left] ** 2
                left += 1    
            else:
                new_nums[new_right] = nums[right] ** 2
                right -= 1
            
            new_right -= 1
            

        return new_nums

        
        

        
# @lc code=end

