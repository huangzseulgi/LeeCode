#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
from typing import List
from collections import deque


# @lc code=start
# 构造一个单调队列 使得队列中数据从队列头递减
class MyQueue:
    def __init__(self):
        self.queue = deque()

    def pop(self, value):
        # 当队列非空并且当前pop数据就是队头时pop
        if self.queue and value == self.queue[0]:
            self.queue.popleft()
        
    def push(self, value):
        # 当队列非空并且当前push的值大于队尾值时push
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        # 获取队列内当前最大的值
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        result = []

        for i in range(k):
            que.push(nums[i])
        result.append(que.front())  # 记录前k个的最大值

        for i in range(k, len(nums)):
            que.pop(nums[i - k])
            que.push(nums[i])
            result.append(que.front())

        return result
# @lc code=end

