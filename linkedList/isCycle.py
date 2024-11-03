# Used hashset to solve https://leetcode.com/problems/linked-list-cycle/
# space complexity O(n)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: # type: ignore
        if head == None: return False
        visited = {}
        curr = head
        while curr.next:
            if curr in visited.keys(): return True
            visited[curr] = True
            curr = curr.next
        return False

# Using the Floyd's tortoise and Hare algorithm where one point moves slow (one step) and another one moves faster (two steps)
# https://leetcode.com/problems/linked-list-cycle/
# space complexity O(1)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: # type: ignore 
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False