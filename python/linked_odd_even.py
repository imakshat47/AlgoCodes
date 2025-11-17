def segregateEvenOdd(head):

    evenStart = evenEnd = None
    oddStart = oddEnd = None

    curr = head

    while curr:
        next_node = curr.next  # Save next
        curr.next = None       # Disconnect node

        if curr.data % 2 == 0:    # Even node
            if evenStart is None:
                evenStart = evenEnd = curr
            else:
                evenEnd.next = curr
                evenEnd = curr
        else:                     # Odd node
            if oddStart is None:
                oddStart = oddEnd = curr
            else:
                oddEnd.next = curr
                oddEnd = curr

        curr = next_node

    # If no even nodes, return odd list
    if evenStart is None:
        return oddStart

    # Append odd list after even list
    evenEnd.next = oddStart

    return evenStart
