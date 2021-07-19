# 파이썬 기본

## 할당

- 할당 연산자 = 로 변수에 값을 할당할 수 있다.

## 변수

- 값이 할당 되는 공간?

## 데이터 타입

- 숫자, 문자열, Boolean, None 4가지 타입
- 숫자
  - 정수 int
  - 실수 float
  - 복소수 complex
- 문자열
  - str
  - '' , "" 로 만듦. """ 로는 여러줄의 문자열을 만들 수 있음.
  - .format, f-string 이용 가능
    - f-string {}안에 할당식은 불가능
  - 특정 문자는 이스케이프 문자 사용
- Boolean
  - True / False
  - 0, 0.0, (), [], {}, '', None 처럼 비어있는 값은 False로 변환
- None
  - 값이 없음

## 형변환

- 암시적 형변환
  - 사용자가 의도하지 않아도 파이썬 내부에서 알아서 타입 변환됨
  - bool, 숫자형 연산
- 명시적 형변환
  - 사용자가 명시적으로 형을 변환
  - 형식이 맞는 경우 int(), str(), float()으로 형변환 가능

## 표현식 (Expression)

- 평가되고, 값으로 변경괴는 식
- 하나의 값으로 환원될 수 있는 문장
- 식별자, 값, 연산자로 구성됨.
- 식별자 하나만 있어도 표현식임.

## 식별자

- 변수, 함수, 모듈, 클래스 등의 이름
- 규칙에 따라 정해야함.

## 문장 (Statement)

- 파이썬이 실행 가능한 최소한의 코드 단위
- 표현식 < 문장

## 연산자

- 산술, 비교, 논리 등등
- 연산자에는 순서가 있음
- 논리 연산자는 단축평가라는게 있음.
  - 앞의 값만 보고도 결과를 알 수 있다면 뒤의 값은 더이상 보지 않고 마지막에 확인한 값을 반환

## 컨테이너

- 여러 개의 값을 저장할 수 있는 것
- 시퀀스형과 비시퀀스형으로 나누어짐
- 시퀀스형, 순서가 있는 데이터
  - list, tuple, range, string, binary
- 비시퀀스형, 순서가 없는 데이터
  - set, dictionary

- 변경 가능한(mutable) 데이터와 변경 불가능한 데이터(immutable) 데이터로도 나누어짐

- mutable

  - list
  - set
  - dictionary

- immutable

  - 리터럴(literal) : 숫자, 문자열, Boolean
  - range
  - tuple

- mutable과 immutable의 차이는 복사에서 크게 나타남.

  - mutable 데이터를 복사하면 주소만 복사하게 됨. 두 개의 식별자가 같은 주소를 참조하고 있기 때문에 값을 변경하면 두 개가 동시에 변경됨

    ```python
    A = [1,2,3]
    B = A
    B[0] = 4
    
    print(A)  # [4,2,3]
    print(B)  # [4,2,3]
    ```

    

  - immutable 데이터를 복사하면, 두 개의 식별자가 같은 값을 공유함. 하나의 값을 재할당하면 두 개의 값이 달라짐.

    ```python
    a = 10
    b = a
    b = 0
    
    print(a)  # 10
    print(b)  # 0
    ```

    

- Iterable한 객체

  - 순회 가능한 객체 string, list, tuple, range 등

  - enumerate를 이용할 경우 iterable객체를 순회하면서 (_index_, _value_) 형태의 tuple을 반환함. 

