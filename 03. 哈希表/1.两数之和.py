# @before-stub-for-debug-begin
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import *
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} # 值：下标
        for i in range(len(nums)):
            need = target - nums[i]
            if need in map.keys():
                return [i, map[need]]
            else:
                map[nums[i]] = i
        return []

            
            
# @lc code=end

