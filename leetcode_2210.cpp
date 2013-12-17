class Solution {
public:
  RandomListNode *copyRandomList(RandomListNode *head) {
    if (head == nullptr) return nullptr;

    for (RandomListNode *cur = head; cur != nullptr; ) {
      RandomListNode *node = new RandomListNode(cur->label);
      node->next = cur->next;
      cur->next = node;
      cur = node->next;
    }

    for (RandomListNode *cur = head; cur !=nullptr; ) {
      if (cur->random != NULL)
        cur->next->random = cur->random->next;
      cur = cur->next->next;
    }

    RandomListNode new_head(-1);
    for (RandomListNode *cur = head, *new_cur = &new_head; cur != nullptr; ) {
      new_cur->next = cur->next;
      new_cur = newcur->next;
      cur->next = cur->next->next;
      cur = cur->next;
    }
    return new_head.next;
  }
}
