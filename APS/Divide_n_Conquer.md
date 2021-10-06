# 분할 정복

- 유래
  - 1805년 아우스터리츠 전투 나폴레옹의 전략
  - 연합군을 둘로 나눠 한 부분씩 격파
- 설계전략
  - 분할(Divide) : 해결할 문제를 여러 개의 작은 부분으로 나눈다.
  - 정복(Conquer) : 나눈 작은 문제를 각각 해결한다.
  - 통합(Combine) : (필요하면) 해결된 해답을 모은다.
- Top-down 접근
  - 문제를 부분 문제로 분할
  - 부분 문제를 해결
  - 해결한 해답을 결합



## 거듭 제곱

- 반복 알고리즘:  O(N)

- 분할 정복 알고리즘 : O(log N)

  - ```python
    def recursiv_power(x, n):
        if n == 1: return x
        if n % 2 == 0:
            y = recursive_power(x, n/2)
            return y * y
        else:
            y = recursive_power(x, (n-1)/2)
            return y * y * x
    ```



## 병합 정렬

- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- 분할 정복 알고리즘을 활용하는 top-down 방식
- 최소 크기의 부분집합이 될 떄까지 분할한 후 병합하며 정렬한다.
- O(N log N)

- 분할 과정 알고리즘

  ```
  Merge_sort(LIST m):
  	IF length(m) == 1: RETURN m
  	
  	LIST left, right
  	middle = length(m) / 2
  	FOR x in m before middle
  		add x to left
      FOR x in m after or equal middle
      	add x to right
      	
    	left = merge_sort(left)
    	right = merge_sort(right)
    	
    	RETURN merge(left, right)
  ```

- 병합 과정 알고리즘

  ```
  merge(LIST left, LIST right)
  	LIST result
  	
  	WHILE length(left) > 0 OR length(right) > 0
  		IF length(left) > 0 AND length(right) > 0
  			IF first(left) <= first(right)
  				append popfirst(left) to result
              ELSE
              	append popfirst(right) to result
          ELIF length(left) > 0
          	append popfirst(left) to result
         	ELIF length(right) > 0
          	append popfirst(right) to result
      RETURN result
  ```

  

## 퀵 정렬

- 주어진 배열을 두 개로 분할하고, 각각을 정렬한다.

- 병합 정렬과 다른점

  - 분할 시 기준 아이템(pivot)을 중심으로, 더 작은 건 왼쪽, 큰 건 오른쪽에 위치
  - 퀵 정렬에는 병합 과정이 없음.
  - 피봇이 중간에 올 수록 분할 정복의 효과가 커짐.
  - 피봇 선택
    - 왼쪽 끝, 오른쪽 끝, 임의의 세개의 중간값 등.

- ```
  quickSort(A[], l, r)
  	if l < r
  		s = partition(a, l, r)  // 분할 작업
  		quickSort(A[], l, s-1)
  		quickSort(A[], s+1, r)
  ```

- Hoare-Partition 알고리즘

  ```
  partition(A[], l, r)
  	p = A[l]  // p : 피봇 값
  	i = l, j = r
  	WHILE i <= j
  		WHILE i <= j and A[i] <= p : i++
  		WHILE i <= j and A[j] >= p : j--
  		IF i < j : swap(A[i], A[j])
  	swap(A[l], A[j])
  	RETURN j
  ```

- 아이디어

  - 피봇 값들보다 큰 값은 오른쪽, 작은 값은 왼쪽에 위치하도록함

  - 피봇을 두 집합의 가운데에 위치시킴.

  - i는 왼쪽부터 시작해서 P보다 큰 값을 찾음.

    j는 오른쪽부터 시작해서 P보다 작은 값을 찾음.

  - 그 두 값의 위치를 바꿈.

  - i와 j가 교차하게 되면, i와 j 사이가 피봇을 기준으로 하는 작은 값과 큰 값의 경계하는 뜻.

  - 따라서 j와 피봇의 위치를 바꾸면서 경계에 피봇이 위치하도록함.

- Lomuto partition 알고리즘

  ```
  partition(A[],p, r)
  	x = A[r]
  	i = p - 1
  	
  	FOR j in p -> r-1
  		IF A[j] <= x
  			i++, swap(A[i], A[j])
      
      swap(A[i+1], A[r])
      RETURN i + 1
  ```

- 아이디어

  - i와 j 사이에 P보다 큰 원소가 위치하게 됨.

  - i : 피봇보다 작은 원소중 가장 오른쪽을 가리킴.

  - j를 하나씩 키워가면서 피봇보다 작은 원소가 나오게 되면 현재 i를 1키우고 

    i와 j에 위치한 원소를 교환한다.



## 이진 검색(Binary Search)

- **정렬되어있는** 자료의 가운데에 있는 항목의 키값과 비교하여 다음 검색의 위치를 결정해 검색을 진행함.
- 과정
  - 중앙에 있는 원소 고르기
  - 중앙 원소 값과 목표 값 비교
  - 목표값보다 작으면 왼쪽 반에 대해 검색 수행, 목표값보다 크면 오른쪽 반에 대해 검색 수행,
  - 위의 과정 반복

- 반복 구조 알고리즘

  ```
  binarySearch(n, S[], key)
  low = 0
  high = n - 1
  
  WHILE low <= high AND location = 0
  	mid = ( high + low ) // 2
  	
  	IF S[mid] == key
  		RETURN mid
  	ELIF S[mid] > key
  		high = mid - 1
      ELSE
      	low = mid + 1
      	
  RETURN -1
  ```

- 재귀 구조 알고리즘

  ```
  binarySearch(S[], low, high, key)
  	IF low > high
  		RETURN -1
  	ELSE
  		mid = (low + high) / 2
  		IF key == S[mid]
  			RETURN mid
  		ELIF key < a[mid]
  			RETURN binarySearch(S[], low, mid - 1, key)
  		ELSE
  			RETURN binarySearch(S[], mid + 1, high, key)
  ```

  

## 분할 정복의 활용

- 병합 정렬은 외부 정렬의 기본. 멀티 코어 CPU나 다수의 프로세서에서 정렬 알고리즘 병렬화를 위해 병합 정렬 알고리즘 활용

- 퀵 정렬은 매우 큰 입력 데이터에 대해 좋은 성능을 보임

  

