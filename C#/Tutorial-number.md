# C# 자습서 따라가기 - 숫자형

## 01. 정수

- 정수 연산

  ```c#
  int a = 18;
  int b = 6;
  int c = a + b;
  Console.WriteLine(c);  // 24
  ```

  - 더하기 :  `+`
  - 빼기 : `-`
  - 곱하기 : `*`
  - 나누기 : `/` - 몫 계산
  - 나머지 : `%`

- `int`형 최소 최대 한도

  `int` 형에는 최소 한도와 최대 한도가 있다. 해당 한도를 초과하면 **언더플로** 또는 **오버플로** 조건이 발생.

  `int`형 최대 최소 한도 알아보기

  ```c#
  int max = int.MaxValue;
  int min = int.MinValue;
  Console.WriteLine($"The range of integers is {min} to {max}");
  // The range of integers is -2147483648 to 2147483647
  ```

- 오버플로 확인

  ```c#
  int what = max + 3;
  Console.WriteLine($"An example of overflow: {what}");
  // An example of overflow: -2147483646
  ```

  최대 한도를 넘어가 가장 작은 정수로 _래핑_ 되었다.

## 02. 숫자 형식

- double 숫자 형식

  `double` 숫자 형식은 배정밀도 부동 소수점 수를 나타낸다.

  **부동 소수점** 수는 아주 크거나 작은 정수가 아닌 수를 나타낼 때 유용.

  **배정밀도** 는 값을 저장하는데 사용 되는 이진 자릿수를 설명하는 상대 용어.

  **배정밀도** 숫자의 이진 자릿수는 **단정밀도**의 두배

  **단정밀도** 숫자는 `float` 키워드로 선언. 

- double 숫자 형식 연산

  ```c#
  double a = 19;
  double b = 23;
  double c = 8;
  double d = (a + b) / c;
  Console.WriteLine(d);  // 5.25
  ```

- double 값의 범위

  ```c#
  double max = double.MaxValue;
  double min = double.MinValue;
  Console.WriteLine($"The range of double is {min} to {max}");
  // The range of double is -1.7976931348623157E+308 to 1.7976931348623157E+308
  ```

  `int` 보다 훨씬 크다.



## 03. 10진수 형식

- `decimal` 형식

  `decimal` 형식은 범위가 작지만`double`보다 전체 자릿수가 크다.

  ```C#
  decimal min = decimal.MinValue;
  decimal max = decimal.MaxValue;
  Console.WriteLine($"The range of the decimal type is {min} to {max}");
  // The range of the decimal type is -79228162514264337593543950335 to 79228162514264337593543950335
  ```

- `double`과 비교

  ```c#
  double a = 1.0;
  double b = 3.0;
  Console.WriteLine(a / b);
  // 0.3333333333333333
  
  decimal c = 1.0M;
  decimal d = 3.0M;
  Console.WriteLine(c / d);
  // 0.3333333333333333333333333333
  ```

  `double`보다 자릿수가 크다는 걸 확인할 수 있다.

  `decimal` 형식을 사용하려면 숫자 뒤에 `M`접미사를 붙여 `decimal`임을 나타내야한다.

  >  `M`은 double 과 decimal 사이의 가장 시각적으로 고유한 m으로 선택된 거다.

- `Math.PI`

  Pi의 상수. `double` 형식이다.

  ```c#
  double pi = Math.PI;
  double radius = 2.5;
  
  Console.WriteLine(radius * radius * pi);        // 19.634954084936208
  Console.WriteLine(Math.Pow(radius, 2) * (pi));  // 19.634954084936208
  ```

  - `Math` 클래스 : 수학과 관련된 상수 및 정적 메서드 제공
  - C#에는 제곱 연산자가 따로 없고 `Math.Pow()` 메서드로 제곱연산이 가능하다.