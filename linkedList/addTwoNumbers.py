# Used a new linkedList to add values with carry https://leetcode.com/problems/add-two-numbers/

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        dummy = ListNode() # type: ignore
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            # get the added value
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            
            # put carry if needed and insert new node in our net LL
            carry = val // 10
            val = val%10
            curr.next = ListNode(val) # type: ignore

            # update pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
