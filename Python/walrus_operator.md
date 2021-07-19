# Syntax :=

백준 문제를 풀다가 다른 분의 풀이에 := 와 같은 기호를 보게 됐다. 이게 뭘까

수학에서 정의내리는 기호랑 똑같이 생겼다.



그래서 검색해봤다.

[What's New in Python 3.8-Assignment expressions](https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions)

Python 3.8에 처음 나온 Syntax라고 한다. 바다코끼리랑 닮아서 "the walrus operator"라고 한다고 한다...

`NAME := value` 로 변수 할당하는 기호다.



예문을 보자.

```python
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
```

위와 같이 사용해 `len()`함수를 두 번 호출하는 걸 막을 수 있다.



while 문에서도 유용하게 사용될 수 있다고 한다.

```python
while (cmd := input(">>> ")) != 'quit':
    print(cmd)
```



너무 막 쓰면 가독성도 떨어지고 복잡해지니 적절히 쓰라고 한다.