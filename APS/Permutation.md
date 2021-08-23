# 순열 구현하기

- 주어진 n개의 원소를 나열하기

```python
def f(i, N):
    if i == N:  # 순열 완성
        print(P)
    else:
        # i보다 오른쪽에 있는 숫자와 교환
        for j in range(i, N):
       		# P[i] 결정
            P[i], P[j] = P[j], P[i]
            
        	f(i + 1, N)
            
        	# P[i] 복구
            P[i], P[j] = P[j], P[i]
```

- 주어진 n개의 원소중 r개를 나열하기

```python
def f(i, N, r):
    if i == r:  # 순열 완성
        print(P[:r])
    else:
        # i보다 오른쪽에 있는 숫자와 교환
        for j in range(i, N):
       		# P[i] 결정
            P[i], P[j] = P[j], P[i]
            
        	f(i + 1, N, r)
            
        	# P[i] 복구
            P[i], P[j] = P[j], P[i]
```

