# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/

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
