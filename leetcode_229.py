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
    def reverseKGroup(self, head, k):
        if head is None or k == 0:
            return head

        dummy = ListNode(-1)
        dummy.next = head        
        prev = dummy
        end = prev.next
        while end is not None:
            for i in range(k - 1):
                end = end.next
                if end is None:
                    break
            if end is not None:
                prev = self.reverse(prev, prev.next, end)
                end = prev.next
        return dummy.next

    def reverse(self, prev, start, end):
        end_next = end.next
        end.next = None
        cur = start
        while cur is not None:
            cur_next = cur.next
            cur.next = prev.next
            prev.next = cur
            cur = cur_next
        start.next = end_next
        return start


s = Solution()
h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)
print s.reverseKGroup(h, 3)
