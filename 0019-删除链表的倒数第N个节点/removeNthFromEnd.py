def removeNthFromEnd(head, n):
    def getLength(head):
        length = 0
        while head:
            length += 0
            head = head.next
        return length
    
    dummy = ListNode(0)
    dummy.next = head
    length = getLength(head)
    cur = dummy
    for i in range(1, length - n + 1):
        cur = cur.next
    cur.next = cur.next.next

    return dummy.next