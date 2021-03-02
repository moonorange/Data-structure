# https: // leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		tmp = curr = head
		size = 0
		while (tmp):
			tmp = tmp.next
			size += 1
		if (size - n <= 0):
			return head.next
		for _ in range(size - n - 1):
			curr = curr.next
		curr.next = curr.next.next
		return head

	def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
		fast = slow = head
		for _ in range(n):
			fast = fast.next
		if (fast is None):
			return head.next
		while fast.next:
			fast = fast.next
			slow = slow.next
		slow.next = slow.next.next
		return head
