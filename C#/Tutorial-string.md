# C# 자습서 따라가기 - 문자열 



## 01. 변수 선언 및 사용

- 변수 선언

  ```c#
  string Friend = "Bill";     // 문자열 변수 선언
  Console.WriteLine(Friend);  // 문자열 출력
  ```

- 변수 재할당

  ```c#
  Friend = "Maira";  // Friend에 이제 "Maria"가 저장됨
  Console.WriteLine(Friend);  // 문자열 출력
  ```

<br/>

## 02. 문자열 작업

- 문자열 보간, `$ {}`

  ```c#
  Console.WriteLine($"Hello {Friend}");  // 문자열 앞에 $으로 문자열 보간
  ```

- 문자열 길이 속성, `Length`

  ```c#
  // Length는 문자열 속성, 문자열 길이 반환
  Console.WriteLine($"The name {Friend} has {Friend.Length} letters")
  ```

- 문자열 공백 제거 메서드, `Trim()`

  ```c#
  string greeting = "      Hello World!       ";
  Console.WriteLine($"[{greeting}]");
  // [      Hello World!       ]
  
  string trimmedGreeting = greeting.TrimStart();
  Console.WriteLine($"[{trimmedGreeting}]");
  // [Hello World!       ]
  
  trimmedGreeting = greeting.TrimEnd();
  Console.WriteLine($"[{trimmedGreeting}]");
  // [      Hello World!]
  
  
  trimmedGreeting = greeting.Trim();
  Console.WriteLine($"[{trimmedGreeting}]");
  // [Hello World!]
  ```

- 문자열 치환 메서드, `Replace()`

  ```c#
  string sayHello = "Hello World!";
  Console.WriteLine(sayHello);
  // Hello World!
  
  sayHello = sayHello.Replace("Hello", "Greetings");
  Console.WriteLine(sayHello);
  // Greetings World!
  ```

- 문자열 대문자 or 소문자 지정 메서드, `ToUpper()`, `ToLower()`

  ```c#
  string sentence = "Apple is red!";
  Console.WriteLine(sentence.ToUpper());
  // APPLE IS RED!
  
  Console.WriteLine(sentence.ToLower());
  // apple is red!
  ```

<br/>

## 03. 문자열 검색

- 문자열 포함 여부 확인, `Contains()`

  ```c#
  string songLyrics = "You say goodbye, and I say hello";
  Console.WriteLine(songLyrics.Contains("goodbye"));  // True
  Console.WriteLine(songLyrics.Contains("greetings"));  //False
  ```

- 시작 또는 끝 부분에 있는 하위 문자열 검색, `StartsWith()`, `EndsWith()`

  ```C#
  string songLyrics = "You say goodbye, and I say hello";
  Console.WriteLine(songLyrics.StartsWith("You"));      // True
  Console.WriteLine(songLyrics.StartsWith("goodbye"));  // False
  Console.WriteLine(songLyrics.EndsWith("hello"));      // True
  Console.WriteLine(songLyrics.EndsWith("goodbye"));    // False
  ```

  

