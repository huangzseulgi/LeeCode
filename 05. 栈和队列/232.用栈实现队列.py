#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        # 栈实现队列需要两个栈
        self.stack_in = []
        self.stack_out = []



    def push(self, x: int) -> None:
        self.stack_in.append(x)


    def pop(self) -> int:
        if self.empty():
            return None
        
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()


    def peek(self) -> int:
        # 先pop出来获取了值之后再append进去
        res = self.pop()
        self.stack_out.append(res)
        return res


    def empty(self) -> bool:
        # 如果in和out都有值则队列非空
        return not (self.stack_in or self.stack_out)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

