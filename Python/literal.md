# Literal

[리터럴(Literal)](https://ko.wikipedia.org/wiki/%EB%A6%AC%ED%84%B0%EB%9F%B4)은 소스 코드의 *고정된 값* 을 대표하는 용어.

값이 변하지 않는 데이터?

## String literals

`''`, `""`, `""" """`으로 생성

```python
s1 = "성재"
s2 = '123'
s3 = """Hello
World!
"""
```



## Numerial literals

- 숫자형

```
x = 10
y = 0b1101
z = 1 + 2j
w = 3.14
```



## Boolean literals

- 참/거짓

```python
x = True
y = False
```



## Special literals

- None

```python
val = None
```



## Literal Collection

- list : `[]` 로 닫혀있고 각 원소들이 `,` 로 구분됨.

  ```python
  # List literals
  numbers = [1, 2, 3, 4]
  empty_list = []
  ```

- dict : `{}` 로 닫혀있고 각 키-값 쌍들이 `,`로 구분됨.

  ```python
  # Dictionary literals
  alphabets = {'a': 'apple', 'b': 'banana', 'c': 'cat'}
  empty_dict = {}
  ```

- set : `{}` 로 닫혀있고 각 원소들이 `,`로 구분됨.

  ```python
  # Set literals
  animals = {'dog', 'cat', 'pig'}
  # 빈 set은 리터럴 없음
  ```

- tuple : `()` 로 닫혀있고 각 원소들이 `,` 로 구분됨.

  ```python
  # Tuple literals
  fruits = ('orange', 'cherry')
  empty_tuple = ()
  ```

