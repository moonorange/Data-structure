# 実行時間

最悪実行時間(worst-case running time):
実行時間に対する保証の中で、最も強力なもの。
あるデータ構造の操作について最悪実行時間が f (n)であるといったら、そのような操作の実行時間が f (n) より長くなることは決してない。

償却実行時間(amortized running time):
償却実行時間が f (n) であるとは、典型的な操作にかかるコストが f (n) を超えないことを意味する。
より正確には、m 個の操作にかかる実行時間を合計しても、mf (n) を超えないことを意味する。
いくつかの操作には f (n) より長い時間がかかるかもしれないが、操作の列全体として考えれば、1 つあたりの実行時間は f (n) という意味だ。

期待実行時間(expected running time):
期待実行時間が f (n) であるとは、実行時間が確率変数(1.3.4 節を参照)であり、その確率変数の期待値が f (n) であることを意味する。
この期待値を計算する際に考えるランダム性は、そのデータ構造内で起こる選択におけるランダム性である。

### 減価償却とは?

固定資産を使用可能期間にしたがって、少しずつ費用を計上すること

# Interface

## List Interfaceにまとめられるもの

FIFOキューにおける add(x)、remove() を、それぞれ enqueue(x)、dequeue() と呼ぶ

Stack と呼ぶ場合は、add(x) と remove() のことを、それぞれ push(x) および pop() と呼ぶ。これにより LIFO と FIFO の取り出し規則を区別できる。

FIFO キューと LIFO キュー(スタック)を一般化した Deque というインターフェースもある。

Deque は双方向キューと呼ばれ、先頭と末尾を持った要素の列を表しており、先頭または末尾に要素を追加できる。
Deque における操作には、addFirst(x)、removeFirst()、addLast(x)、 removeLast()がある

## List Interface

1. size(): リストの長さ n を返す
2. get(i): xi の値を返す
3. set(i,x): xi の値を x にする
4. add(i,x): x を i 番め *2 として追加し、xi,...,xn−1 を後ろにずらす。
すなわち、j ∈ {i,...,n−1} について xj+1 = xj とし、n をひとつ増やし、xi = x とする
5. remove(i): xi を削除し、xi+1,...,xn−1 を前にずらす。
すなわち、j ∈ {i,...,n − 2} について xj = xj+1 とし、n をひとつ減らす


## USet Interface

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


# 配列を使ったリスト
C++ のふつうの配列は要素数を保持していないので、要素数を保持する配列のクラス array を定義する

(Page 28).

## ArrayStack

```c++
void add(int i, T x) {
   if (n + 1 >= a.length) resize();
   for (int j = n; j > i; j--)
    a[j] = a[j - 1];
  a[i] = x;
  n++;
  }
```
(Page 30).

resize()のコストを無視すれば、add(i,x) のコストは x を入れる場所を作るために右にシフトする要素数に比例する。
つまり、この操作の（resize() のコストを無視した）実行時間は、O(n − i) である。

(Page 30).

remove(i) も同様に実装できる。a[i + 1],...,a[n − 1] を左に 1 つシフトし、 n の値を 1 つ小さくする。
a.length() >= 3nだった場合resize()を読んでaを小さくする
計算量はresize()を無視すれば同様にO(n-i)である

- 配列では任意の要素に一定の時間でアクセスできる。そのため、get(i)操作と set(i,x) 操作を定数時間で実行できる

- 配列はそれほど動的ではない。リストの中ほどに要素を追加、削除するには、隙間を作ったり埋めたりするため、配列に含まれる多くの要素を移動させる必要がある。
add(i,x) 操作と remove(i) 操作の実行時間がn と i に依存するのは、これが原因である

- 配列は伸び縮みしない。backing array のサイズより多くの要素をデータ構造に入れるには、新しい配列を割り当てて古い配列の要素をそちらにコピーしなければならず、この操作のコストは大きい

resize() の実装は単純。大きさ 2n の新しい配列 b を割り当て、n 個の a の 要素を b の先頭の n 個としてコピーする。そして a を b に置き換える。よって、resize() の呼び出し後は a.length = 2n が成り立つ
大きさ 2n の配列 b を割り当て、 n 個の要素をコピーする。これには O(n) の時間がかかる。
```c++
void resize() {
   array<T> b(max(2 * n, 1));
   for (int i = 0; i < n; i++)
    b[i] = a[i];
   a = b;
    }
```

(Page 32).

### 要約

次の定理は ArrayStack の性能について整理したものだ。
定理 2.1. ArrayStack は List インターフェースを実装する。
resize() にかかる時間を無視した場合の ArrayStack における各操作の実行時間を以下にまとめる。
- get(i) および set(i,x) の実行時間は O(1) である
- add(i,x) および remove(i) の実行時間は O(1 + n − i) である
空の ArrayStack に対して任意の m 個の add(i,x) および remove(i) からなる操作の列を実行する。
このとき resize() にかかる時間の合計は O(m) である。

ArrayStack というデータ構造は、Stack インターフェースを実装する効率的な方法である。
特に、push(x) は add(n,x) に相当し、pop() は remove(n − 1)に相当する。
これらいずれの操作の償却実行時間も O(1) である。

