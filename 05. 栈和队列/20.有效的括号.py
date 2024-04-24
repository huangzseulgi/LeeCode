#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        s_dict = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []

        for item in s:
            if item in s_dict.keys():
                stack.append(item)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if item != s_dict[top]:
                    return False
        
        return True if not stack else False
                


# @lc code=end

