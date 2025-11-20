class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def delete_occurrences(head, key):
    curr = head
    prev = None

    while curr is not None:
        if curr.data == key:
            if prev is None:
                head = curr.next
            else:
                prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next

    return head

def print_list(curr):
    while curr is not None:
        print(f" {curr.data}", end="")
        curr = curr.next
    print()

if __name__ == "__main__":
    head = Node(2)
    head.next = Node(2)
    head.next.next = Node(1)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(2)

    key = 2
    head = delete_occurrences(head, key)
    print_list(head)
