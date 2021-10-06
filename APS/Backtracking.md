# 백트래킹 (Backtracking)

- 해를 찾는 도중 해가 아니면 되돌아가서 다시 탐색하는 기법
- 최적화 문제와 결정 문제를 해결할 수 있다.
- 결정 문제: 문제의 조건을 만족하는 해가 존재하는지의 여부를 답하는 문제

- 백트래킹과 깊이우선탐색과의 차이
  - 어떤 노드에서 출발하는 경로가 해가 될 수 없을 것 같으면 더 이상 진행하지 않음으로써 시도 횟수를 줄임. (=Pruning 가치지기)
  - 불필요한 경로를 조기에 차단하므로 깊이우선탐색(N!)보다 경우의 수를 줄일 수 있다.
  - 하지만 여전히 최악의 경우는 지수함수 시간이 걸림

- 백트래킹 기법
  - 노드의 유망성 검사 후 유망하지 않으면 부모로 되돌아감(backtracking)
  - 유망성 : 노드를 포함한 경로가 해일 가능성이 있는지
  - 가지치기(pruning) : 유망하지 않은 노드가 포함되는 경로는 고려하지 않음

## 부분집합 구하기

- 백트래킹 기법으로 powerset 구하기

  - n개의 원소에 대해 포함유무를 결정짓는 길이가 n인 배열을 이용한다.

  - ```python
    def backtrack(a, k, input):
        # k : 현재 고려 중인 부분
        global MAXCANDIDATES
        c = [0] * MAXCANDIDATES
        
        if k == input:
            process_solution(a, k)  # 해라면 원하는 작업 실행
        else:
            k += 1
            # 유망성있는 후보 배열
            ncandidates = construct_candidates(a, k, input, c)
            for i in range(ncandidiates):
                a[k] = c[i]
                backtrack(a, k, input)
    ```
    
    
  
- {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 부분집합 중 합이 10인 부분집합 구하기

  ```python
  def backtrack(k, target, c, s):
      if s == target:
          print(c)
          return
  
      if s > target:  # 현재까지의 합이 target을 넘으면 가지치기
          return
  
      if k >= len(numbers):
          return
  
      backtrack(k + 1, target, c | {k+1}, s + numbers[k])
      backtrack(k + 1, target, c, s)
  
  
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  
  backtrack(0, 10, set(), 0)
  ```

  

- NxN 2차원 배열에서 행이나 열이 중복되지 않게 N개의 원소를 골라 그 합이 최소가 되는 값을 구하기

  - 예시

    | 2    | 1 *  | 2    |
    | ---- | ---- | ---- |
    | 5 *  | 8    | 5    |
    | 7    | 2    | 2 *  |

    인 경우, *가 붙은 요소들만 골라 더하면 8로 최솟값이다.

  ```python
  def backtrack(matrix, y, used_x, s):
      # y : 이번에 살펴볼 행 번호
      # used_x : 현재까지 사용한 열 인덱스 집합
      # s : 현재까지 배열 합
      global answer
  
      # 이미 기존 최솟값보다 크다면 중지
      if s >= answer:
          return
  
      # 마지막 라인까지 봤다면 최솟값 갱신
      if y == N:
          answer = s
  
      for i in range(N):
          if i not in used_x:
              backtrack(matrix, y + 1, used_x | {i}, s + matrix[y][i])
              
              
  answer = N*N*10  # 가능한 최댓값으로 일단 설정
  
  backtrack(matrix, 0, set(), 0)  # matrix : 입력받은 행렬
  ```

  

## N-Queen 문제

- 접근
  - 상태 공간 트리로 생각
  - i행 j번째에 퀸을 둠.
  - 모든 후보를 검사하는게 아니라, 노드마다 노드의 유망성을 검사 후 유망한 경우만 자식 노드로 감.
- 절차
  - 상태 공간 트리의 깊이 우선 탐색
  - 노드 유망성 검사
  - 유망하지 않으면 부모노드로 되돌아감



- 일반적인 백트래킹 알고리즘

  ```
  checknode(node v)
  	IF promising(v)
  		IF there is a solution at v
  			write the solution
  		ELSE
  			FOR each child u of v
  				checknode(u)
  ```

  ```
  bool backtrack(선택 집합, 선택한 수, 모든 선택수)
  	if (선택한 수 == 모든 선택수) // 모두 선택했음. 탐색 끝
  		찾는 솔루션인지 체크
  		return 결과
  	
  	현재 선택한 상태 집합에 포함되지 않는 후보 선택들 생성
  	
  	모든 후보 선택들에 대해
  		선택 집합에 하나의 후보선택 추가
  		선택한 수 = 선택한 수 + 1
  		결과 = backtrack 호출
  		
  		if 결과 == 성공
  			return 성공
  		
  	return 실패
  ```

  

