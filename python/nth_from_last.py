class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def nth_from_end(head, N):
    main_ptr = head
    ref_ptr = head

    for _ in range(1, N):
        ref_ptr = ref_ptr.next
        if ref_ptr is None:
            return -1

    while ref_ptr.next is not None:
        ref_ptr = ref_ptr.next
        main_ptr = main_ptr.next

    return main_ptr.data

if __name__ == "__main__":
    head = Node(35)
    head.next = Node(15)
    head.next.next = Node(4)
    head.next.next.next = Node(20)

    print(nth_from_end(head, 4))
