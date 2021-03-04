import sys
from pathlib import Path
sys.path.append(str(Path('__file__').resolve().parent))
from linked_list.utils import ListNode

# https://leetcode.com/problems/reverse-linked-list/
class Solution:
	def reverse_list(self, head: ListNode) -> ListNode:
		prev = None
		while (head):
			curr = head #1 2 3
			head = head.next #2→3　3→None None
			curr.next = prev #1→None　2→1→None　3→2→1→None
			prev = curr #1→None 2→1→None 3→2→1→None
		return prev

# last = ListNode(3)
# second = ListNode(2, last)
# first = ListNode(1, second)
# i = 1
# print("before operation")
# head = first
# while (head):
# 	print(f"{i}: {head.val}")
# 	head = head.next
# 	i += 1
# sol = Solution()
# ans = sol.reverse_list(first)
# i = 1
# print("after operation")
# while (ans):
# 	print(f"{i}: {ans.val}")
# 	ans = ans.next
# 	i += 1
