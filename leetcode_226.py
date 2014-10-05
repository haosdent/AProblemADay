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
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None or k == 0:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        l = 0
        while p.next is not None:
            p = p.next
            l += 1
        k %= l
        p.next = dummy.next
        for i in range(l - k):
            p = p.next
        head = p.next
        p.next = None
        return head

s = Solution()
h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)
print s.rotateRight(h, 2)
