# 문제

```python
A = [[0]*3]*2 # [[0,0,0],[0,0,0]]
B = [[0 for _ in range(3)] for _ in range(2)] # [[0,0,0],[0,0,0]]

print(A)
print(B)

A[1][1] = 1
B[1][1] = 1

print(A)
print(B)
```

```
[[0, 0, 0], [0, 0, 0]]
[[0, 0, 0], [0, 0, 0]]
[[0, 1, 0], [0, 1, 0]]
[[0, 0, 0], [0, 1, 0]]
```



이런 일이 일어나는 이유를 찾아보자.

```python
A = [[0]*3]*2 # [[0,0,0],[0,0,0]]
B = [[0 for _ in range(3)] for _ in range(2)] # [[0,0,0],[0,0,0]]

print(id(A[0]), id(A[1]))
print('='*28)
print(id(B[0]), id(B[1]))
```

```
2425334689664 2425334689664
============================
2425334669952 2425334652352
```



`A[0]` 과 `A[1]` 의 `id` 가 같지만, `B[0]` 과 `B[1]` 의 `id`는 다르다!

A의 경우 리스트에  `*`  연산은 리스트 내부 원소들이 복사가 되는데 값이 복사가 되는게 아니라 주소를 복사해 온다.

반면 B의 경우 list comprehension으로 같은 동작을 반복하면서 같은 값을 가진 객체를 새로 생성했기 때문에 `id`가 다르다.

