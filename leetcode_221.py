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
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        result = ListNode(-1)
        cur = result
        while l1 is not None or l2 is not None:
            if cur.val >= 10:
                cur.next = ListNode(cur.val / 10)
                cur.val = cur.val % 10
            else:
                cur.next = ListNode(0)
            cur = cur.next
            if l1 is not None:
                cur.val += l1.val
                l1 = l1.next
            if l2 is not None:
                cur.val += l2.val
                l2 = l2.next
        if cur is not None and cur.val >= 10:
            cur.next = ListNode(cur.val / 10)
            cur.val = cur.val % 10
        return result.next

s = Solution()
print s.addTwoNumbers(ListNode(5), ListNode(5))
