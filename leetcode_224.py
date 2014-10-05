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
    # @return a ListNode
    def deleteDuplicates(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while head is not None:
            duplicated = False
            while head.next is not None and head.val == head.next.val:
                duplicated = True
                head = head.next
            if duplicated:
                head = head.next
                continue
            prev.next = head
            prev = prev.next
            head = head.next
        prev.next = head        
        return dummy.next

s = Solution()
h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(2)
print s.deleteDuplicates(h)
