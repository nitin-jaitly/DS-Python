
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        # T BigO (n)
        # M BigO (1)
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

