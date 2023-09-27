from linked_list import LinkedList
from print_list import print_list_with_forward_arrow


def get_middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def driver_get_middle_node():
    input_array = (
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
        [3, 2, 1],
        [10],
        [1, 2],
        [10, 20, 30, 40, 50, 55 , 60, 65, 70, 75, 80, 90, 100]
    )

    for i in range(len(input_array)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input_array[i])
        print(i+1, "\t.Linked List: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tMiddle of the linked list : ",
              get_middle_node(input_linked_list.head).data
              )
        print("-"*100, "\n")
