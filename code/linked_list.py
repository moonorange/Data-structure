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
		if index < 0 or self.size <= index:
			print("invalid index")
			return 1
		return 0

	def get(self, index: int) -> int:
		"""
		Get the value of the index-th node in the linked list. If the index is invalid, return -1.
		"""
		if self.__is_invalid_index(index):
			return -1
		current = self.head
		for _ in range(index):
			current = current.next
		print(f"get {index}th object")
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
		if index < 0 or self.size < index:
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
		print(f"add {val} to {index}th place")
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
		print(f"delete {index}th val")
		self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
val = 5
obj.addAtHead(val)
print(f"head value is {obj.head.val}")
val = 1
obj.addAtTail(val)
tail_obj = obj.get(obj.size - 1)
print(f"tail_obj is {tail_obj.val}")
index = 1
obj.addAtIndex(index, 150)
print(f"1st value is {obj.head.next.val}")
obj.deleteAtIndex(index)
print(f"1st value after delete is {obj.head.next.val}")
