# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
#         nodes_seen=set()
        
#         current = head
        
#         while current is not None:
#             if current in nodes_seen:
#                 return True
#             nodes_seen.add(current)
#             current=current.next
#         return False

        if head is None:
            return False
        slow=head
        fast=head.next
        while slow!=fast:
            if fast is None or fast.next is None:
                return False
            slow=slow.next
            fast=fast.next.next
        return True
