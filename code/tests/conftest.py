import pytest
import sys
from pathlib import Path
sys.path.append(str(Path('__file__').resolve().parent))
from linked_list.utils import ListNode

SAMPLE_LINKED_LISTS = [ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))), ListNode(10, ListNode(5, ListNode(14, ListNode(84, ListNode(3)))))]

@pytest.fixture(params=SAMPLE_LINKED_LISTS, scope="function")
def sample_linked_list(request):
	return request.param
