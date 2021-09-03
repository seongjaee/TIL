# [StringBuilder 클래스](https://docs.microsoft.com/ko-kr/dotnet/api/system.text.stringbuilder?view=net-5.0)

- namespace : `System.Text`
- 변경할 수 있는 문자열

- String 클래스는 변경할 수 없는 문자열임.

  String.Concat은 실제로는 변수의 값을 변경하는 것임.

- 따라서 문자열을 여러 번 수정하는 경우, 성능 저하 발생 가능



- 그럼에도 String을 사용하는 게 좋은 경우
  - 문자열의 수정 내용 수가 적은 경우
  - 문자열 작성하는 동안 광범위한 검색 작업을 하는 경우
    - StringBuilder에는 `IndexOf` 와 `StartWith`메서드가 없음
  - concate 작업이 고정된 횟수만 진행되는 경우, 컴파일러가 한 번의 연산 작업으로 처리할 수 있음.

- `Capacity` 속성 : 문자열 용량, 기본값으로 16자 최대 20억.
  - 만약 기본 용량을 넘어서면 새로운 메모리 할당이 일어나고 용량이 두 배로 늘어남.

## 속성

- `Capacity` : 현재 인스턴스에  할당된 메모리의 최대 문자수
- `Chars[Int32]` : 인덱스 위치의 문자
- `Length` : 길이
- `MaxCapacity` : 최대 용량

## 메서드

- `Append()` : 문자열에 추가
- `Append(Char, Int32)` : `Char`를 `Int32`개 추가
- `AppendJoin(Char, String[])` : 각 문자열 사이에 지정된 문자 구분 기호를 사용하여 추가하려 `String[]`의 문자열을 연결
- `Clear()` : 모든 문자 제거
- `Insert(Int32, )` : 지정된 위치에 문자열 삽입
- `Remove(Int32, Int32)` : 지정된 범위 제거
- `Replace(Char, Char)` : 지정된 문자를 지정된 문자로 변경
- `ToString()` : String으로 변환