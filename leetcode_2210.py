# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        cur = head
        while cur is not None:
            tmp = RandomListNode(cur.label)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        cur = head
        while cur is not None:
            tmp = cur.next
            if cur.random is not None:
                tmp.random = cur.random.next
            cur = tmp.next
        
        new_head = RandomListNode(-1)
        cur = head
        tmp = new_head
        while cur is not None:
            tmp.next = cur.next
            tmp = tmp.next
            cur.next = tmp.next
            cur = cur.next
        return new_head.next

if __name__ == "__main__":
    s = Solution()
    l = RandomListNode(2)
    l.next = RandomListNode(3)
    print s.copyRandomList(l)
