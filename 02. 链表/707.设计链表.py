# @before-stub-for-debug-begin
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class MyLinkedList:
    # 定义链表
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0
      

    # 获取index值
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.dummy_head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        data = ListNode(val=val, next=self.dummy_head.next)
        self.dummy_head.next = data
        self.size += 1   # 完成增加操作不要忘记增加大小


    def addAtTail(self, val: int) -> None:
        data = ListNode(val=val)
        cur = self.dummy_head

        while cur.next:
            cur = cur.next
        cur.next = data
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        data = ListNode(val=val)
        cur = self.dummy_head
        
        for _ in range(index):
            cur = cur.next
        data.next = cur.next
        cur.next = data
        self.size += 1

        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        cur = self.dummy_head
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

