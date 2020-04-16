# Tree

<br>

<br>

## Tree의 개념

- 비선형 구조

- 원소들 간에 `1 : n 관계`를 가지는 자료구조

- `계층형` 자료구소

  - OS의 폴더 구조
  - **포함관계**를 표현할 때 Tree로 표현하면 용이

- 상위 원소에서 하위 원소로 내려가면서 확장되는 `Tree 형태`의 구조

  s<br>

<br>

## Tree의 정의

- 한 개 이상의 `node`로 이루어진 유한 집합이며, 다음 조건을 만족한다
  - node 중 최상위 node를 `root`라고 한다
  - 나머지 node들은 n(>=0)개의 분리집합 T1,....,Tn으로 분리될 수 있다
- 이들 **T1,...,Tn**은 각각 하나의 `tree`가 되며 (재귀적 정의), root의 `subtree`라 한다

<br>

<br>

## Tree 용어 정리

<br>

### Node

- Tree의 원소

<br>

### 간선 (edge)

- node를 연결하는 선
- 부모 node와 자식 node를 연결

<br>

### Root node

- Tree의 시작 node

<br>

### 형제 노드 (sibiling node)

- 같은 부모 node의 자식 node들

<br>

### 조상 노드

- 간선을 따라 root node까지 이르는 경로에 있는 모든 node들

<br>

### Subtree

- 부모 node와 연결된 간선을 끊었을 때 생성되는 tree

<br>

### 자손 node

- subtree에 있는 하위 level의 node들

<br>

### 차수 (degree)

- node의 차수
  - node에 연결된 자식 node의 수
- tree의 차수
  - tree에 있는 node의 차수 중에서 가장 큰 값
- 단말 node (leaf node)
  - 차수가 0인 node
  - 자식 node가 없는 node

<br>

### 높이

- node의 높이
  - root에서 node에 이르는 간선의 수
  - node의 level
- tree의 높이
  - tree에 있는 node의 높이 중에서 가장 큰 값
  - 최대 level

<br>

<br>

## Tree의 특성

- 그래프 / 연결 컴포넌트 (connected component)
  - 임의의 두 node 사이에  유일한 경로가 존재
- Cycle이 없다
  - node 수 = 간선수 +1

<br>

<br>

## 이진 트리 (Binary Tree)

- 모든 node들이 2개의 subtree를 갖는 특별한 형태의 tree
- 각 node가 자식 node를 최대한 2개까지만 가질 수 있는 tree
  - left child node
  - right child node

<br>

<br>

## 이진 트리 특성

- level i에서의 node의 최대 개수는 2개
- 높이가 h인 이진 tree가 가질 수 있는 node의 
  - 최소 개수는 `h+1` 개
  - 최대 개수는 `2^(h+1) -1` 개

<br>

<br>

## 이진 트리 종류

<br>

### 포화 이진 트리 (Full Binary Tree)

- 모든 level에 node가 포화상태로 차 있는 이진 트리
- 높이가 h 일 때, 최대의 노드 개수인 `2^(h+1) -1` 의 node를 가진 binary tree
  - ex) 높이 3일때 2^(3+1) -1 =15개의 node
- root를 1번으로 하여 `2^(h+1) -1` 까지 정해진 위치에 대한 node 번호를 가짐

<br>

### 완전 이진 트리 (Complete Binary Tree)

- 높이가 h이고 node수가 n개 일 때, (단, h+1 <= n < 2^(h+1) -1), 포화 이진 트리의 node 번호 1번부터 n번까지 빈 자리가 없는 이진 트리
- 배열로 구현하기 용이하다!

<br>

### 편향 이진 트리 (Skewed Binary Tree)

- 높이 h에 대한 최소 개수의 node를 가지면서 한쪽 방향의 자식 node만을 가진 이진 tree
  - left skewed binary tree
  - right skewed binary tree
- linked list와 차이 없음...안좋은 구조

<br>

<br>

## 이진 트리 - 순회 (traversal)

- 순회란 tree의 각 node를 중복되지 않게 전부 방문(visit) 하는 것을 말하는데, tree는 비 선형 구조이기 때문에 선형구조에서와 같이 선후 연결 관계를 알 수 없다
  - 그래서 특별한 방법이 필요하다!

<br>

### 3가지 기본적인 순회 방법

1. 전위 순회 (preorder traversal)

   - VLR
   - 부모 노드 방문 후, 자식노드를 좌, 우 순서로 방문

2. 중위 순회 (inorder traversal)

   - VRL

   - 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문

3. 후위 순회 (postorder traversal)

   - LRV

   - 자식 노드를 왼쪽, 오른쪽 순서로 방문, 부모 노드 방문