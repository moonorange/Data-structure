# https: // leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/

"""
Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Each value on each linked list is in the range[1, 10 ^ 9].
Your code should preferably run in O(n) time and use only O(1) memory.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# The first brute force O(N**2) ans
	def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
		curr_a = headA
		while (curr_a):
			curr_b = headB
			while (curr_b):
				if (curr_a == curr_b):
					return curr_a
				curr_b = curr_b.next
			curr_a = curr_a.next
		return None

	# The solution
	def	getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
		ptr_a = headA
		ptr_b = headB
		while (ptr_a is not ptr_b):
			ptr_a = headB if ptr_a is None else ptr_a.next
			ptr_b = headA if ptr_b is None else ptr_b.next
		return ptr_a
