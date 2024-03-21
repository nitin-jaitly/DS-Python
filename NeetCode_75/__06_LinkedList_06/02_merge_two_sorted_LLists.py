

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LL:
    def merge_two_lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        l1 = list1
        l2 = list2
        my_list_node = ListNode()
        my_ll = my_list_node

        while l1 and l2:
            if l1.val < l2.val:
                my_ll.next = l1
                l1 = l1.next
            else:
                my_ll.next = l2
                l2 = l2.next
            my_ll = my_ll.next

        if l1:
            my_ll.next = l1
        elif l2:
            my_ll.next = l2

        return my_list_node.next
