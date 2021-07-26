# 데이터 구조

>  Algorithms + Data Structures = Programs , Niklaus Wirth



## 문자열(String)

### 특징

**Sequence of characters** , 문자들의 시퀀스

- Immutable
- Ordered
- Iterable



### 인덱싱과 슬라이싱

- 인덱싱
  - 왼쪽부터 0, 1, 2, ...
  - 오른쪽부터 -1, -2, -3, ...
- 슬라이싱
  - s[start : stop : step]으로 슬라이싱
  - s[::]로 복사, s[::-1]로 뒤집기 가능



### 메서드

- `.find(x)` : `x`의 첫번쨰 위치 반환, 없으면 `-1`반환
- `.index(x)` : `x`의 첫번쨰 위치 반환. 없으면 ValueError
- `.replace(old, new[,count])`: 바꿀 대상(`old`)을 새로운 글자(`new`)로 바꿔 복사본 반환, `count` 지정으로 해당 개수만큼만 바꿈.
- `.strip([chars])` : 특정 문자들을 지정하면 양쪽(`strip`), 오른쪽(`rstrip`), 왼쪽(`lstrip`)을 제거한 후 복사본 반환. 문자열을 지정하지 않으면 공백을 제거.
- `.split(sep=None)` : 문자열을 특정 단위로 나눠 리스트로 반환, `sep`을 지정하지 않으면 연속된 공백을 기준으로 나눔.
- `'separator'.join(iterable)` : iterable 컨테이너 요소들을 separator로 합쳐 문자열 반환

- `.capitalize()` : 첫 문자만 대문자, 나머지는 소문자로
- `.title()`: '  나 공백 이후의 단어 첫 문자를 대문자로
- `.upper()` : 전부 대문자로
- `.lower()` : 전부 소문자로
- `.swapcase()` : 대문자와 소문자를 변경.
- `.isalpha()` : 알파벳 문자 여부(유니코드 상 letter인지 확인, 한국어도 포함)
- `.isupper()` : 대문자 여부
- `.islower()` : 소문자 여부
- `.istitle()` : 타이틀 형식 여부

## 리스트(List)

**순서가 있는 시퀀스, 인덱스로 접근**

- Mutable
- Ordered
- Iterable



### 인덱싱과 슬라이싱

- 인덱싱
  - 왼쪽부터 0, 1, 2, ...
  - 오른쪽부터 -1, -2, -3, ...
- 슬라이싱
  - s[start : stop : step]으로 슬라이싱
  - s[::]로 복사, s[::-1]로 뒤집기 가능



### 메서드

- `.append(x)`: 리스트의 끝에 값 추가
- `.extend(iterable)` : 리스트에 iterable의 요소들을 추가함
- `.insert(i, x)` : 정해진 위치 `i`에 값 `x`를 추가, `i`가 리스트 길이보다 크면 맨 뒤에 추가
- `.remove(x)`: 리스트에서 값이 `x`인 첫번째 항목 삭제, 값이 없으면 ValueError
- `.pop(i)` : 정해진 위치 `i`에 있는 값을 삭제하고, 그 항목을 반환. `i`가 정해지지 않으면 마지막 항목 삭제하고 반환.
- `.clear()` : 리스트의 모든 항목 삭제
- `.index(x)` : 처음으로 나오는 `x`의  index 값 반환. `x`가 없으면 ValueError
- `.count(x)` : 리스트에 포함된 `x`의 개수를 반환.
- `.sort()` : 원본 리스트를 정렬, None 반환, `sorted` 함수는 정렬된 복사본 반환.
- `.reverse()` : 원본 리스트의 순서를 반대로 뒤집음

#### 리스트 복사

**얕은 복사(Shallow copy)**

- Slice 연산자로 같은 원소를 가진 리스트지만 연산된 결과를 복사(다른 주소)

  - `b = a[:]`

- `list()`로 같은 원소를 리스트지만 연산된 결과를 복사

  - `b = list(a)`

    

**얕은 복사의 한계**

