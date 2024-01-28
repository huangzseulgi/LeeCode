#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 定义左右指针
        left, right = 0, len(nums)-1
        
		# 左闭 右开
  		# while left < right: 
        # 左闭 右闭
        while left <= right:   
        
            # mid = (right - left) // 2 + left
            mid = (right + left) // 2
	
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # 左闭 右开（right不包含在内）
            	# right = mid
                # 左闭 右闭
                right = mid - 1
                
                
            else:
                left = mid + 1
        return -1
    # @lc code=end

