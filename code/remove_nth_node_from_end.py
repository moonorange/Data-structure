# https: // leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		curr = head
		size = 0
		while (curr):
			curr = curr.next
			size += 1
		curr = head
		if (size - n <= 0):
			head = head.next
			return head
		for _ in range(size - n - 1):
			curr = curr.next
		curr.next = curr.next.next
		return
