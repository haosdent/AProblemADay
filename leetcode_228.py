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
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while cur.next is not None and cur.next.next is not None:
            x = cur.next
            y = cur.next.next
            z = cur.next.next.next
            cur.next = y
            y.next = x
            x.next = z
            cur = cur.next.next
        return dummy.next

s = Solution()
h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
print s.swapPairs(h)
