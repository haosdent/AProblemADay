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
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        for i in range(1, n + 1):
            if i == m:
                prev_m = prev

            if i > m and i <= n:
                prev.next = head.next
                head.next = prev_m.next
                prev_m.next = head
                head = prev

            prev = head
            head = head.next

        return dummy.next

s = Solution()
s.reverseBetween()
