
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LL:
    def remove_nth_from_end(self, head: ListNode, n:int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Move right pointer to the n-1 position
        while n > 0 and right:
            right = right.next
            n -= 1

        # Move right pointer to end so that left point to n-1
        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next
        return dummy.next
