#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, 0
        while right < len(nums):
            if nums[right] == val:
                right += 1
            else:
                nums[left] = nums[right]
                left += 1
                right += 1
        return left
# @lc code=end

