#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#
from collections import deque
# @lc code=start
class MyStack:

    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()


    def push(self, x: int) -> None:
        self.queue_in.append(x)


    def pop(self) -> int:
        if self.empty():
            return None

        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())
        
        self.queue_in, self.queue_out = self.queue_out, self.queue_in    # 交换in和out，这也是为啥in只用来存
        return self.queue_out.popleft()


    def top(self) -> int:
        if self.empty():
            return None
        
        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        res = self.queue_out.popleft()
        self.queue_in.append(res)
        return res
        


    def empty(self) -> bool:
        # 当队列中有一个非空时 则非空
        return not (self.queue_in)



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

