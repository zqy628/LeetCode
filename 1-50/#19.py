#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    #Two pass algorithm
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # used to simplify some corner cases such as a list with only one node, or removing the head of the list.
        first = ListNode(0)
        first.next = head
        p = head
        lenth = 0
        while p:
            lenth += 1
            p = p.next
        j = 1
        p_ = first
        while j < lenth-n+1:
            p_ = p_.next
            j += 1
        p_.next = p_.next.next
        return first.next
    #Two pass algorithm 用两个结点，第一个结点领先第二个n位
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = ListNode(0)
        l.next = head
        first = l.next
        second = l.next
        for i in range(n):
            first = first.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return l