- 복사라는 리스트의 원소가 주소를 참조하는 경우

  - ```python
    a = [1, 2, [3, 4]]
    b = a[:]
    print(f'a : {a}, b : {b}')   
    #a : [1, 2, [3, 4]], b : [1, 2, [3, 4]]
    
    b[2][0] = 5
    print(f'a : {a}, b : {b}')  
    # a : [1, 2, [5, 4]], b : [1, 2, [5, 4]]
    ```

  - 리스트의 원소가 참조하고 있는 주소는 바뀌지 않음

    

**깊은 복사(Deep copy)**

`copy` 모듈 안에 `deepcopy` 함수 사용

- ```python
  import copy
  
  a = [1, 2, [3, 4]]
  b = copy.deepcopy(a)
  print(f'a : {a}, b : {b}')   
  # a : [1, 2, [3, 4]], b : [1, 2, [3, 4]]
  
  b[2][0] = 5
  print(f'a : {a}, b : {b}')  
  # a : [1, 2, [3, 4]], b : [1, 2, [5, 4]]
  ```



### List comprehension

표현식과 제어문을 통해 특정한 값을 가진 리스트를 생성하는 법

- `[<expression> for <변수> in <iterable>]`
- `[<expression> for <변수> in <iterable> if <condition>]`
- `[<expression1> if <조건식> else <expression2> for <변수> in <iterable>]`



```python
[x for x in range(1, 11) if x%2 == 0]
# [2, 4, 6, 8, 10]
```



```python
girls = ['jane', 'ashley']
boys = ['justin', 'eric']

[(boy, girl) for boy in boys for girls in girls]
```

List Comprehension은 가독성이 떨어질 수 있음.



### Built-in Function

- map
  - `map(function, iterable)` : iterable의 모든 요소에 `function`을 적용하고, 그 결과를 map object로 반환.
- filter
  - `filter(function, iterable)` : iterable의 모든 요소에 `function`을 적용하고, 그 결과가 `True`인 것들을 filter object로 반환
- zip
  - `zip(*iterable)` : 여러 개의 iterable을 모아 인덱스가 같은 것 끼리 묶은 튜플을 원소로 하는 zip object 반환, 길이가 더 짧은 걸 기준



## 세트(Set)

중복 없이 순서가 없는 구조

- Mutable
- Unordered
- Iterable



### 메서드

- `.add(elem)` : 값을 추가
- `.update(*others)` : 여러 값을 추가
- `.remove(elem)` : 값을 삭제, 없으면 KeyError
- `.discard(elem)` : 값을 삭제, 없어도 에러 발생하지 않음
- `.pop()` : 임의의 원소를 제거해 그 항목을 반환. 값이 없으면 KeyError



## 딕셔너리(Dictionary)

Key와 Value로 구성된 데이터 구조

- Mutable
- Unordered
- Iterable



### 메서드

- `.get(key, [,default])` : `key`에 대응하는 `value`를 가져옴, `key`가 없으면 KeyError 대신 `default`를 반환
- `.pop(key, [,default])` : `key`가 있으면 제거하고 해당 값 반환, 없으면 `default`반환. `default`도 없으면 KeyError
- `.update()` : 값을 제공하는 key, value로 갱신(기존 key를 덮어씀)
  - `my_dict.update(key = value)`



### 딕셔너리의 순회

- 딕셔너리는 기본적으로 key를 순회
- 추가 메서드를 활용해 순회 가능
  - `.keys()` : Key로 구성된 결과
  - `.values()` : Value로 구성된 결과
  - `.items()` : (Key, Value)의 튜플로 구성된 결과



### Dictionary Comprehension

- `{key: value for <변수>  in <iterable>}`
- `{key: value for <변수>  in <iterable> if <조건식>}`



다음 딕셔너리 중 값이 70이상으로 구성된 새로운 딕셔너리를 작성

```python
dusts = {'서울': 72, '대전': 82, '구미': 29, '광주': 45}
```

```python
result = {}
for key, value in dusts.items():
    if value >= 70:
        result[key] = value
print(reuslt)
# {'서울': 72, '대전': 82}
```

```python
result = {key: value for key, value in dusts.items() if value >= 70}
print(result)
# {'서울': 72, '대전': 82}
```



Dictionary Comprehension도 가독성이 떨어지니 주의.

