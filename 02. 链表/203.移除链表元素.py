# @before-stub-for-debug-begin
from tkinter.tix import ListNoteBook
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# from tkinter.tix import ListNoteBook

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 处理空链表的情况
        if not head:
            return None
        
        # 处理头节点就是要删除的情况
        while head and head.val == val:
            head = head.next

        cur = head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head
# @lc code=end