## FastArrayStack

FastArrayStack：最適化された ArrayStackである。
ArrayStack で主にやっていることは、（add(i,x) と remove(i) のため に）データをシフトすることと、（resize() のために）データをコピ-することである。
実装では、これに for ループを使った。しかし実際には、データのシフトやコピーに特化したもっと効率的な機能が使える。
C++ には、std::copy(a0,a1,b) アルゴリズムがある。

## ArrayQueue

このデータ構造では、（add(x) によって）追加された要素が、同じ順番で（remove() によって）削除される。
(Page 35).

仮に無限長の配列aがあればFIFOを簡単に実装できる。
次に削除する要素を追跡するインデックス j と、キューの要素 数 n を記録しておく。そうすれば、キューの要素は以下の場所に入っている

```c++
a[j],a[j + 1],...,a[j + n − 1]
```

剰余算術は無限長の配列を模倣するのに便利である。i mod a.length が常 に 0,...,a.length − 1 の値を取ることを利用して、配列の中にキューの要素を うまく入れられるのだ。

```c++
a[j%a.length],a[(j + 1)%a.length],...,a[(j + n − 1)%a.length]
```

ここでは a を循環配列として使っている。配列の添字が a.length − 1 を超え ると、配列の先頭に戻ってくるわけである。
(Page 36).

### 要約

ArrayQueue は、（FIFO の）Queue インターフェースの実装であ る。resize() のコストを無視すると、ArrayQueue は add(x)、remove() の実 行時間は O(1) である。さらに、空の ArrayQueue に対して長さ m の任意の add(x) および remove() からなる操作の列を実行するとき、resize() にかかる時間の合計は O(m) である。
(Page 39).

## ArrayDeque：配列を使った高速な双方向キュー

両端に対して追加と削除が効率よくできるデータ構造
ArrayDeque に 対 す る get(i) と set(i,x) は 簡 単 だ 。配 列 の 要 素 a[(j + i) mod a.length] を読み書きすればよい。

```c++
void add(int i, T x) {
  if (n + 1 >= a.length) resize();
  if (i < n/2) { // a[0],..,a[i-1] を左に 1 つずらす
    j = (j == 0) ? a.length - 1 : j - 1;
    for (int k = 0; k <= i-1; k++)
      a[(j+k)%a.length] = a[(j+k+1)%a.length];
} else { // a[i],..,a[n-1] を右に 1 つずらす
    for (int k = n; k > i; k--)
      a[(j+k)%a.length] = a[(j+k-1)%a.length];
    }

  a[(j+i)%a.length] = x; n++; }
```

このように要素をずらせば、add(i,x) によって移動する要素の数が高々 min{i,n − i} 個に保証される。そのため、add(i,x) の実行時間は、resize() を無視すれば O(1 + min{i,n − i}) である。 remove(i) も同様に実装できる。i < n/2 かどうかに応じて、左から i 個の要素をいずれも 1 つずつ右にシフトするか、右から n − i − 1 個の要 素をいずれも 1 つずつ左にシフトする。remove(i) の実行時間も、やはり O(1 + min{i,n − i}) である。

(Page 41).

### 要約

resizeの実行時間を無視すれば

- get(i) および set(i,x) の実行時間は O(1) である
- add(i,x) および remove(i) の実行時間は O(1+min{i,n−i}) である

(Page 42).


## DualArrayDeque：2 つのスタックから作った双方向 キュー

DualArray dequeでは front と back という名前の 2 つの ArrayStack を背中合わせに配置 する。

```c++
ArrayStack<T> front;
ArrayStack<T> back;
```

DualArrayDeque では、要素数 n を明示的に保持しない。要素数は n = front.size() + back.size() により求められる。

要素の追加
```c++
void add(int i, T x) {
   if (i < front.size()) {
     front.add(front.size() - i, x);
     } else {
        back.add(i - front.size(), x);
    }
    balance();
}
```

でbalance() のコストを無視した add(i,x) の実行時間を求める。 i < front.size() のときは、add(i,x) により front.add(front.size() − i,x) が実行されるだけである。front は ArrayStack なので、この実行時間は次のようになる。
` O(front.size() − (front.size() − i) + 1) = O(1 + i)`

一方、i ≥ front.size() のときには、add(i,x) により back.add(i − front.size(),x) が実行されるだけである。
このときの実行時間は次のようになる。
`O(back.size() − (i − front.size()) + 1) = O(1 + n − i)`
(Page 45).

balance() のおかげで front.size() と back.size() の差が三倍より大きくなることはない(size() < 2 の場合を除く。
具体的には、balance() により、 3*front.size() ≥ back.size() かつ 3*back.size() ≥ front.size() であることが保証される。

resize() と balance() のコストを無視すると、DualArrayDeque における各操作の実行時間は次のようになる。
- get(i) および set(i,x) の実行時間は O(1) である
- add(i,x) および remove(i) の実行時間は O(1 + min{i,n − i}) である
また、空の DualArrayDeque に対して長さ m の任意の add(i,x) および remove(i) からなる操作の列を実行するとき、resize() にかかる時間の合 計は O(m) である。
(Page 48).