# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
使用两个指针解决问题
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = cur = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        if length == n:
            return head.next
        else:
            for i in range(1, length-n):
                cur = cur.next
            cur.next = cur.next.next
        return head
