# 객체지향 프로그래밍, OOP

Object Oriented Programming



## 객체, Object

>  모든 것은 객체다.

[위키피디아 - 객체](https://ko.wikipedia.org/wiki/%EA%B0%9D%EC%B2%B4_(%EC%BB%B4%ED%93%A8%ED%84%B0_%EA%B3%BC%ED%95%99))



_객체(object)는 특정 타입의 인스턴스(instance)다._



- 1, 519, 2는 모두 `int`의 인스턴스
- `'hello'`,` 'python'` 은 모두 `string`의 인스턴스
- `['a', 'b', 'c']`, `[]`는 모두 `list`의 인스턴스



**객체의 특징**

- 타입(type) : 어떤 연산자와 조작(metod)이 가능한가
- 속성(attribute) : 어떤 상태(데이터)를 가지는가
- 조작(method) : 어떤 행위(함수)를 할 수 있는가



`is` : 객체의 아이덴티티를 검사하는 연산자

```python
type(10) is int  # True
type(10) is bool  # False
```

`isinstance(objectm classinfo)` 

- object가 classinfo의 instance이거나 subclass인 경우 True 
- classinfo가 type으로 구성된 tuple인 경우 그 중 하나라도 일치하면 True

```python
isinstance(10, int)  # True
isinstance(10, (int, bool))  # True
```



### 객체의 속성

- 속성은 객체의 상태/데이터

- `<object>.<attribute>`

  ```python
  (3 + 4j).real  # 3
  (3 + 4j).imagine  # 4
  ```

  

### 객체의 메서드

- 특정 객체에 적용될 수 있는 행위, 클래스에 정의된 함수

- `<object>.<method>()`

  ```python
  [1, 2, 3].pop()  # 3
  'hello'.upper()  # HELLO
  ```

  







## OOP, Object Oriented Programming

### 프로그래밍 패러다임

- 명령형 프로그래밍 : 프로그래머가 기계에게 상태를 변경하는 방법을 지시
  - 절차 지향 프로그래밍 : 데이터와 함수로 변화를 이끌어냄
  - **객체 지향 프로그래밍** : 데이터와 기능(메서드) 분리, 추상화된 구조(인터페이스)

### 객체 지향 프로그래밍

[위키피디아 - 객체 지향 프로그래밍](https://ko.wikipedia.org/wiki/%EA%B0%9D%EC%B2%B4_%EC%A7%80%ED%96%A5_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)

컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것이다.



#### 왜 객체 지향 프로그래밍인가

- 현실 세계를 프로그램 설계에 반영 (추상화)하기 위해
- 



## 상속

