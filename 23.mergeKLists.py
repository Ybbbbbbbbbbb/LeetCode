# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        result = head = ListNode(0) 
        while lists:
            l = len(lists)
            temp = -1
            flag = 100000
            for i in range(l):
                if lists[i]:
                    if lists[i].val < temp:
                        temp = lists[i].val
                        flag = i
                    else:
                        continue
            head.next =  lists[flag]
            head = head.next
            lists[flag] = lists[flag].next
        return result.next

        
if __name__ == "__main__":
    s = Solution()
    result = s.mergeKLists([[1,4,5],[1,3,4],[2,6]])
    print(result)               