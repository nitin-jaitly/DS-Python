
class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class LL:
    def cycle_exists(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False



