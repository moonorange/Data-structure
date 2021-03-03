import pytest
import sys
from linked_list.reverse.reverse_linked_list import Solution
from linked_list.utils import ListNode

solution_obj = Solution()
REVERSED_ORDER = [ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))), ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), ListNode(3, ListNode(84, ListNode(14, ListNode(5, ListNode(10)))))]

idx = 0

class TestReverseListSolution:
	def test_reverse_list(self, sample_linked_list):
		global idx
		reversed_list = solution_obj.reverse_list(sample_linked_list)
		each_list = REVERSED_ORDER[idx]
		while (each_list):
			assert reversed_list.val == each_list.val
			reversed_list = reversed_list.next
			each_list = each_list.next
		idx += 1
