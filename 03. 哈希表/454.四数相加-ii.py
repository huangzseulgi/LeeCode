# @before-stub-for-debug-begin
from python3problem454 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#
from typing import *
# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        unordered_map = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sum = nums1[i] + nums2[j]
                unordered_map[sum] = unordered_map.get(sum, 0) + 1

        cnt = 0
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                sum = nums3[i] + nums4[j]
                need = 0 - sum
                if need in unordered_map:
                    cnt += unordered_map[need]
        return cnt
                    
                

# @lc code=end

