#desgin linked list https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/
#SInfly Linked List
class Node(object):
    def __init__(self, val):
		self.val: int = val
		self.prev: Node = None
		self.next: Node = None

class DoublyLinkedList:
    def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.head: Node = None
		self.tail: Node = None
		self.size: int = 0

    def get(self, index: int) -> int:
		"""
		Get the value of the index-th node in the linked list. If the index is invalid, return -1.
		"""
		if index < 0 or index >= self.size:
			return - 1
		current = self.head
		for _ in range(index):
			current = current.next
		return current.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion,           the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the         length of linked list, the node will be appended to the end of linked list. If index is             greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return

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
        if index < 0 or index >= self.size:
            return

        current = self.head
        if index == 0:
            self.head = current.next
        else:
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1


# Your DoublyLinkedList object will be instantiated and called as such:
obj = DoublyLinkedList()
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
obj.addAtIndex(obj.size + 1, 150)
obj.deleteAtIndex(obj.size)
