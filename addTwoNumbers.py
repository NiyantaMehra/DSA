# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_1 = ""
        while l1:
            list_1 += str(l1.val)
            l1 = l1.next
        list_1 = list_1[::-1]
        
        list_2 = ""
        while l2:
            list_2 += str(l2.val)
            l2 = l2.next
        list_2 = list_2[::-1]
        
        ans = str(int(list_1)+int(list_2))
        ans = ans[::-1]
        result = dummy = ListNode(0)
        for ele in ans:
            # node = ListNode(ele)
            #next needs to be a node not an element
            dummy.next = ListNode(ele)
            dummy = dummy.next 
        
        return result.next
    