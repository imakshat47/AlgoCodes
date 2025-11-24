class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def removeLoop(head):
    if head is None or head.next is None:
        return

    slow = head
    fast = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head

            while slow != fast:
                slow = slow.next
                fast = fast.next

            while fast.next != slow:
                fast = fast.next
            fast.next = None  

def printList(curr):
    while curr:
        print(curr.data, end=' ')
        curr = curr.next
    print()

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = head.next

    removeLoop(head)

    printList(head)
