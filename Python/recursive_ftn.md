# 재귀 함수(Recursive function)

## 재귀 함수란

- 자기 자신을 호출하는 함수
- 알고리즘 설계 및 구현에 유용하게 활용
  - 점화식 등 재귀 함수로 로직을 표현하기 쉬운 경우
  - 변수의 사용이 줄어들어, 가독성이 높아짐

## 재귀 함수 사용

- base case(종료되는 상황)이 존재해 수렴하도록 작성
  - 큰 문제를 해결하기 위해 작은 문제로 줄이고 작은 문제의 해답을 이용해 해결



- 재귀 함수 주의 사항
  - base case에 도달할 때까지 함수를 호출함
  - 메모리 스택이 넘치면 프로그램이 동작하지 않음
  - 파이썬의 최대 재귀 깊이(maximum recursion depth) 은 1000번, 넘어가면 Recursion Error 발생
    - `sys.setrecursionlimit(limit))`으로 재귀 깊이 제한 수정 가능







- 재귀 함수를 이용한 팩토리얼 계산

  ```python
  def factorial(n):
      if n == 1:                 # base case
          return 1     
      return n * factorial(n-1)  # 자기 자신 호출
  
  
  print(factorial(4)) # 24
  """
  factorial(4) 
  	return 4 * factorial(3)   -> 4 * (3 * 2 * 1)
  		return 3* factorial(2)   -> 3 * (2 * 1)
  			return 2 * factorial(1)   -> 2 * 1
  				return 1
  """
  ```

  

- 재귀 함수를 이용한 피보나치 수 계산

  ```python
  def fibonacci(n):
      if n < 2:
          return 1
      return fibonacci(n-1) + fibonacci(n-2)
  ```

  

- 메모이제이션을 적용한 피보나치 수 계산

  ```python
  memos = {0:1, 1:1}
  def fibonacci(n):
      if n in memos:
          return memos[n]
      memos[n] = fibonacci(n-1) + fibonacci(n-2)
      return memos[n]
  ```

  