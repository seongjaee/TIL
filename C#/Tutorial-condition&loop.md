# C# 자습서 따라가기 - 분기 및 루프

## 01. if 문

- `if` 문 사용

  ```c#
  int a = 5;
  int b = 6;
  if (a + b > 10)
  {
      Console.WriteLine("The answer is greater than 10.");
  }
  ```

  `if` 키워드 뒤에 조건문을 `()`안에 쓴다.

  C#에서는 들여쓰기와 공백을 중요하게 취급하지 않는다. 사용자의 가독성을 위한 것이다.

  일반적으로 모든 `if` 및 `else`절에서 중괄호를 사용해야한다.

- `if ~ else` 문사용

  ```c#
  int a = 5;
  int b = 3;
  if (a + b > 10)
  {
      Console.WriteLine("The answer is greater than 10");
  }
  else
  {
      Console.WriteLine("The answer is not greater than 10");
  }
  ```

- 논리 연산자
  - `==` 
  - `&&`
  - `||`

## 02. 루프

- `while` 문

  ```c#
  int counter = 0;
  while (counter < 5)
  {
    Console.WriteLine($"Hello World! The counter is {counter}");
    counter++;
  }
  // Hello World! The counter is 0
  // Hello World! The counter is 1
  // Hello World! The counter is 2
  // Hello World! The counter is 3
  // Hello World! The counter is 4
  ```

  `++` 는 **증가** 연산자. 값에 1을 더한 후 변수에 해당 값을 저장

- `do ... while` 문

  ```c#
  int counter = 0;
  do
  {
    Console.WriteLine($"Hello World! The counter is {counter}");
    counter++;
  } while (counter < 5);
  
  // Hello World! The counter is 0
  // Hello World! The counter is 1
  // Hello World! The counter is 2
  // Hello World! The counter is 3
  // Hello World! The counter is 4
  ```

  `do ... while` 문은 `while`문 뒤 코드를 실행하기 전에 `do` 안의 코드를 먼저 실행

  즉, 코드가 한 번은 반드시 실행됨

- `for` 문

  ```c#
  for(int counter = 0; counter < 5; counter++)
  {
    Console.WriteLine($"Hello World! The counter is {counter}");
  }
  // Hello World! The counter is 0
  // Hello World! The counter is 1
  // Hello World! The counter is 2
  // Hello World! The counter is 3
  // Hello World! The counter is 4
  ```

  `for` 문을 제어하는 세 가지 부분이 있음

  - **for 이니셜라이저** : `int counter = 0;`은 `counter`가 루프 변수임을 선언 첫번째 값을 `0`을 설정
  - **for 조건** : `counter < 5` 는 루프가 카운터 값이 5보다 작을 때 계속 실행됨을 선언
  - **for 반복기** : `counter++`는 `for`문 안의 블록을 실행 후 루프 변수 수정 방법을 선언

- `foreach` 문

  은 나중에

  

## 03. 중첩 루프

- 루프 안에 루프로 중첩 루프

  ```c#
  for (int row = 1; row < 4; row++)
  {
    for (char column = 'a'; column < 'd'; column++)
    {
      Console.WriteLine($"The cell is ({row}, {column})");
    }
  }
  // The cell is (1, a)
  // The cell is (1, b)
  // The cell is (1, c)
  // The cell is (2, a)
  // The cell is (2, b)
  // The cell is (2, c)
  // The cell is (3, a)
  // The cell is (3, b)
  // The cell is (3, c)
  ```

  - `char` 형식은 증가 및 감소 연산자도 지원.



## 04. 분기 및 루프 결합

- 1부터 20까지 3으로 나눠떨어지는 모든 정수 합계 구하기

  ```c#
  int total = 0;
  
  for (int num = 1; num < 21; num++)
  {
      if (num % 3 == 0)
      {
          total += num;
      }
  }
  Console.WriteLine(total);  // 63
  ```


  ```c#
  int total = 0;
  
  for (int num = 3; num < 21; num += 3)
  {
      total += num;
  }
  Console.WriteLine(total);  // 63
  ```

  

