# Dictionary `.get()` 활용

## `.get(key[, default])` 메서드

dict객체의 `.get()` 메서드는 key값을 통해 value를 가져오는 메서드이다.

단순히 key값을 이용한 조회`dict[key]` 와 다른 점은 해당하는 key가 없어도 에러를 발생시키지 않는다는 것이다. 

대신 `None`(default)을 반환한다.

특히 뒤의 선택인자로 key값이 없을경우 반환할 값을 결정할 수 있다.



**key값으로 조회할 경우**

```python
my_dict = {'A': '사과', 'B': '바나나', 'C': '체리'}

print(my_dicy['D'])  # 에러 발생
```

```
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
C:\Users\SEONGJ~1\AppData\Local\Temp/ipykernel_7084/1897060321.py in <module>
      1 my_dict = {'A': '사과', 'B': '바나나', 'C': '체리'}
      2 
----> 3 print(my_dict['D'])

KeyError: 'D'
```



** `.get()`을 이용할 경우 **

```python
my_dict = {'A': '사과', 'B': '바나나', 'C': '체리'}

print(my_dict.get('D'))
```

```
None
```

```python
my_dict = {'A': '사과', 'B': '바나나', 'C': '체리'}

print(my_dict.get('D', '해당하는 키가 없습니다.'))  # 키 값이 없을경우 반환할 값을 지정할 수 있음.
```

```
해당하는 키가 없습니다.
```





## Count에서 활용

중복되는 값이 있는 리스트에서 요소들의 개수를 세고 싶을 때 딕셔너리와 for문을 이용해 개수를 셀 수 있다.

```python
numbers = ['a', 'a', 'c', 'b', 'e', 'c', 'd', 'e', 'b']

cnt_dict = {}
for num in numbers:
    if num in cnt_dict:
        cnt_dict[num] += 1
    else:
        cnt_dict[num] = 1
        
print(cnt_dict)
```

```
{'a': 2, 'c': 2, 'b': 2, 'e': 2, 'd': 1}
```

딕셔너리에 아직 추가되지 않은 값이라면 1을 부여하고

이미 추가된 값이라면 1을 더해준다.



`.get()`을 이용하면 `if else` 문 없이도 똑같은 로직을 만들 수 있다.

```python
numbers = ['a', 'a', 'c', 'b', 'e', 'c', 'd', 'e', 'b']

cnt_dict = {}
for num in numbers:
    cnt_dict[num] = cnt_dict.get(num, 0) + 1
        
print(cnt_dict)
```

```
{'a': 2, 'c': 2, 'b': 2, 'e': 2, 'd': 1}
```

`.get()` 을 이용해 키값이 없다면 0을, 있다면 value값을 가져와 거기에 1을 더해준다.

그리고 그 값을 새로운 value값으로 할당해준다.



비슷한 예로 문자열의 문자들의 인덱스가 담긴 리스트를 구할 수 있다.

```python
words = 'pineapplepen'
index_dict = {}

for idx, char in enumerate(words):
    index_dict[char] = index_dict.get(char, []) + [idx]
    
print(index_dict)
```

```
{'p': [0, 5, 6, 9], 'i': [1], 'n': [2, 11], 'e': [3, 8, 10], 'a': [4], 'l': [7]}
```