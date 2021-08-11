# 검색 (Search)

- 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
- 탐색 키 : 자료를 구별하여 인식할 수 있는 키. 찾고자 하는 것.

- 검색의 종류
  - 순차 검색
  - 이진 검색
  - 해쉬

<br/>

## 순차 검색(Sequential Search)

- 일렬로 되어있는 자료를 순서대로 검색
- 가장 간단하고 직관적
- 배열이나 연결 리스트 등 순차 구조에서 유용
- 구현이 쉽지만, 검색 대상의 수가 많으면 비효율적

### 정렬되지 않은 경우

- 첫 번째 원소부터 차례대로 검색
- 중간에 찾으면 인덱스 반환
- 마지막까지 못 찾으면 검색 실패

- 평균 비교 횟수는 (n+1) / 2

- 시간복잡도 O(n)

#### 구현

```python
def sequential_search(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i += 1
        
    if i < n: return i
    else: return -1
```



### 정렬되어 있는 경우

- 오름차순인 경우,
- 원소의 값이 검색 대상보다 크면 찾는 원소가 없으므로 검색 종료 
- 검색 실패를 반환하면 평균 비교 횟수는 반으로 줄어든다.
- 시간 복잡도 O(n)

#### 구현

```python
def sequential_search(a, n, key):
    i = 0
    while i < n and a[i] < key:
        i += 1
        
    if i < n and a[i] == key:
        return i
    else:
        return -1
```



<br/>



## 이진 검색 (Binary Search)

- 자료의 가운데에 있는 항목의 키값과 비교 후 다음 검색의 위치를 결정. 검색 반복
- 검색 범위가 반으로 줄어 빠르게 검색 가능
- 자료가 정렬된 상태여야함.

### 과정

- 자료의 중앙 원소를 고름
- 중앙 원소과 목표 값 비교
- 작으면 자료의 왼쪽 반에 대해 새로 검색, 크면 자료의 오른쪽 반에 대해 새로 검색
- 찾을 때 까지 반복

#### 구현

```python
def binary_search(arr, key):
    stary = 0
    end = len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return False
```



