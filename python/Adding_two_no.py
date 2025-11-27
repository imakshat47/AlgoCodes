class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# function to reverse the linked list
def reverse(head):
    prev = None
    curr = head

    while curr is not None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    return prev

# function to trim leading zeros in linked list
def trimLeadingZeros(head):
    while head and head.data == 0:
        head = head.next
    return head

# Function to add two numbers represented by linked list
def addTwoLists(num1, num2):
    res = None
    curr = None
    carry = 0

    num1 = trimLeadingZeros(num1)
    num2 = trimLeadingZeros(num2)
    
    num1 = reverse(num1)
    num2 = reverse(num2)

    # Iterate till either num1 is not empty or num2 is
    # not empty or carry is greater than 0
    while num1 is not None or num2 is not None or carry != 0:
        sumValue = carry

        if num1 is not None:
            sumValue += num1.data
            num1 = num1.next

        if num2 is not None:
            sumValue += num2.data
            num2 = num2.next
        
        newNode = Node(sumValue % 10)

        carry = sumValue // 10

        # If this is the first node, then make this node
        # as the head of the resultant linked list
        if res is None:
            res = newNode
            curr = newNode
        else:
            # Append new node to resultant linked list
            # and move to the next node
            curr.next = newNode
            curr = curr.next

    return reverse(res)

def printList(head):
    curr = head
    while curr is not None:
        print(curr.data, end="")
        if curr.next != None:
            print(" -> ", end="")
        curr = curr.next
    print()

if __name__ == "__main__":
    
    num1 = Node(1)
    num1.next = Node(2)
    num1.next.next = Node(3)

    num2 = Node(9)
    num2.next = Node(9)
    num2.next.next = Node(9)

    sumList = addTwoLists(num1, num2)
    printList(sumList)
