# 문자열, String

## 문자의 표현

컴퓨터에서의 문자 표현

- 컴퓨터는 각 문자에 대해서 대응되는 숫자를 정해 놓고 이 숫자를 메모리에 저장한다.

### ASCII

- 영어는 대소문자 52자이므로 6비트면 모두 표현 가능하다.
- 미국의 ASCII 문자 인코딩 표준은 코드 체계를 통일한 것.
- ASCII는 7bit 인코딩으로 128문자 표현, 33개 출력 불가능한 제어문자 + 공백을 포함한 95개의 출력 가능한 문자.
- 확장 ASCII는 표준 문자 이외의 특수 문자 등 128개 추가한 부호
- 확장 아스키는 8bit를 모두 사용.
- 확장 부호는 서로 다른 프로그램이나 컴퓨터 사이에 교환 불가
- 오늘날 대부분의 컴퓨터는 문자 읽고 쓰기에 ASCII형식 사용

### 유니코드

- 각 나라마다 자국의 문자를 표현하기 위한 코드체계의 필요
- 다국어 처리를 위한 표준이 유니코드

- 유니코드도 Character Set으로 분류
- UCS-2, UCS-4
- 유니코드를 저장하는 변수의 크기 정의
- 바이트 순서에 대해서 표준화하지 못했다.
- 따라서 파일이 UCS-2, UCS-4인지 인식해야하고 구분해야하는 문제 발생
- 따라서 적당한 외부 인코딩이 필요.
- big-endian, little-endian
- 유니코드 인코딩 (UTF)
- UTF-8 in web, 8 ~32
- UTF-16 in window, java, 16 ~ 32
- UTF-32 in unix, 32 ~ 32

### 파이썬 인코딩

- 2버전 - ASCII
- 3버전 - 유니코드 UTF-8



<br/>



## 문자열의 분류

- fixed length
- variable length
  - length controlled (java)
  - delimited (C)

- java의 String 클래스의 메모리 배치
  - 기본적인 객체 메타 데이터 외에도,
  - hash해시값, count문자열길이, offset문자열데이터시작점, value실제문자열배열참조
- C언어에서 문자열 처리
  - 문자들의 배열 형태로 구현된 응용 자료형
  - 문자배열에 문자열 저장시 항상 마지막에 널문자(`\0`)를 넣어줘야함.
  - 문자열 처리에 필요한 연산을 함수 형태로 제공
- java에서 문자열처리
  - String 클래스 사용
  - 문자열 처리에 필요한 연산을 연산자, 메소드 형태로 제공

- Python에서의 문자열 처리
  - char 타입 없음
  - 텍스트 데이터 취급 방법 통일
  - 문자열 기호
    - `''`,`""`,`"""`,`'''`
    - `+` 연결
    - `*` 반복
  - 시퀀스 자료형으로 분류, 인덱싱과 슬라이싱 사용
  - 변경 불가능
- C, Java String 처리 차이점
  - C는 아스키 코드
  - Java는 유니코드 UTF-16
  - Python은 유니코드 UTF-8
  - 길이 반환 시 C는 몇 바이트인지 반환



<br/>



## 문자열 다루기

### 문자열 비교

- C : `strcmp()`
- Java : `equals()`,
  - `==` 는 메모리 참조가 같은지
- Python : `==`, `is`
  - `==`는 내부적으로 특수 메서드 `__eq__()`호출

### 문자열 숫자 정수로 변환

- C :`atoi()`, 역함수 `itoa()`
- Java : 숫자 클래스의 `parse`메소드, 역함수 `toString()`
- Python : `int()`, 역함수 `str()`





