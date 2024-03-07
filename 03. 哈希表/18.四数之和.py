#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
from typing import *
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if nums[i] > target and nums[i] > 0 and target > 0:  # a的剪枝
                break
            if i > 0 and nums[i] == nums[i-1]:  # a的去重
                continue
            for j in range(i+1, n): 
                if nums[i] + nums[j] > target and target > 0:  # b的剪枝
                    break
                if j > i+1 and nums[j] == nums[j-1]:  # b的去重
                    continue

                left, right = j+1, n-1

                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target: # 在得到一个结果之后执行去重的操作
                        res.append([nums[i],  nums[j], nums[left], nums[right]]) 
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return res


# @lc code=end

