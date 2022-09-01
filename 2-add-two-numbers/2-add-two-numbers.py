# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry =0
        ans = p = ListNode(123)
        while l1 or l2:
            l1data,l2data = l1.val if l1 else 0,l2.val if l2 else 0 
            k= l1data +l2data+carry
            carry = k//10
            p.next =ListNode(k%10)
            p,l1,l2 = p.next,l1.next if l1 else l1,l2.next if l2 else l2
        if carry:
            p.next=ListNode(carry)
        return ans.next
        
        