# Nested List (2차원)

## 2차원 배열

### 2차원 배열 선언

- 1차원 List를 묶어놓은 List

- 2차원 이상의 다차원 List는 차원에 따라 Index 선언

- Python에서 2차원 List 선언

  - `arr = [[0, 1, 2, 3], [4, 5, 6, 7]]`
- `zero_arr = [[0]*m for _ in range(n)]` : 0만 담긴 n행 m열

<br/>



### 2차원 배열 접근

- 배열 선회

- 행 우선

  ```python
  for i in range(len(arr)):
  	for j in range(len(arr[i])):
          arr[i][j]
  ```

- 열 우선

  ```python
  for j in range(len(arr[0])):
      for i in range(len(arr)):
          arr[i][j]
  ```

- 지그재그 순회

  ```python
  for i in range(len(arr)):
      for j in range(len(arr[i])):
          arr[i][j + (len(arr[i])-1-2*j) * (i%2)]
  ```

- 델타를 이용한 2차원 배열 탐색

  2차원 배열의 한 좌표에서 4방향의 인접 배열 요소 탐색

  ```python
  # arr : N행 M열 2차원 배열
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]
  
  for x in range(len(arr)):
      for y in range(len(arr[x])):
          for i in range(4):
              nx = x + dx[i]
              ny = y + dy[i]
              if 0 <= nx < N and 0 <= ny < M:
              	arr[nx][ny]  # 접근 후 동작
  ```




<br/>



### 2차원 배열 활용

- 전치 행렬

  ```python
  # arr : N x N 정사각행렬
  
  for i in range(N):
      for j in range(i+1, N):
          arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
  ```

  

