# Linked list

<br>

<br>

## Python List

- 순서를 가진 data의 묶음
  - 같은 data 중복 저장 가능
- `Sequence` 자료형
  - indexing, slicing, operator, method 사용 가능
- 크기 제한 없음
- Type 제한 없음

<br>

<br>

### List 복사

- 여러 가지 방법으로 리스트 복사
- 수행시간의 차이가 있고, 의미가 다른 항목 존재

<br>

| Code                                              | Description                                                  |
| ------------------------------------------------- | ------------------------------------------------------------ |
| new_list = old_list                               | `주소`의 복사<br>얕은 복사                                   |
| new_list = old_list[:]                            | `Slicing` <br>깊은 복사                                      |
| new_list = [] <br>new_list.extend(old_list)       | `extend()` : list를 추가하는 함수<br>깊은 복사               |
| new_list = list(old_list)                         | `list()`<br>깊은 복사                                        |
| import copy<br>new_list = copy.copy(old_list)     | `copy` 활용<br>깊은 복사                                     |
| new_list = [ i for i in old_list ]                | `List comprehension`<br>깊은 복사                            |
| import copy<br>new_list = copy.deepcopy(old_list) | `deepcopy` 활용<br>List 원소까지도 깊은 복사<br>가장 느림<br>깊은 복사 |

<br><br>

## 순차 리스트 

- 구현 방법

  - 1차원 배열에 항목들을 순서대로 저장한다
  - 데이터의 종류와 구조에 따라 구조화된 자료구조를 만들어 배열로 만들 수도 있다

- 초기화 및 생성

  - 변수에 값을 초기화하는 것으로 리스트 생성

- 데이터 접근

  - 배열의 `index` 를 이용해 원하는 위치의 data에 접근해 data를 변경하고 참조 할 수 있다

- 삽입 연산

  - 삽입 위치 다음의 항목들을 **이동**해야 한다

  - 파이썬에서 다음의 함수들의 내부에서 삽입 연산이 일어남

    - 항목들을 이동하는데 추가적인 연산 (비용)이 발생! - **단점**

    ```python
    insert()
    pop()
    ```

    

- 삭제 연산

  - 삭제 위치 다음의 항목들을 이동해야 한다 - **단점**

- 문제점

  - 자료의 *삽입/삭제* 연산 과정에서 연속적인 메모리 배열을 위해 원소들을 이동시키는 작업이 필요
  - 원소의 개수가 많고 *삽입/삭제* 연산이 빈번하게 일어날수록 작업에 소요되는 시간이 크게 증가함

<br>

<br>

## 연결 리스트 (Linked List)

> List의 단점을 보완한 자료 구조

- 자료의 논리적인 순서와 memory상의 물리적인 순서가 일치하지 않고, 

  **개별적으로 위치**하고 있는 원소의 주소를 연결하여 하나의 전체적인 자료구조를 이룸

- `link`를 통해 원소에 접근하므로, 순차 리스트에서처럼 **물리적인 순서**를 맞추기 위한 작업이 필요하지 않다

- 자료구조의 크기를 **동적**으로 조정할 수 있어, memory의 효율적인 사용이 가능하다 - **장점**

- 탐색 - **순차 탐색**

<br>

### Node

- `Linked list`에서 하나의 원소에 필요한 data를 갖고있는 자료 단위
  - 구성 요소
    1. #### data field
       
       - 원소의 `값`을 저장하는 자료구조
       - 저장할 원소의 종류나 크기에 따라 구조를 정의하여 사용
    2. #### link field
       
       - 다음 node의 `주소`를 저장하는 자료구조

<br>

### Head

- List의 처음 Node를 가리키는 reference

<br>

<br>

## 단순 연결 리스트

- Node가 하나의 link field에 의해 다음 Node와 연결되는 구조를 가짐
- **Head**가 가장 앞의 node를 가리키고, 각 node의 link field가 연속적으로 다음 노드를 가리킴
- 최종적으로 **None**을 가리키는 node가 list의 가장 *마지막 node*

<br>

### 단순 연결 리스트의 삽입 연산

>  A, C, D를 원소로 갖고 있는 list의 두 번째에 B node를 삽입할 때

1. Memory를 할당하여 새로운 node `new` 생성함
2. 생성된 node `new`의 data field에 B를 저장
3. 삽입될 위치의 바로 앞에 위치한 node의 link field를 `new`에 복사
4. `new`의 주소를 앞 node의 link field에 저장

<br>

#### 첫 번째 node로 삽입하는 알고리즘

```python
def addtoFirst(data): #첫 node에 data 삽입
    global Head
    Head = Node(data, Head) #새로운 node 생성
```

<br>

#### 가운데 node로 삽입하는 알고리즘

> node `pre`의 다음 위치에 node 삽입

```python
def add(pre, data): #pre 다음에 data 삽입
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)
```

<br>

#### 마지막 node로 삽입하는 알고리즘

```python
def addtoLast(data): #마지막에 data 삽입
    global Head
    if Head == None: #빈 list이면
        Head = Node(data,None) #list의 최초 node로 추가
    else:
        p = Head
        while p.link != Node: #마지막 node 찾을 때까지 (link가 None 일때 까지)
            p = p.link
        p.link = Node(data,None)
```

<br>

<br>

### 단순 연결 리스트의 삭제 연산

> A, B, C, D list의 B node를 삭제할 때

1. 삭제할 node의 선행 node 탐색
2. 삭제할 node의 link field를 선행 node의 link field에 복사

<br>

#### 첫 번째 node를 삭제하는 알고리즘

```python
def deletetoFirst(): #처음 node 삭제
    global Head
    if Head == None:
        print('error!')
    else:
        Head = Head.link
```

<br>

#### Node를 삭제하는 알고리즘

> node `pre`의 다음 위치에 있는 node 삭제

```python
def delete(pre): #pre 다음 node 삭제
    if pre == None or pre.link== None:
        print('error!')
    else:
        pre.link = pre.link.link
```



<br>

<br>

## 이중 연결 리스트 (Doubly Linked List)

- 양쪽 방향으로 순회할 수 있도록 node를 연결한 list
- 두 개의 link field와 한 개의 data field로 구성

<br>

### 이중 연결 리스트의 삽입 연산

> `cur`이 가리키는 node 다음에 D 값을 가진 node를 삽입하는 과정

1. 메모리를 할당하여 새로운 노드 `new`를 생성하고 data field `D`를 저장
2. `cur`의 next를 `new`의 next에 저장하여 `cur`의 다음 node를 삽입할 node의 다음 node로 연결
3. `new`의 값을 `cur`의 `next`에 저장하여 삽입할 node를 `cur`의 다음 node로 연결
4. `cur`의 값을 `new`의 prev field에 저장하여 `cur`를 `new`의 이전 node로 연결
5. `new`의 값을 `new`가 가리키는 node의 다음 node의 prev field에 저장하여 삽입하려는 node의 다음 node와 삽입하려는 node를 연결

<br>

### 이중 연결 리스트의 삭제 연산

> `cur`이 가리키는 node를 삭제하는 과정

1. 삭제할 node의 다음 node의 주소를 삭제할 node의 이전 node의 next field에 저장하여 link를 연결
2. 삭제할 node의 다음 node의 prev field에 삭제할 node의 이전 node의 주소를 저장하여 link를 연결
3. `cur`이 가리키는 node에 할당된 memory를 반환