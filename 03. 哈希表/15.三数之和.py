# @before-stub-for-debug-begin
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import *
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 将数组排序之后用双指针法解决    
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            # a的剪枝
            if nums[i] > 0:
                return res
            
            # a的去重
            if i >= 1 and nums[i] == nums[i-1]:
                continue

            while left < right:
                # 求解三数之和
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # 跳过重复的元素
                    # b的去重 只要相等且左边小于右边则一直移动
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1

                elif sum < 0:
                    left += 1
                else:
                    right -= 1
                
        return res
                
            






# @lc code=end

