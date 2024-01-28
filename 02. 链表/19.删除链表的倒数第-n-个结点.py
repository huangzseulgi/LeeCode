#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 创建虚拟头结点避免删除头结点时要另外执行
        dummy_head = ListNode(next=head)
        cur = dummy_head
        tail = dummy_head

        # 在cur和tail之间创建间隔n
        for _ in range(n):
            tail = tail.next

        # 将tail移动至链表尾部此时cur.next即为待删除元素
        while tail.next:
            cur = cur.next
            tail = tail.next
        
        cur.next = cur.next.next
        return dummy_head.next
        
        


# @lc code=end

