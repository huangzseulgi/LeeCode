# @before-stub-for-debug-begin
from python3problem59 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        cnt = 1
        start_x = 0
        start_y = 0
        offset = 1
        loop, mid = n // 2, n // 2
        matrix = [[0]*n for _ in range(n)]
        # 外循环
        for offset in range(1, loop + 1):
            # 内循环
            for j in range(start_y, n-offset):
                matrix[start_x][j] = cnt
                cnt += 1
            
            for i in range(start_x, n-offset):
                matrix[i][n-offset] = cnt
                cnt += 1
            
            for j in range(n-offset, start_y, -1):
                matrix[n-offset][j] = cnt
                cnt += 1
            
            for i in range(n-offset, start_x, -1):
                matrix[i][start_y] = cnt
                cnt += 1 

            start_x += 1
            start_y += 1
         
        #  n为奇数时还需要填充一个芯
        if n % 2 != 0:
            matrix[mid][mid] = cnt
                      
        return matrix
# @lc code=end

