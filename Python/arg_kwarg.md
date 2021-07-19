# *args 와 **kwargs의 의미

공식 문서들을 보다보면 함수의 매개변수에 *args나 **kwarg가 붙어있는 걸 볼 수 있다.

이게 무슨 의미일까



## *args, 가변 인자

함수에 전달할 인자의 개수를 고정하지 않을 때 사용한다.

가변 개수의 인자를 함수에 넘겨주고 싶을 때 사용하면 된다.

함수를 정의할 때, *args는 다른 변수들보다 뒤에 있어야한다.

```python
def foo(x, *args):
    print(x)
    print(args)
    
foo(1, 2, 3, 4)
```



```python
output :
1
(2, 3, 4)
```

함수가 *args로 전달받은 인자들은 튜플로 전달된다.



<br/>



## **kwargs, 키워드 가변 인자

키워드로 지정된 가변 개수의 인자를 넘겨주고 싶을 때 사용하면 된다.

역시 함수를 정의할 때, **kwargs는 다른 변수들보다 뒤에 있어야한다.

*args보단 앞에다.

```python
def goo(x, y, **kwargs):
    print(x)
    print(y)
    print(kwargs)

goo(1, 2, a='apple', b='banana', c=100)
```



```python
output : 
1
2
{'a': 'apple', 'b': 'banana', 'c': 100}
```

함수가 **kwargs로 전달받은 인자들은 딕셔너리로 전달된다.