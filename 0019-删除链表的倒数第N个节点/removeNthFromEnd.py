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

def removeNthFromEnd_2(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        # 快指针first走到链表末尾，慢指针刚好走到倒数第n个节点
        while first:
            first = first.next
            second = second.next
        
        # 删除倒数第n个节点
        second.next = second.next.next
        return dummy.next
