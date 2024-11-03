# Used below 4 steps to solve the problem https://leetcode.com/problems/reorder-list/
# 1. find the middle point by slow and fast pointer (slow moves by 1 and fast moves by 2)
# 2. once fast reaches last slow is in middle , slow.next is the start of second list ! split the list in two list
# 3. reverse the link of the second list
# 4. merge two lists

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None: # type: ignore
        """
        Do not return anything, modify head in-place instead.
        """
        # find second
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # start of second    
        second = slow.next
        # breaks the link from first list
        prev = slow.next = None
        # reverses the link
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge two list [1] -> [2] -> [3] and [5] -> [4] -> None
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2