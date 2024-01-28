class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur_a, len_a = headA, 0
        cur_b, len_b = headB, 0

        # 将a和b都先移动到链表尾部得到链表长度
        while cur_a:
            cur_a = cur_a.next
            len_a += 1
        while cur_b:
            cur_b = cur_b.next
            len_b += 1
        
        # 始终让cur_a指向较长的链表
        cur_a, cur_b = headA, headB
        if len_b > len_a:
            cur_a, cur_b = cur_b, cur_a
            len_a, len_b = len_b, len_a
        
        
        # 计算两条链之间的长度差
        len_ab = len_a -len_b
        # 将两条链表尾部对齐
        for _ in range(len_ab):
            cur_a = cur_a.next
        
        # 将两条链同时移动并比较指针
        while cur_a and cur_b:
            if cur_a == cur_b:
                return cur_a
            cur_a = cur_a.next
            cur_b = cur_b.next
        
        return None