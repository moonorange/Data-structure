# Introduction

linked list is a linear data structure.
There are two types of linked list, singly linked list and doubly linked list.

## Singly linked list

メンバ初期化子リスト使っているサンプルプログラム
```c++
struct SinglyListNode {
  int val;
  SinglyListNode *next;
  SinglyListNode(int x):val(x), next(NULL) {}　// コンストラクタ。{}内での処理は代入処理であり厳密には初期化処理ではない
};


# 参考

C++構造体
https://atcoder.jp/contests/apg4b/tasks/APG4b_ab?lang=ja
