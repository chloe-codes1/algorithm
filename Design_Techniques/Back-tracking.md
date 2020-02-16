# Back-tracking

> 해를 찾는 도중에 막히면 (해가 아니면) 되돌아가서 다시 해를 찾는 기법

:  어떤 Node가 Promising한지 검사 한 후 그렇지 않으면 그 Node의 부모로 Backtracking 한 다음 자식 Node로 가는 방식



<br/>

### Back-tracking으로 해결 가능한 문제

- 최적화(Optimization) 문제

- 결정(Decision) 문제

  : 문제의 조건을 만족하는 해가 존재하는지의 여부를 'yes' or 'no'로 답하는 문제

  - 미로 찾기
  - N-Queen
  - Map coloring
  - 부분 집합의 합(Subset Sum) 문제

  <br/>

### Differencet between Back-tracking and DFS (= Depth First Search)

1. Back-tracking

   - 어떤 node에서 출발하는 경로가 답이 아닐 것 같으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임

      -> 가지치기 (Pruning)

   - N! 가지의 경우의 수를 가진 문제에서 일반적으로 경우의 수 줄어들지만, 최약의 경우에는 지수함수 시간(Exponential Time)을 요하므로 처리 불가

   - 모든 후보를 검사하지 않음

2. DFS

   - 모든 경로를 추적
   - N! 가지의 경우의 수를 가진 문제에 대해서는 처리 불가능함 -> 너무 많아서!
   - 모든 후보를 검사하지 않음

   
<br/>


   







