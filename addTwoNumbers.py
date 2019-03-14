# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n = result = ListNode(0)
        middle = 0
        while l1 or l2 or middle:
            temp_1 = temp_2 = 0
            if l1:
                temp_1 = l1.val
                l1 = l1.next
            if l2:
                temp_2 = l2.val
                l2 = l2.next
            middle, b = divmod(temp_1 + temp_2 + middle, 10)
            n.next = ListNode(b)
            n = n.next
        return result

if __name__ == "__main__":
    test = Solution()
    result = test.addTwoNumbers()


        