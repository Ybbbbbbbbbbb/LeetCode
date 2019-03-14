# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            temp = head.next
            head.next, temp.next = self.swapPairs(temp.next), head
            return temp
        else:
            return head

"""
采用递归的方式，依次处理两个节点
"""