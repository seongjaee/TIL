# 완전검색과 조합적 문제

## 브루트 포스

- 문제를 해결하기 위한 간단하고 쉬운 접근법
- 대부분의 문제에 적용 가능
- 상대적으로 빠른 시간에 알고리즘 설계를 할 수 있다.
- 자료의 크기가 작다면 유용
- 알고리즘의 효율성을 판단하기 위한 척도

<br/>

## 완전 검색으로 시작하기

- 모든 경우의 수를 테스트하기 때문에 속도는 느리지만 해답을 찾을 확률이 큼.
- 이를 기반으로 그리디 기법이나 동적계획법을 이용해 효율적인 알고리즘 찾기
- 우선 완전 검색으로 접근하여 해답을 도출한 후, 성능 개선을 위해 다른 알고리즘을 사용해 해답 확인.



<br/>

## 순열 생성

### 최소 변경을 통한 방법

- Johnson-Trotter 알고리즘



### 재귀 호출을 통한 순열 생성

```python
# arr : 데이터 저장된 배열
# n : 원소의 개수

def perm(n, k):
    if k == n:
        # 완성. 작업 수행
        print(arr)
    else:
       	for i in range(k, n):  # i번째 자리 결정
            arr[k], arr[i] = arr[i], arr[k]  # swap
            perm(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]  # 복구
            
arr = [1, 2, 3]
perm(3, 0)
"""
output:
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 2, 1]
[3, 1, 2]
"""
```



### 사전 순서 순열

- 사용할 숫자 배열 `arr`를 저장
- 사용된 숫자의 위치를 표시할 배열 `used` 준비
- `used`의 왼쪽부터 순회하며 사용하지 않은 숫자를 찾아 표시하고, 해당 숫자를 복사
- 다음 자리 정하기 위해 재귀 호출
- 모두 골랐으면 출력

```python
# arr : 데이터 저장된 배열
# n : 총 원소의 개수
# m : 사용할 원소의 개수
# used : 사용 여부
# p : 순열 배열

def perm(n, m, k):
    if k == m:  # m 개를 모두 골랐다면
        # 완성. 작업 수행
        print(p)
    else:
       	for i in range(n):  # 주어진 숫자의 개수만큼
            if not used[i]:    # 사용된 적 없으면
                p[k] = arr[i]
                used[i] = True
                perm(n, m, k+1)
                used[i] = False
                
                
arr = [1, 2, 3, 4]
p = [0] * 3
used = [False] * 3
perm(4, 3, 0)
"""
output:
[1, 2, 3]
[1, 2, 4]
[1, 3, 2]
[1, 3, 4]
[1, 4, 2]
[1, 4, 3]
[2, 1, 3]
[2, 1, 4]
[2, 3, 1]
[2, 3, 4]
[2, 4, 1]
[2, 4, 3]
[3, 1, 2]
[3, 1, 4]
[3, 2, 1]
[3, 2, 4]
[3, 4, 1]
[3, 4, 2]
[4, 1, 2]
[4, 1, 3]
[4, 2, 1]
[4, 2, 3]
[4, 3, 1]
[4, 3, 2]
"""
```



<br/>

## 부분 집합

- 집합에 포함된 원소 선택
- 많은 알고리즘들이 원소들의 그룹에서 최적의 부분 집합을 찾는것
  - 배낭 짐싸기
- N개의 원소를 포함한 집합
  - 자기 자신과 공집합 포함한 모든 부분집합의 개수는 2^n개
  - 원소의 수가 증가하면 부분집합의 개수는 지수적으로 증가

### 부분 집합 생성방법

- 바이너리 카운팅
  - 원소 수에 해당하는 N개의 비트열을 이용
  - n번째 비트값이 1이면 n번째 원소가 포함되었음을 의미

```python
arr = [3, 6, 4, 2, 1]
n = len(arr)

for i in range(1 << n):
    for j in range(n):    # 원소 수만큼 비트 비교
        if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=' ')
    print()
```



<br/>

## 조합 생성

- n, r 에 대해 `tr[r-1] = an[n-1]`
  - 기존 배열 `an`의 `n-1`인덱스의 값을 조합 배열 `tr`의 `r-1`에 저장.
  - comb(n, r)은 언제나 `n-1` 값을 고른 경우 그리고 남은 자리는 `r-1`개라고 생각.
- comb(n, r)을 재귀적으로 표현하면
  - comb(n-1, r) , comb(n-1, r-1)
  - comb(n-1, r) 

```python
def comb(n, r):
    if r == 0 : print(arr)
    elif n < r : return
    else:
        tr[r-1] = an[n-1]
        comb(n-1, r-1)
        comb(n-1, r)
```



```python
def nCr(n, r, s, k): # n개에서 r개 고름. s : 선택할 수 있는 구간 시작, k: 현재 고른 개수
	if k == r:
        print(*comb)
    else:
        for i in range(s, n-r+k+1): # n-r+k : 선택할 수 있는 구간의 끝
            comb[k] = i  # k번째를 고름
            nCr(n, r, i+1, k+1)  # 그다음
```

