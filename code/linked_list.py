#desgin linked list https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/
import sys

class Node:
	def __init__(self, val):
		"""
		Node object
		"""
		self.val: int = val
		self.next: Node = None

class MyLinkedList:
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.head: Node = None
		self.size = 0

	def __is_invalid_index(self, index: int) -> None:
		if index < 0 or len(self.size) <= index:
			print("invalid index")
			return 1
		return 0

	def get(self, index: int) -> int:
		"""
		Get the value of the index-th node in the linked list. If the index is invalid, return -1.
		"""
		if __is_invalid_index(index):
			return -1
		current = self.head
		for _ in range(index):
			current = current.next
		return current

	def addAtHead(self, val: int) -> None:
		"""
		Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
		"""
		self.addAtIndex(0, val)


	def addAtTail(self, val: int) -> None:
		"""
		Append a node of value val to the last element of the linked list.
		"""
		self.addAtIndex(self.size, val)

	def addAtIndex(self, index: int, val: int) -> None:
		"""
		Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
		"""
		if index < 0 or len(self.size) < index:
			print("invalid index")
			sys.exit(0)

		current = self.head
		new_node = Node(val)

		if index == 0:
			new_node.next = current
			self.head = new_node
		else:
			for _ in range(index - 1):
				current = current.next
			new_node.next = current.next
			current.next = new_node

		self.size += 1

	def deleteAtIndex(self, index: int) -> None:
		"""
		Delete the index-th node in the linked list, if the index is valid.
		"""
		if self.__is_invalid_index(index):
			sys.exit(0)

		current = self.head
		for _ in range(index - 1):
			current = current.next
		current.next = current.next.next
		self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
