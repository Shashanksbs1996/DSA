# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self,head,val):
        if not head:
            return head
        if head.val == val:
            return self.removeElements(head.next, val)
        else:
          next_el=  self.removeElements(head.next, val)
          head.next=next_el
        return head
    
       