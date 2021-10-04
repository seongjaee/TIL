# 힙 (heap)

- 완전 이진 트리에 있는 노드 중에서 키값이 가장 큰 노드나 가장 작은 노드를 찾기위한 자료구조

## 최대 힙

- 키값이 가장 큰 노드를 찾기 위한 완전 이진 트리
- 부모 노드 키값 > 자식 노드 키값
- 루트노드 : 키값이 가장 큰 노드



## 최소 힙

- 키값이 가장 작은 노드를 찾기 위한 완전 이진 트리
- 부모 노드 키값 < 자식 노드 키값
- 루트노드 : 키값이 가장 작은 노드





## 힙 연산

- 연산 후에도 완전 이진 트리가 유지되어야 함.

### 삽입

- 일단 삽입할 자리를 확장함.
- 확장한 자리에 삽입할 원소를 저장
- 새로운 원소와 부모를 비교
  - 부모 > 새로운 원소 : 종료 ( 최대 힙인 경우 )
  - 부모 < 새로운 원소 : 부모와 자리 바꾸기 
    - 부모가 없거나, 부모가 새로운 원소보다 클 때까지 반복

### 삭제

- 힙에서는 루트 노드의 원소만을 삭제
- 루트 원소 삭제
- 마지막 노드를 루트 노드로 함
- 루트 노드와 자식노드를 비교해 자식 노드 중 더 큰 값이 있으면 자리를 바꿈.





## 힙의 사용

- 최대, 최소를 구하는 건 sort를 이용해도 구할 수 있지 않을까
- 리스트를 sort하는 것과의 차이점
  - **삽입, 삭제의 속도 차이**
  - 리스트 중간에 새로운 값이 들어가야할 자리를 찾는 것도 오래 걸리는데, 중간에 새로운 값을 삽입하는 것도 오래걸린다.
  - 하지만 힙은 새로운 값을 맨 뒤에 붙인 후 자리를 찾아나가는데, 자리를 찾는 것도 log(N)번만에 가능하다.
  - 삭제에서도 마찬가지이다.
- 리스트 정렬은 언제나 같은 모양을 보장하지만, 힙은 입력 순서에 따라 모양이 달라질 수 있다.
- 따라서 힙은 제한적인 상황에서 사용할 수 있다.
- **삽입과 삭제가 빈번한 자료 구조의 최대 또는 최소 값을 접근해야할 때** 사용하면 좋다.





## 최소 힙 구현

```python
class MinHeap:
    def __init__(self):
        self.heap = []

    def __str__(self):
        return ' '.join(map(str, self.heap))

    def Add(self, data):
        # 마지막 인덱스
        i = len(self.heap)
        # 값 추가
        self.heap.append(data)

        while i > 0:
            parent = (i - 1) // 2
            # 부모보다 크거나 같으면 break
            if self.heap[parent] <= self.heap[i]:
                break
            # 더 작으면 스왑
            else:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                i = parent

    def Pop(self):
        # 비어있으면 에러 반환
        if not self.heap:
            raise IndexError('pop form empty heap')
            
        # 반환할 루트 노드
        root = self.heap[0]
        # 마지막 원소를 루트 노드로 하고 마지막 원소 제거
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        i = 0
        last = len(self.heap) - 1
        while i < last:
            child = 2*i + 1
            # 오른쪽이 더 작으면 오른쪽 이용
            if child < last and self.heap[child] > self.heap[child + 1]:
                child += 1

            # 부모가 더 작거나 같으면 break
            if child > last or self.heap[i] <= self.heap[child]:
                break

            # 스왑
            self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
            i = child
                
        return root


my_heap = MinHeap()

data = [3,7,5,6,1,2,4]

for d in data:
    my_heap.Add(d)

for i in range(7):
    print(my_heap.Pop())
    
"""
1
2
3
4
5
6
7
"""
```

