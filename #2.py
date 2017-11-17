#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
#链表定义
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#用了列表写，要用链表写
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len_l1 = len(l1)
        len_l2 = len(l2)
        index = 0
        carry = 0
        s = []
        while index < len_l1 or index < len_l2:
            if index >= len_l1:
                l1.append(0)
            if index >= len_l2:
                l2.append(0)
            sum = l1[index] + l2[index] + carry
            if sum >= 10:
                s.append(sum-10)
                carry = 1
            else:
                s.append(sum)
                carry = 0
            index += 1
        if carry == 1:
            s.append(1)
        return s

#链表写法
class Solution1:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        ans1 = ans = ListNode(0)
        while l1 or l2:
            if l1:
                v1 = l1.val
                l1 = l1.next
            else:
                v1 = 0
            if l2:
                v2 = l2.val
                l2 = l2.next
            else:
                v2 = 0
            sum = v1 + v2 + carry
            #这个判断结构可以改写
            # if sum >= 10:
            #     ans.next = ListNode(sum-10)
            #     carry = 1
            # else:
            #     ans.next = ListNode(sum)
            #     carry = 0
            sum = v1 + v2 + carry
            ans.next = ListNode(sum % 10)
            ans = ans.next
        if carry == 1:
            ans.next = ListNode(1)
        a = ListNode(6)
        a.next = ans1
        return ans1.next

s = Solution()
print(s.addTwoNumbers([2,4,3],[5,6,4]))