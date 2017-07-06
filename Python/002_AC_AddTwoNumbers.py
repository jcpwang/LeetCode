# Author:   Jerry C. Wang <jcpwang@gmail.com>
# File:     AC_AddTwoNumbers.py

lass Solution(object):
    def addTwoNumbers(self, l1, l2):
        tmp = ListNode(0)
        head = tmp
        flag = 0

        while flag or l1 or l2:
            newNode = ListNode(flag)
            if l1:
                newNode.val += l1.val
                l1 = l1.next
            if l2:
                newNode.val += l2.val
                l2 = l2.next
            flag = newNode.val / 10
            newNode.val %= 10
            tmp.next = newNode
            tmp = tmp.next
        return head.next
