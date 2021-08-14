# 병합 정렬 (Merge sort)

- 리스트를 나눈 뒤 재귀적으로 정렬하고 다시 병합하는 분할 정복 방식.



## 정렬 과정

- 분할(divide) : 리스트를 절반으로 자른다.
- 정복(conquer) : 각 부분 리스트를 재귀적으로 정렬한다.
- 결합(combine) :  두 개의 부분 리스트를 하나로 병합한다.



## 예시

- ```python
  # 주어진 리스트
  [8, 5, 3, 6, 1, 4, 2, 7]
  ```

- 반으로 분할한다.

  ```python
  [8, 5, 3, 6], [1, 4, 2, 7]
  ```

  ```python
  [8, 5], [3, 6], [1, 4], [2, 7]
  ```

  ```python
  [8], [5], [3], [6], [1], [4], [2], [7]
  ```

- 길이가 1인 리스트는 정렬되어있다. 다시 병합할 때 크기를 비교하면서 정렬한다.

  ```python
  [5, 8], [3, 6], [1, 4], [2, 7]
  ```

  리스트를 병합할 때는 작은 값부터 차례대로 가져온다.

  ```python
  [3, 5, 6, 8], [1, 2, 4, 7]
  ```

  ```python
  [1, 2, 3, 4, 5, 6, 7, 8]
  ```



## 코드

[https://www.geeksforgeeks.org/merge-sort/](https://www.geeksforgeeks.org/merge-sort/)를 참고함.

```python
def merge_sort(arr):
    # 길이가 1이면 정렬되어있음
    if len(arr) == 1: return
    
    # 분할
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    # 정복
    merge_sort(left_arr)  # 왼쪽 정렬
    merge_sort(right_arr)  # 오른쪽 정렬
    
    # 병합
    l_idx = r_idx = a_idx = 0
    while l_idx < len(left_arr) and r_idx < len(right_arr):
        # 왼쪽 리스트와 오른쪽 리스트를 비교하면서 더 작은 값부터
        # 차례대로 arr에 저장
        if left_arr[l_idx] < right_arr[r_idx]:
            arr[a_idx] = left_arr[l_idx]
            l_idx += 1
        else:
            arr[a_idx] = right_arr[r_idx]
            r_idx += 1
        a_idx += 1
        
    # 위의 while문의 조건이 and이므로 왼쪽, 오른쪽 중 한쪽을 다 쓰면 종료됨
    # 아직 남아 있는 요소들도 뒤에 이어서 저장
    while l_idx < len(left_arr):
        arr[a_idx] = left_arr[l_idx]
        l_idx += 1
        a_idx += 1
        
    while r_idx < len(right_arr):
        arr[a_idx] = right_arr[r_idx]
        r_idx += 1
        a_idx += 1
```



## 정리

- 평균 시간 복잡도 : O(N logN)
- 최악 시간 복잡도 : O(N log N)
- 연결 리스트의 경우 가장 효율적이다.