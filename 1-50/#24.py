#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = guard = ListNode(0)
        guard.next = head

        try:
            while True:
                p0, p1, p2 = p1, p1.next, p1.next.next
                p0.next, p1.next, p2.next = p2, p2.next, p1
        except:
            return guard.next


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = guard = ListNode(0)
        guard.next = head

        while p1.next and p1.next.next:
            a, b = p1.next, p1.next.next
            p1.next, b.next, a.next = b, a, b.next
            #上面一定要写在一行里，不然报错
            # b.next = a
            # a.next = b.next
            p1 = a

        return guard.next