#!/usr/bin/env python
# -- coding: utf-8 --
"""
@AUTHOR : zlikun <zlikun-dev@hotmail.com>
@DATE   : 2019/03/01 17:03:55
@DESC   : 两数相加
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, m: ListNode, n: ListNode) -> ListNode:

        if not m:
            return n
        if not n:
            return m

        carry = 0
        head = ListNode(None)
        curr = head

        while m or n:
            t = carry
            if m:
                t += m.val
                m = m.next
            if n:
                t += n.val
                n = n.next

            curr.val = t % 10
            carry = t // 10

            node = ListNode(carry)
            if m or n or carry > 0:
                curr.next, curr = node, node

        return head


def traverse(head: "ListNode"):
    while head:
        print(head.val, end="\t")
        head = head.next
    print()


def test1():
    m = ListNode(2)
    m.next = ListNode(4)
    m.next.next = ListNode(3)
    traverse(m)

    n = ListNode(5)
    n.next = ListNode(6)
    n.next.next = ListNode(4)
    traverse(n)

    traverse(Solution().addTwoNumbers(m, n))


def test2():
    m = ListNode(5)
    traverse(m)
    n = ListNode(5)
    traverse(n)

    traverse(Solution().addTwoNumbers(m, n))


if __name__ == '__main__':
    test1()
    print('-' * 32)
    test2()
