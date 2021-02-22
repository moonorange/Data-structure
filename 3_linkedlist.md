# Introduction

linked list is a linear data structure.
There are two types of linked list, singly linked list and doubly linked list.

## Singly linked list

Implementation is here
`code/singly_linked_list.py`

## Doubly Linked List

Advantages over singly linked list

```
1) A DLL can be traversed in both forward and backward direction.
2) The delete operation in DLL is more efficient if pointer to the node to be deleted is given.
3) We can quickly insert a new node before a given node.
In singly linked list, to delete a node, pointer to the previous node is needed. To get this previous node, sometimes the list is traversed. In DLL, we can get the previous node using previous pointer.
```

Disadvantages over singly linked list
```
1) Every node of DLL Require extra space for an previous pointer. It is possible to implement DLL with single pointer though (See [this](https://www.geeksforgeeks.org/xor-linked-list-a-memory-efficient-doubly-linked-list-set-1/)).
2) All operations require an extra pointer previous to be maintained. For example, in insertion, we need to modify previous pointers together with next pointers. For example in following functions for insertions at different positions, we need 1 or 2 extra steps to set previous pointer.
```

# 参考

C++構造体
https://atcoder.jp/contests/apg4b/tasks/APG4b_ab?lang=ja
