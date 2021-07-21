# 에러와 예외

## 디버깅

> "코드의 상태를 신중하게 출력해가며 심사숙고하는 것보다 효과적인 디버깅은 없다."
>
> - 브라이언 케니헨



코드 작성 중

- 에러 메시지가 발생하는 경우

- 로직 에러가 발생하는 경우
  - 예상과 다른 결과가 나온 경우





## 에러(Error)

### 문법 에러 (Syntax Error)

- 문법을 지키지 않아 발생하는 에러
  - 파일이름, 줄 번호, ^ 문자를 통해 문제 발생 위치 표현

- Invalid syntax
  - 불가능한 문법
- assign to literal
  - 리터럴에 할당할 수 없음
- EOL(End of Line)
- EOF(End of File)

### 

## 예외(Exception)

- 실행 도중 감지되는 에러, 프로그램 실행을 멈춤
- 문법적으로 틀린 것은 아님.

### ZeroDivisionError

- 0으로 나누려고 하면 발생

### NameError

- namespace 상에 이름이 없는 경우 발생

### TypeError

- 타입이 불일치할 때 발생
- argument 누락 시 발생
- argument 개수 초과 시 발생

### ValueError

- 타입은 올바르지만 값이 적절하지 않거나 없으면 발생

### IndexError

- 인덱스가 존재하지 않거나 벗어나는 경우 발생

### KeyError

- 키가 존재하지 않는 경우 발생

### ModuleNotFoundError

- 존재하지 않는 모듈을 import 하는 경우 발생

### ImportError

- Module은 있지만 그 안에 존재하지 않는 클래스/함수를 가져오려고 하는 경우 발생

### KeyboardInterrupt

- 임의로 프로그램을 종료했을 때 발생

### IndentationError

- Indentation 잘못됐을 때 발생

[파이썬 예외 계층 구조](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)



## 예외 처리

- try / except 문을 이용해 예외처리

  ```python
  try:
      <code block>
  except <Exception>:
      print('error!')
  ```

- 예외 발생 시에도 프로그램이 작동할 수 있게 만듦



- `try` : 코드를 실행
- `except` : `try` 문에서 예외 발생시 실행
- `else` : `try` 문에서 예외 발생하지 않으면 실행
- `finally` : 예외 발생 여부와 상관없이 항상 실행



### 예외 처리 예시

- 파일을 열고 읽는 코드

  - 파일 열기 시도
    - 파일 없으면 => '파일 없음' 출력
    - 파일 있으면 => 파일 내용 출력
  - 파일 읽기 작업 종료 메시지 출력

  ```python
  try:
      f = open('file.txt')
  except:
      print('파일이 없습니다.')
  else:
      print('파일을 읽기 시작합니다.')
      print(f.read())
      f.close()
      print('파일을 다 읽었습니다.')
  finally:
      print('파일 읽기를 종료합니다.')
  ```

  

### 에러 메시지 처리

- `as` 키워드 활용해 원본 에러 메시지 사용 가능

  ```python
  try:
      empty_list = []
      print(empty_list[2])
  except IndexError as err:
      print(f'{err} 오류가 발생')
  ```

  

## 예외 발생 시키기

- `raise` 문으로 예외를 강제로 발생시킴

  ```python
  raise <Exception Type>(<error message>)
  ```

  디버깅, 테스트 등 사용

- `assert` 문으로 **AssertionError** 강제로 발생

  - 일반적으로 디버깅 용도로 사용

  ```python
  assert <Expression>, <error message>
  ```

  

