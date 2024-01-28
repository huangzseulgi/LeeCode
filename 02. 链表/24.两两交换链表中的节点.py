#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        cur = dummy_head
        # 当cur.next.next.next == None 时，到链表尾部
        while cur.next and cur.next.next:
            pre = cur.next
            tail = cur.next.next.next

            cur.next = cur.next.next
            cur.next.next = pre
            pre.next = tail

            # 相邻两个元素交换，因此指针移动两位
            cur = cur.next.next
        return dummy_head.next








# @lc code=end

