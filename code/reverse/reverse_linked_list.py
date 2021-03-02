class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# https://leetcode.com/problems/reverse-linked-list/
class Solution:
	def reverseList(self, head: ListNode) -> ListNode:
		prev = None
		while (head):
			curr = head
			print(f"curr: {curr.val}")
			head = head.next
			print(f"head: {head.val}") if head else print(f"head: {head}")
			curr.next = prev
			print(f"curr.next: {curr.next.val}") if curr.next else print(f"curr.next: {curr.next}")
			prev = curr
		return prev


obj = ListNode(23, ListNode(6, ListNode(15)))
sol = Solution()
ans = sol.reverseList(obj)
i = 1
while (ans):
	print(f"{i}: {ans.val}")
	ans = ans.next
	i += 1
