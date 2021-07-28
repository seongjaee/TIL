# 객체지향 프로그래밍, OOP (2)

Object Oriented Programming

## 클래스와 인스턴스의 변수와 메서드



### 인스턴스 변수

- 인스턴스의 속성
- 각 인스턴스들만의 고유한 변수
  - 메서드에서 `self.<name>`으로 정의
  - `<instance>.<name>` 으로 접근, 할당

### 클래스 변수

- 클래스의 속성
- 모든 인스턴스가 공유함
  - 클래스 선언 내부에서 정의
  - `<classname>.<name>`으로 접근, 할당

### 인스턴스와 클래스 간의 이름 공간

- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
- 인스턴스를 만들면, 인스턴스 객체와 이름공간 생성
- 인스턴스의 속성에 접근하면, 인스턴스->클래스 순으로 탐색



### 변수 정리

- 클래스 변수

  - 클래스 정의 안에, 인스턴스 메서드 밖에 선언
  - 특정 클래스 인스턴스에 묶여있지 않음
  - 클래스 자체 내용을 저장
  - 같은 클래스에서 만들어진 인스턴스들은 동일한 클래스 변수 공유

- 인스턴스 변수

  - 특정 인스턴스에 묶여있음
  - 클래스에서 만들어진 각각의 객체에 저장
  - 인스턴스마다 독립적이므로 변수의 값을 수정하면 해당 객체에만 영향

- **주의**

  ```python
  class Cat:
      num_tails = 1  # 클래스 변수
      
      def __init__(self, name):
          self.name = name  # 인스턴스 변수
  ```

  ```python
  alice = Cat('alice')
  bob = Cat('bob')
  print(alice.name)  # alice
  print(bob.name)  # bob
  ```

  ```python
  # 클래스 변수는 각 인스턴스 또는 클래스 자체에서 접근 가능
  print(alice.num_tails)  # 1
  print(bob.num_tails)  # 1
  
  print(Cat.num_tails)  # 1
  ```

  ```python
  # 클래스에서 클래스 변수에 접근에 수정할 수 있음.
  Cat.num_tails = 2
  
  print(alice.num_tails)  # 2
  print(bob.num_tails)  # 2
  ```

  ```python
  # (바로 위의 코드를 실행하지 않고)
  # 인스턴스에서 클래스 변수를 접근 가능하지만, 수정할 수 없음
  # 대신 새로운 인스턴스 변수가 생김
  bob.num_tails = 2
  
  print(alice.num_tails)  # 1
  print(bob.num_tails)  # 2
  print(Cat.num_tails)  # 1
  
  # bob 인스턴스에서는 더이상 Cat.num_tails에 접근할 수 없음
  # 인스턴스 -> 클래스 순으로 탐색하기 때문
  ```

  - 클래스 변수가 동일한 이름의 인스턴스 변수에 의해 가려질 수 있기 때문에 주의해야함!
  - 클래스 변수는 반드시 클래스에서 접근해 변경해야함



### 인스턴스 메서드

- 인스턴스가 사용할 메서드
- 클래스 내부에서 정의되는 메서드
- 호출 시, 첫번째 인자로 인스턴스 자기자신(self)가 인자로 전달됨
- 클래스 상태를 수정할 수도 있음. 하지만 하지 말자.

### 클래스 메서드

- 클래스가 사용할 메서드
- `@classmethod` 데코레이터를 사용하여 정의
- 호출 시, 첫번쨰 인자로 클래스(cls)가 전달됨
- 클래스 자체의 변경을 원할 때 사용
- 클래스 정보에 접근해야 할 때 사용

### 스태틱 메서드

- 클래스가 사용할 메서드
- `@staticmethod` 데코레이터를 사용하여 정의
- 호출 시, self나 cls가 인자로 전달되지 않음(_클래스 정보에 접근/수정 불가_ )



### 메서드 정리

- 메서드는 해당 함수에서 어떤 값을 활용하고 변경하는지에 따라 정의
  - 인스턴스는 모든 메서드를 호출할 수는 있지만, 인스턴스의 동작은 반드시 인스턴스 메서드로 정의
  - 클래스는 클래스 속성 접근 여부에 따라 클래스 메서드 또는 정적 메서드로 정의 

- 인스턴스 메서드
  - self 매개변수를 통해 동일한 객체의 속성과 메서드에 접근 가능
  - 클래스 자체에도 접근 가능
    - 클래스 상태도 수정가능 하지만, 하지말자.
- 클래스 메서드
  - cls 매개변수를 받음
  - cls 인자에만 접근하기 때문에 객체 인스턴스를 수정할 수 없음
- 스태틱 메서드
  - 임의 개수의 매개변수를 받지만, self, cls 매개변수를 사용할 수 없음
  - 인스턴스도 클래스 상태도 수정불가
  - 일반 함수처럼 동작하지만 클래스의 이름공간에 귀속
    - 주로 해당 클래스로 한정하는 용도로 사용

- 예시

  ```python
  class MyClass:
      def method(self):
          return 'instance method', self
      @classmethod
      def classmethod(cls):
          return 'class method', cls
      @staticmethod
      def staticmethod():
          return 'static method'
      
      
  obj = MyClass()
  obj.method()  # 'instance method', <__main__.MyClass at 0x...>
  MyClass.method(obj)  # 'instance method', <__main__.MyClass at 0x...>
  
  obj.classmethod()  # 'classmethod', __main__.MyClass
  MyClass.classmethod()  # 'classmethod', __main__.MyClass
  obj.staticmethod()  # 'static method'
  
  MyClass.method()  # TypeError
  ```

  

- 스태틱 메서드는 언제 쓸까?
  - 스태틱 메서드는 독립적인 메서드
  - 스태틱 메서드와 클래스 메서드는 개발자의 의도를 전달하는 동시에, 자신의 의도를 강제해서 버그로 인한 설계가 깨지지 않게 함
  - 즉, 객체 인스턴스와 클래스 상태에 접근할 수 없음을 보장
  - 코드 유지 보수에 도움
  - 또, 일반 함수처럼 실행할 수 있기 때문에 객체 지향과 절차 지향 스타일을 연결하는 역할



<br/>



## 상속

- 클래스는 상속이 가능
- 상속을 통해 객체 간의 관계 구축
- 부모 클래스의 속성과 메서드가 자식 클래스에 상속되므로 코드 재사용성이 높아짐



- `issubclass`, `isinstance`

- `super()` : 자식클래스에서 부모클래스를 사용하고 싶은 경우 사용

  ```python
  class Person:
  	def __init__(self, name, age, number):
          self.name = name
          self.age = age
          self.number = number
          
          
  class Student:
      def __init__(self, name, age, number, student_id):
          # Person 클래스
          super().__init__(name, age, number)
          self.student_id = student_id
  ```

  

### 메서드 오버라이딩

- 상속 받은 메서드를 재정의
  - 상속받은 클래스에서 같은 이름의 메서드로 덮어씀
  - 이때도 부모 클래스의 메서드를 실행하고 싶으면 `super` 활용



### 이름 공간

- 인스턴스 -> 자식 클래스 -> 부모 클래스 순으로 탐색



### 다중 상속

- 두 개 이상의 클래스를 상속받는 경우

  - 상속 받은 모든 클래스의 요소를 활용 가능
  - 중복된 속성이나 메서드가 있으면 상속 순서에 의해 결정

  

  