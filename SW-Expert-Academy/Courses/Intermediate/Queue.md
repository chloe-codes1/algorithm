# Queue

1. 삽입/삭제의 위치가 제한적인 자료구조
2. `FIFO (= First In First Out)`

3. 기본연산
   - 삽입: enQueue
   - 삭제: deQueue
4. Front & Rear
   - Front와 Rear 값이 같으면 Queue가 비어있다고 판단 할 수 있음
5. 종류
   - 선형 큐 - list
   - 원형 큐 - list
   - 연결 큐 - linked list
   - 우선순위 큐 (advanced ver.)

<br>

#### 선형 큐

- 1차원 list를 이용한 queue

- queue의 크기 = list의 크기

- front: 저장된 첫 번째 원소의 index

- rear: 저장된 마지막 원소의 index

- **상태 표현**

  - 초기 상태

    : front = rear = -1

  - 공백 상태

    : front = rear

  - 포화 상태

    : rear = n - 1

      (n: 리스트의 크기, n-1: 리스트의 마지막 index)

- **문제점**

  : 잘못된 포화 상태 인식

    -> why?

  - 리스트의 크기 고정

  - 사용할 queue의 크기만큼 미리 확보

  - 메모리 낭비 발생

    ex) 삽입/삭제 계속 할 경우 list 앞부분에 공간 있어도 rear=n-1 상태 즉, 포화 상태로 인식

- Pros & Cons

  - Pros

    : 삽입/삭제 처리속도 빠름

  - Cons

    : 메모리 낭비가 심함

- 선형 큐의 단점 해결 방법

  1. 원형 큐 사용으로 메모리 절약

  2. Python의 list 특셩을 사용한 queue 사용으로 memory 절약

     but, 삽입/삭제 시 연산 수행에 많은 시간 소모

  3. linked list로 구현한 queue 사용으로 메모리 동적 확보

<br>

#### 원형 큐

- 1차원 리스트를 사용하되, 논리적으로 list의 처음과 끝이 연결되어 원형 형태의 queue를 이룬다고 가정하고 사용함

- 특징

  - **초기 공백 상태**

    : front = rear = 0

  - **index의 순환**

    - front와 rear의 위치가 list의 마지막 index인 n-1을 가리킨 후, 논리적 순환을 이루어 list의 처음 index인 0으로 이동해야 함
    - 이를 위해 나머지 연산자 %를 사용

  - 포화상태 검사

    - 삽입할 rear 의 다음위치 == 현재위치 일 때

  - front 변수

    : 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠
  
    <br>
  
    

| 테이블 인덱스 | 삽입 위치             | 삭제 위치              |
| ------------- | --------------------- | ---------------------- |
| 선형 큐       | rear = rear + 1       | front = front +1       |
| 원형 큐       | rear = (rear + 1) % n | front = (front + 1) %n |

<br>

<br>

#### 연결 큐

- **Linked List를 이용한 Queue**
  
  - Queue의 원소
  
    : Linked List의 각 node
  
  - Queue의 원소 순서
  
    : 각 node의 연결 순서 (link로 연결되어 있음)
  
  - Front
  
    : 첫 번째 node를 가리키는 link
  
  - Rear
  
    : 마지막 node를 가리키는 link
- 상태 표현
  - 초기 상태
  
    : front = rear = None
  
  - 공백 상태: front = rear = None

<br>

<br>









<br>

<br>

### Queue Module

<br>

#### Classes

1. queue.Queue(maxsize)

   : FIFO Queue Object 생성

2. queue.LifoQueue(maxsize)

   : Stack 개념의 LIFO Queue Object 생성

3. queue.PriorityQueue(maxsize)

   : 우선순위 Queue Object 생성

   - 입력되는 item의 형식은 (순위, 아이템)의 튜플로 입력되며, 우선순위는 숫자가 작을수록 높은 우선순위를 가짐



<br>

참고!

https://www.geeksforgeeks.org/stack-queue-python-using-module-queue/

<br>

<br>

### Queue 의 활용

<br>

#### 우선순위 Queue

- 우선순위를 가진 항목들을 저장하는 큐
- FIFO 순서가 아니라 *우선순위가 높은 순서대로* 먼저 나가게 됨

<br>

##### List 를 이용한 우선순위 큐

1. 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조
2. 가장 앞에 최고 우선순위의 원소가 위치하게 됨
3. But, list를 사용하므로 삽입/삭제 연산이 일어날 때 원소의 재배치가 발생
   - 소요되는 시간이 많이 걸림
   - 메모리 사용이 큼
     - Solution
       - PriorityQueue class 사용
       - Heap 자료구조 사용

<br>

<br>

#### Buffer

- 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 memory 영역
- `Buffering`
  - buffer를 활영하는 방식
  - buffer를 채우는 동작

<br>

##### Buffer의 자료구조

- buffer는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용