# 함수(Function)

## 함수란? (What)

- 특정 기능의 코드 묶음
- 높은 재사용성, 유지 보수 용이 장점
- 함수 특징
  - 이름
  - 매개변수
  - 바디 - Docstring 코드셋
  - 반환 값



## 함수를 사용해야 하는 이유 (Why)

- 코드의 재사용성
- 유지 보수 용이



## 함수 사용법(How)

### 함수의 선언

- `def` 키워드로 선언
- 들여쓰기로 body 작성, Docstring은 선택적으로 작성
- 매개변수(parameter)
-  `return`으로 결과 값 전달
  - 반드시 하나의 객체



### 함수의 호출

- `함수명()` 으로 호출
- 매개변수가 있는경우, `함수명(값1, 값2, ...)` 로 호출



### 함수의 리턴

- 항상 반환되는 값이 있으며 어떠한 객체라도 상관없음
- 여러 개의 값은 튜플로 반환
- 명시적인 return 값이 없는 경우 None으로 반환



### 함수의 입력

#### parameter(매개변수) vs. argument(인자)

- 매개변수 : 함수에 입력으로 전달된 값을 받는 변수

  - ```python
    def my_func(a, b):
    	pass
    ```

    여기서 a랑 b은 매개변수

- 인자 : 함수를 호출할 때 함수에 전달하는 입력값

  - ```
    my_func(1, 2)
    ```

    여기서 1이랑 2은 인자

- 위치 인자(Positional Arguments)
  - 함수 호출 시 인자는 위치에 따라 함수 내에 전달됨

- 기본 인자 값

  - 기본값을 지정하여 함수 호출 시 인자 값을 설정하지 않도록 함

    ```python
    def foo(x, y=0):
        return x+y
    
    print(foo(2)) # 2
    ```

- 키워드 인자(Keyword Arguments)

  - 직접 변수의 이름으로 특정 인자를 전달할 수 있음

  - 키워드 인자 다음에 위치 인자를 활용할 수 없음

    ```python
    def add(x, y):
        return x+y
    
    print(add(x=2, y=5)) # 7
    print(add(2, y=5)) # 7
    ```

- 가변 인자 리스트 (Arbitrary Arguments Lists)

  - 함수가 임의의 개수 인자로 호출될 수 있도록 지정

  - 인자들은 튜플로 묶여 처리되며, 매개변수에 `*`를 붙여 표현, 꼭 args아니어도 됨, 관례

    ```python
    def foo(*args):
    	for arg in args:
            print(arg)
          
    foo(2)
    # 2
    
    foo(2, 3, 4, 5)
    # 2
    # 3
    # 4
    # 5
    ```

- 가변 키워드 인자 (Arbitrary Keyword Arguments)

  - 함수가 임의의 개수 인자를 키워드 인자로 호출될 수 있도록 지정

  - 인자들은 딕셔너리로 묶여 처리되며, 매개변수에 `**`를 붙여 표현, 꼭 kwargs 아니어도됨.

    ```python
    def student(**kwargs):
        for key, value in kwargs:
            print(key, ":", value)
            
    student('철수'='201920131', '영희'='201582932')
    # 철수 : 201920131
    # 영희 : 201582932
    ```

- 함수 선언 및 활용 시 인자 주의 사항
  - 기본 인자 값을 가지는 인자는 기본 값이 없는 인자 뒤에 정의해야함
  - 키워드 인자 다음에 위치 인자 활용 불가
  - 가변 인자 리스트는 위치 인자보다 뒤에 정의해야함
  - 가변 키워드 인자리스트는 위치 인자보다 뒤에 정의해야함
    - **함수 선언 시 `위치 인자` >`기본값이 있는 위치 인자`> `*args` > `**kwargs` 순서로 정의**

### 함수 Scope

- 스코프
  - 전역 스코프 : 코드 어디서든 참조할 수 있는 공간
  - 지역 스코프 : 함수가 만든 스코프. 함수 내에서만 참조 가능

- 변수
  - 전역 변수 : 전역 스코프에 정의된 변수
  - 지역 변수 : 지역 스코프에 정의된 변수
- 변수의 수명 주기
  - 빌트인 스코프 : 파이썬이 실행된 이후부터 영원히 생존
  - 전역 스코프 : 모듈 호출 후 또는 인터프리터 끝나기 전까지 유지
  - 지역 스코프 : 함수가 호출될때 생성, 함수가 종료되면 사망:skull:

- 이름 검색 규칙

  - 파이썬에서 사용되는 식별자들은 namespace에 저장되어 있음

  - LEGB Rule

    - Local scope
    - Enclosed scope
    - Global scope
    - Built-in score

  - 식별자의 값을 위의 순서대로 찾아나감

  - 함수 내에서 바깥 스코프 변수에 접근(get) 가능하나 수정(set)은 불가

  - 바깥 스코프에서 안쪽 스코프 변수에 접근도 불가, 수정도 불가

    ```python
    # LEGB rule 1
    a = 0
    b = 1
    def enclosed():
        a = 10
        c = 3
        def local(c):
            print(a, b, c)
        local(300)
        print(a, b, c)
    enclosed()
    print(a, b)
    
    # 10, 1, 300   -> local(300)
    # 10, 1, 3     -> enclosed() 안의 print
    # 0, 1         -> 마지막 print(a, b)
    ```

    ```python
    # LEGB rule 2
    print(sum)              # <built-in function sum>
    print(sum(range(2)))    # 1
    sum = 5         
    print(sum)              # 5
    print(sum(range(2)))    # TypeError: 'int' object is not callable
    ```

    

- `global`
  - 현재 코드 블록에 전체 적용, 나열된 식별자들이 전역 변수임을 나타냄
  - 주의사항
    - `global`로 선언된 변수가 같은 코드 블록에서 `global` 키워드 앞에 나타날 수 없음
    - 매개변수, for 루프 대상, 클래스/함수 정의 등으로 정의되면 안됨
    - 유지 보수에서 문제가 생길 수도 있음
    - 함수로 값을 바꾸고자 한다면 인자로 받아서 리턴 값으로 대신 사용

- `nonlocal`

  - 전역을 제외하고 가장 가까운 스코프의 변수를 연결하도록 함

  - 주의사항

    - 위와 같음

  - 이미 존재하는 이름만 가능

    ```python
    x = 0
    def foo():
        x = 1
        def goo():
            nonlocal x
            x = 2
        goo()
        print(x) # 2
    foo()
    print(x)  # 0
    ```

