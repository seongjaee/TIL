# 객체지향 프로그래밍, OOP (1)

Object Oriented Programming



## 객체, Object

>  Python의 모든 것은 객체(Object)다.

[위키피디아 - 객체](https://ko.wikipedia.org/wiki/%EA%B0%9D%EC%B2%B4_(%EC%BB%B4%ED%93%A8%ED%84%B0_%EA%B3%BC%ED%95%99))



**객체의 특징**

- 타입(type) : 어떤 연산자와 조작(metod)이 가능한가
- 속성(attribute) : 어떤 상태(데이터)를 가지는가
- 조작(method) : 어떤 행위(함수)를 할 수 있는가



### 타입과 인스턴스

__모든 객체(object)는 특정 타입(Type)의 인스턴스(instance)다.__

- 타입 : 공통된 속성, 행동(메서드)을 가진 객체들의 분류
- 인스턴스 : 특정 타입의 실제 데이터
  - 1, 519, 2는 모두 `int` 타입의 인스턴스
  - `'hello'`, ` 'python'` 은 모두 `string` 타입의 인스턴스
  - `['a', 'b', 'c']`, `[]`는 모두 `list` 타입의 인스턴스

### 속성

- 속성은 객체의 상태/데이터

- `<object>.<attribute>`

  ```python
  (3 + 4j).real  # 3
  (3 + 4j).imag  # 4
  ```

### 메서드

- 특정 객체에 적용될 수 있는 행위, 클래스에 정의된 함수

- `<object>.<method>()`

  ```python
  [1, 2, 3].pop()  # 3
  'hello'.upper()  # HELLO
  ```

### 객체의 비교

- `==` : 동등한
  - 변수가 참조하는 객체의 데이터가 같은 경우 `True`
- `is` : 동일한
  - 변수가 동일한 객체를 가리키는 경우 `True`

- `is` : 객체의 아이덴티티를 검사

  ```python
  type(10) is int  # True
  type(10) is bool  # False
  ```

- `isinstance(object, classinfo)` 

  - object가 classinfo의 instance이거나 subclass인 경우 True 
  - classinfo가 type으로 구성된 tuple인 경우 그 중 하나라도 일치하면 True

  ```python
  isinstance(10, int)  # True
  isinstance(10, (int, bool))  # True
  ```

  

<br/>



## OOP, Object Oriented Programming

### 프로그래밍 패러다임

- 명령형 프로그래밍 : 프로그래머가 기계에게 상태를 변경하는 방법을 지시
  - 절차 지향 프로그래밍 : 데이터와 함수로 변화를 이끌어냄
  - **객체 지향 프로그래밍** : 데이터와 기능(메서드) 분리, 추상화된 구조(인터페이스)

### 객체 지향 프로그래밍

[위키피디아 - 객체 지향 프로그래밍](https://ko.wikipedia.org/wiki/%EA%B0%9D%EC%B2%B4_%EC%A7%80%ED%96%A5_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)

- 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것이다.



#### 왜 객체 지향 프로그래밍인가

- 현실 세계를 프로그램 설계에 반영 (추상화)하기 위해
- 코드의 직관성
- 활용의 용이성
- 변경의 유연성



#### 객체 지향 프로그래밍 예시

- 직사각형의 너비와 높이가 주어졌을 때, 직사각형의 넓이와, 둘레를 구하는 코드

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
   	def perimeter(self):
        return 2 * (self.width + self.height)
```

```python
my_rect = Rectangle(30, 100)
my_rect.area()  # 3000
my_rect.perimeter()  # 260
```



- 사각형의 정보 - 속성(attribute)
  - 너비, 높이
- 사각형의 행동 - 메서드(method)
  - 넓이, 둘레

<br/>



## 클래스와 인스턴스, Class & Instance

- 클래스 정의 : `class MyClass:` (클래스 이름은 파스칼 case로)
- 인스턴스 생성 : `my_instance = MyClass()`

- 메서드 호출 : `my_instace.my_method()`
- 속성 : `my_instance.my_attribute`

- 클래스를 정의하고, 인스턴스들을 만들어 활용한다.
  - 클래스 : 객체들의 분류
  - 인스턴스 : 하나하나의 실체들



### 클래스(Class)

- 공통된 속성과 행위를 정의한 것.



### 인스턴스(Instance)

- 특정 class로부터 생성된 클래스의 실체



### 속성

- 특정 클래스의 객체들이 가지게 될 상태/데이터



### 메서드

- 특정 클래스의 객체에 공통적으로 적용 가능한 행위(함수)



### self

- 인스턴스 자기자신
- 인스턴스 메서드는 호출 시 첫번째 인자로 인스턴스 자신이 전달됨.
  - 정의 시에, 첫번째 인자의 이름을 `self`로 정의해야함, 딴 거로 해도 작동은 됨.



### 생성자(constructor)

- 인스턴스 객체가 생성될 때 호출되는 메서드

  ```python
  class MyClass:
      def __init__(self):
          print('인스턴스 생성 완료')
          
  my_instance = Myclass()
  # 인스턴스 생성 완료
  ```
  
  ```python
  class MyClass:
      def __init__(self, name):
          print(f'인스턴스 생성 완료. {name}.')
          
  my_instance = MyClass('Hello')
  # 인스턴스 생성 완료. Hello.
  ```



### 소멸자

- 인스턴스 객체가 소멸되기 직전에 호출되는 메서드

  ```python
  class MyClass:
  	def __init__(self):
          print('인스턴스 생성 완료')
      def __del__(self):
          print('인스턴스가 삭제됩니다.')
          
  my_instance = MyClass()
  # 인스턴스 생성 완료
  del my_instance
  # 인스턴스가 삭제됩니다.
  ```



### 매직 메서드

- Double underscore(`__`) 가 있는 메서드
- 특수한 동작을 위해 만들어진 메서드로, 스페셜 메서드 또는 매직메서드
- 예시
  - `__str__(self)` : 해당 객체의 출력 형태 지정
  -  `__lt__(self, other)` : 부등호 연산자 (<, less than)

