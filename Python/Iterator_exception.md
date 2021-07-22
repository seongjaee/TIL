# Iterator 사용시 주의사항

[Python glossary-Iterator](https://docs.python.org/ko/3/glossary.html#term-iterator)



## 마주친 문제

알고리즘 문제를 풀다가 알 수 없는 예외를 마주쳤다.

아래와 같은 로직의 코드였다.

```python
from itertools import combinations

combs = combinations(range(5), 2)

words = ['apple', 'local', 'group', 'glove']
for word in words:
    for x, y in combs:
        print(word[x], word[y])
```

내가 기대한 것은 `words` 안의 `word` 들마다 2개의 문자씩을 출력하는 것이었다.

하지만 실제로 출력된 것은

```
a p
a p
a l
a e
p p
p l
p e
p l
p e
l e
```

`words`의 첫번째 요소인 `'apple'` 에서만 2개의 문자씩을 출력했다.



문제의 원인은 `combinations`로 만든 iterator 객체  `combs`였다.

파이썬 공식문서에 떡하니 써있는 예외였다.

>iterator (이터레이터)
>
>데이터의 스트림을 표현하는 객체. 
>
>....
>
>더 이상의 데이터가 없을 때는 대신 `StopIteration` 예외를 일으킵니다. 이 지점에서, 이터레이터 객체는 소진되고, 이후의 모든 `__next__()` 메서드 호출은 `StopIteration` 예외를 다시 일으키기만 합니다. 
>
>...
>
> 중요한 예외는 여러 번의 이터레이션을 시도하는 코드입니다. (`list`) 같은 컨테이너 객체는 `iter()` 함수로 전달하거나 `for` 루프에 사용할 때마다 새 이터레이터를 만듭니다. 이런 것을 이터레이터에 대해서 수행하려고 하면, 지난 이터레이션에 사용된 이미 소진된 이터레이터를 돌려줘서, 빈 컨테이너처럼 보이게 만듭니다.

이터레이터는 한번 이터레이션에 사용되면 소진되어 빈 컨테이너처럼 보이게 된다고 한다.

그래서 위의 코드에서 한번 이터레이션에 소진된 `comb`가 빈 컨테이너가 되어 `'local'` 문자열부터는 아무것도 출력되지 않은 것이다.

