class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        cur = self
        r = []
        while cur is not None:
            r.append(cur.val)
            cur = cur.next
        return str(r)

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        left_dummy = ListNode(-1)
        right_dummy = ListNode(-1)
        left_cur = left_dummy
        right_cur = right_dummy
        while head is not None:
            if head.val < x:
                left_cur.next = head
                left_cur = left_cur.next
            else:
                right_cur.next = head
                right_cur = right_cur.next
            head_next = head.next
            head.next = None
            head = head_next
        left_cur.next = right_dummy.next
        right_cur.next = None
        return left_dummy.next
            
s = Solution()
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)
#print s.partition(head, 3)
head = ListNode(3)
head.next = ListNode(1)
head.next.next = ListNode(2)
print s.partition(head, 3)
