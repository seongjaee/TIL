# C# 자습서 따라가기 - 목록 컬렉션

## 01. 목록 만들기

```C#
using System;
using System.Collections.Generic;

var names = new List<string> { "Seongjae", "Ana", "Felipe" };
foreach (var name in names)
{
  Console.WriteLine($"Hello {name.ToUpper()}!");
}
// Hello SEONGJAE!
// Hello ANA!
// Hello FELIPE!
```

- `List<T>` 형식, T에 요소의 형식을 지정한다.
- `List<T>`형식은 길이를 늘리거나 줄일 수 있어서, 요소를 추가하거나 제거할 수 있다.

## 02. 목록 콘텐츠 수정

- 인덱스 접근 : `[ ]`
- 추가 및 삭제
  - 추가 : `Add()`
  - 삭제 : `Remove()`

- 길이 반환 : `Count()`

## 03. 목록 검색 및 정렬

- `IndexOf()` : 항목 검색, 없으면 -1 반환
- `Sort()` : 정렬

## 04. 피보나치 수 목록 만들기

```c#
using System;
using System.Collections.Generic;

var fibo = new List<int> { 0, 1 };

for (int i = 0; i < 19; i++)
{
    fibo.Add(fibo[i] + fibo[i + 1]);
}

foreach (int x in fibo)
{
    Console.WriteLine(x);
}
```

