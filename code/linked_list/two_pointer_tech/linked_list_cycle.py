# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution:
	def detectCycle(self, head: ListNode) -> ListNode:
		index = 0
		curr = head
		node_dict = {}
		while (curr):
			if (curr in node_dict):
				print(f"tail connects to node index {node_dict.get(curr)}")
				return curr
			node_dict.setdefault(curr, index)
			curr = curr.next
			index += 1
		print("no cycle")
		return None

	#O(1) memory
	def hasCycle(self, head: ListNode) -> bool:
		walker = head
		runner = head
		while runner and runner.next:
			walker = walker.next
			runner = runner.next.next
			if (walker == runner): return True
		return False
