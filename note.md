# C++

## Interface

### List Interfaceにまとめられるもの

FIFOキューにおける add(x)、remove() を、それぞれ enqueue(x)、dequeue() と呼ぶ

Stack と呼ぶ場合は、add(x) と remove() のことを、それぞれ push(x) および pop() と呼ぶ。これにより LIFO と FIFO の取り出し規則を区別できる。

FIFO キューと LIFO キュー(スタック)を一般化した Deque というインターフェースもある。

Deque は双方向キューと呼ばれ、先頭と末尾を持った要素の列を表しており、先頭または末尾に要素を追加できる。
Deque における操作には、addFirst(x)、removeFirst()、addLast(x)、 removeLast()がある

### List Interface

1. size(): リストの長さ n を返す
2. get(i): xi の値を返す
3. set(i,x): xi の値を x にする
4. add(i,x): x を i 番め *2 として追加し、xi,...,xn−1 を後ろにずらす。
すなわち、j ∈ {i,...,n−1} について xj+1 = xj とし、n をひとつ増やし、xi = x とする
5. remove(i): xi を削除し、xi+1,...,xn−1 を前にずらす。
すなわち、j ∈ {i,...,n − 2} について xj = xj+1 とし、n をひとつ減らす


### USet Interface

USet インターフェースは、重複がなく順序付けられていない要素の集まりを表現する(USet の U は unordered の意味)。
USet インターフェースは数学における集合(set)のようなものだ。
USet には、n 個の互いに相異なる要素が含まれる。つまり、同じ要素が複数入っていることはない。
また、USet では要素の並び順は決まっていない。USet には以下の操作を実行できる。
size(): 集合の要素数nを返す
add(x): 集合の中にx=yを満たすyがなければxを加える。追加されたらtrueを返しされなければfalse
remove(x): 集合の中にx=yを満たすyがあれば取り除き、そのyを返す。なければnullを返す
find(x):  集合の中にx=yを満たすyがあればそのyを返す。なければnullを返す

## SSet Interface

SSet インターフェースは順序付けされた要素の集まりを表現する(SSet の S
は sorted の意味)。SSet には全順序集合の要素が入る。
全順序集合とは、任意の 2 つの要素 x と y について大小を比較できるような集合をいう。
SSet は、USet とまったく同じセマンティクスを持つ操作 size()、add(x)、remove(x) をサポートする。
USet と SSet の違いは find(x) にある。
find(x): 順序付けられた集合から x の位置を特定する。
すなわち y ≥ x を満たす最小の要素 y を見つける。もしそのような yが存在すればそれを返し、存在しないなら null を返す
