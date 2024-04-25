#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
from typing import List
# @lc code=start
        
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_ = {}
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1
        
        # 初始化一个小顶堆
        pri_que = []
        for item, freq in map_.items():
            heapq.heappush(pri_que, (freq, item))
            if len(pri_que) > k:
                heapq.heappop(pri_que)
        
        result = [0]*k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result



        

# @lc code=end

