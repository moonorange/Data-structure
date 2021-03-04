# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/
from linked_list.utils import ListNode

class Solution:
	def removeElements(self, head: ListNode, val: int) -> ListNode:
		while (head and head.val == val):
			head = head.next
		if (head is None):
			return head
		head_tmp = head
		while (head.next):
			if (head.next.val == val):
				head.next = head.next.next
			else:
				head = head.next
		return head_tmp

	def removeElements_2(self, head: ListNode, val: int) -> ListNode:
		dummy_head = ListNode(-1)
		dummy_head.next =  head
		tmp_head = dummy_head
		while (dummy_head.next):
			if (dummy_head.next.val == val):
				dummy_head.next = dummy_head.next.next
			else:
				dummy_head = dummy_head.next
		return tmp_head.next
