# 스택 응용

## 계산

- 문자열로 주어진 계산식 계산

### 방법

- step1 - 중위 표기법의 수식을 후위 표기법으로 변경
- step2 - 후위 표기법 수식을 스택을 이용하여 계산
- 중위 표기법
  - 연산자를 피연산자 가운데 표기
  - A+B
- 후위 표기법
  - 연산자를 피연산자 뒤에 표기
  - AB+



### Step1

### 중위 표기법 -> 후위 표기법 변경 방법 1

- 수식의 각 연산자에 대해 우선순위에 따라 괄호를 표기
- 연산자를 그에 대응하는 오른쪽 괄호의 뒤로 이동
- 괄호 제거

### 중위 표기법 -> 후위 표기법 변경 방법 2

- 입력 받은 중위 표기식에서 토큰을 읽는다.

- 토큰이 피연산자면 토큰 출력

- 토큰이 연산자면, 토큰이 스택의 top과 우선순위 비교

  - 우선순위가 더 높으면 스택에 push

  - 그렇지 않으면  스택의 top 연산자보다 클 때 까지 스택에서 pop 후 push

    top에 연산자 없으면 그냥 push

  - 연산자가 `)`면 `(`가 나올 때 까지 pop

  

  - 우선순위
    - 토큰일 때 우선순위
      - `(` = 3
      - `*, / ` = 2
      - `+, - ` = 1
    - 스택에서 우선순위
      - `(` = 0
      - `*, / ` = 2
      - `+, - ` = 1

- 예시

  - `( 6 + 5 * ( 2 - 8 ) / 2)`
  - => `6 5 2 8 - * 2 / +`
- 손으로 직접 해보자!

#### 코드

```python
def postfix_notation(formula):
    stack = []
    result = ''
    for token in formula:
        if token in token_rank:
            # 닫는 괄호가 아니면 stack이 비거나
            # stack의 top보다 우선순위가 높아질 때까지 pop
            if token != ')':
                while stack and stack_rank[stack[-1]] >= token_rank[token]:
                    temp = stack.pop()

                    # 괄호면 추가하지 않아도 됨
                    if temp != '(' and temp != ')':
                        result += temp

                # stack에 push
                stack.append(token)

            else:
                # 닫는 괄호 일 때는 
                # 열린 괄호가 나올 때까지 pop
                while stack:
                    temp = stack.pop()
                    if temp == '(':
                        break

                    result += temp

        # 피연산자면 result에 추가
        else:
            result += token

    # stack에 남은 것들 result에 추가
    while stack:
        temp = stack.pop()
        if temp != '(' and temp != ')':
            result += temp

    return result
```



### Step2 - 후위 표기법 수식 계산

- 피연산자를 만나면 스택에 push

- 연산자를 만나면 필요한만큼 피연산자를 스택에서 pop해서 연산

  연산결과를 다시 스택에 push

- 수식이 끝나면 마지막으로 스택을 pop해서 출력
- 예시
  -  `6 5 2 8 - * 2 / +` = -9
  - 손으로 직접 해보자!

#### 코드

```python
def calculate_formula(formula):
    # 후위 표기법 계산하기
    stack = []
    for token in formula:
        # 연산자면 stack에서 두 개를 꺼내서 연산 후
        # 다시 stack에 push
        if token in operator:
            a = int(stack.pop())
            b = int(stack.pop())
            if token == '+':
                stack.append(b + a)
            elif token == '*':
                stack.append(b * a)
            elif token == '-':
                stack.append(b - a)
            elif token == '/':
                stack.append(b // a)

        # 피연산자면 stack에 push
        else:
            stack.append(token)

    # 최종 결과
    return stack.pop()
```





## 백트래킹 (Backtracking)

- 해를 찾는 도중 해가 아니면 되돌아가서 다시 탐색하는 기법
- 최적화 문제와 결정 문제를 해결할 수 있다.
- 결정 문제: 문제의 조건을 만족하는 해가 존재하는지의 여부를 답하는 문제

- 백트래킹과 깊이우선탐색과의 차이
  - 어떤 노드에서 출발하는 경로가 해가 될 수 없을 것 같으면 더 이상 진행하지 않음으로써 시도 횟수를 줄임. (=Pruning 가치지기)
  - 불필요한 경로를 조기에 차단하므로 깊이우선탐색보다 경우의 수를 줄일 수 있다.
  - 하지만 여전히 최악의 경우는 지수함수 시간이 걸림

- 백트래킹 기법
  - 노드의 유망성 검사 후 유망하지 않으면 부모로 되돌아감(backtracking)
  - 유망성 : 노드를 포함한 경로가 해일 가능성이 있는지
  - 가지치기(pruning) : 유망하지 않은 노드가 포함되는 경로는 고려하지 않음

### 부분집합 구하기

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
    
  - {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 부분집합 중 합이 10인 부분집합 
  
    ```python
    ```
  
  - 