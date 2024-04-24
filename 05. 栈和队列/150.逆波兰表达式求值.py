#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#
from typing import List
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operators = ["+", "-", "*", "/"]
        for item in tokens:
            
            # 数字可能包含负数 现有函数无法同时识别正整数和负整数
            if item in operators:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if item == "+":
                    new_num = num1 + num2
                if item == "-":
                    new_num = num1 - num2
                if item == "*":
                    new_num = num1 * num2
                if item == "/":
                    new_num = num1 / num2
                stack.append(new_num)
            else:
                stack.append(item)
        
        # 要求返回值为int类型
        return int(stack.pop())


# @lc code=end

