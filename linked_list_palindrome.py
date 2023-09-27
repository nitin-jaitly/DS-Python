
class Node:
    def __init__(self,data):
        self.data = data;
        self.next = None


class LinkedList:
    def __int__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def is_palindrome(self):
        slow_ptr = self.head
        fast_ptr = self.head

        ## find the middle of the linked list
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        ## reverse the second half of the linked list
        reversed_list = None
        while slow_ptr:
            next_node = slow_ptr.next
            slow_ptr.next = reversed_list
            reversed_list = slow_ptr
            slow_ptr = next_node

        ## check if the first and 2nd half are equal
        first_ptr = self.head
        second_ptr = reversed_list

        while first_ptr and second_ptr:
            if first_ptr.data != second_ptr.data:
                return False
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next

        return True


def check_reversed_list_for_palindrome():
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)

    print(linked_list.is_palindrome())
