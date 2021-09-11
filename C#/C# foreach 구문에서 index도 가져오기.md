# C# foreach 구문에서 index도 가져오기

```C#
string[] arr = {"a", "b", "c", "d"};

foreach (var item in arr.Select((value, index) => (value, index)))
{
    var value = item.value;
    var index = item.index;
    
    Console.WriteLine($"arr[{index}] = {value}")
}
```



## [LINQ 구문](https://docs.microsoft.com/ko-kr/dotnet/csharp/programming-guide/concepts/linq/introduction-to-linq-queries)

