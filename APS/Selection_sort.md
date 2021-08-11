# 선택 정렬 (Selection sort)

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택해 위치를 교환하는 방식

- 정렬 과정
  - 주어진 리스트의 최솟값을 찾는다.
  - 최솟값과 리스트의 맨 앞의 값과 위치를 교환한다.
  - 맨 앞을 제외한 나머지 리스트를 대상으로 반복한다.
- 시간 복잡도 : O(N^2)

## 구현

```python
def selection_sort(arr):
    for i in range(0, len(a)-1):
        min_idx = i
        for j in range(i+1, len(a)):
            if arr[min_idx] > a[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```



## 셀렉션 알고리즘

- 자료로부터 k번째로 큰 또는 작은 원소를 찾는 방법

- 선택 과정

  - 정렬 알고리즘을 이용해 자료 정렬
  - 원하는 순서에 있는 원소 가져오기

- k번째로 작은 원소를 찾는 알고리즘

  - 위의 선택 정렬을 k번까지 진행한다.
  - k가 작을 때 유용, O(kN)

  ```python
  def select(arr, k):
      for i in range(k):  # k까지만 진행
          min_idx = i
          for j in range(i+1, len(arr)):
              if arr[min_idx] > arr[j]:
                  min_idx = j
          arr[i], arr[min_idx] = arr[min_idx], arr[i]
      return arr[k-1]
  ```





## 정리

- 평균 수행 시간 : O(N^2)
- 최악 수행 시간 : O(N^2)
- 비교와 교환 방식
- 교환 횟수가 버블, 삽입 정렬보다 적다.

