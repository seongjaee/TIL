# 큐, Queue

## 큐의 특성

- 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
- 선입선출구조(First In First Out)
  - 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입된 원소는 가장 먼저 삭제

### 큐의 구조

- 머리(Front) : 저장된 원소 중 첫 번째 원소
- 꼬리(Rear) : 저장된 원소 중 마지막 원소

### 큐의 기본 연산

- 삽입 : enQueue
- 삭제 : deQueue

### 주요 연산

- createQueue() : 비어있는 큐 생성
- isEmpty() : 큐가 비어있는지 확인
- isFull() : 큐가 가득 찼는지 확인
- Qpeek() : 큐의 앞쪽(Front)에서 원소를 삭제 없이 반환



## 큐 구현

### 선형 큐

- 1차원 배열을 이용한 큐
  - 큐의 크기 = 배열의 크기
  - front : 첫번째 원소 인덱스
  - rear : 마지막 원소 인덱스
- 상태표현
  - 초기 : front = rear = -1
  - 공백 : front = rear
  - 포화 : rear = n-1
- 구현
  - 초기에 front = rear = -1
  - enQueue : rear += 1, rear에 요소 삽입
  - deQueue : front += 1, front에 요소 반환

#### 선형 큐의 문제점

- 삽입과 삭제 반복 시, 배열의 앞부분에 공간이 있음에도 rear=n-1이면 포화상태로 인식. 더 이상 삽입 진행 불가
- 그렇다고 연산 시마다 저장된 원소를 한 칸씩 앞으로 이동시키려고 하면 많은 시간이 소요됨.

#### 해결 방법

- 1차원 배열을 사용하되, 배열의 처음과 끝이 연결되어 원형 형태를 이룬다고 가정

### 원형 큐

- 초기 공백 상태 : front = rear = 0
- front와 rear의 위치가 n-1이 된 후에는 배열의 첫 인덱스인 0으로 이동 - > mod 이용

- 공백과 포화 구분을 위해 front 자리는 항상 비워둠
- 삽입 : (rear + 1) mod n
- 삭제 : (front + 1) mod n

- 공백 : front = rear
- 포화 : -(rear + 1) = front (mod n)

### 연결 큐

- 단순 연결 리스트를 이용한 큐
- 큐의 원소 : 단순 연결 리스트 노드
- 원소 순서 : 노드 연결 순서. 링크로 연결
- front : 첫 번째 노드를 가리키는 링크
- rear : 마지막 노드를 가리키는 링크

- 상태 표현
  - 초기 : front = rear = null
  - 공백 : front = rear = null

```python
# 단순 연결 리스트로 구현한 큐

class Queue:
    class _Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.rear = None
        self.size = 0

    @property
    def empty(self):
        if self.size > 0:
            return 0
        return 1

    @property
    def front(self):
        if self.size:
            return self.head.data
        return -1

    @property
    def back(self):
        if self.size:
            return self.rear.data
        return -1

    def push(self, X):
        node = self._Node(X)
        if self.empty:
            self.head = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size += 1

    def pop(self):
        if self.empty:
            return -1
        self.size -= 1
        temp = self.head.data
        self.head = self.head.next
        return temp
```



## 우선순위 큐

- 우선순위를 가진 항목들을 저장하는 큐
- 우선순위가 높은 순서대로 먼저 삭제

- 적용 분야
  - 시뮬레이션 시스템
  - 네트워크 트래픽 제어
  - 운영체제 테스크 스케줄링
- 구현
  - 배열 이용
  - 리스트 이용
- 기본 연산
  - 삽입 : enQueue
  - 삭제 : deQueue

### 배열을 이용한 우선순위 큐

- 배열로 저장

- 원소 삽입시 우선순위 비교해서 적절한 위치에 삽입

- 문제점

  - 배열 사용 -> 연산 시 원소 재배치 발생 -> 시간, 메모리 낭비

  - 트리를 이용하면 좋다



## 큐의 활용

### 버퍼

- 데이터를 전송하는 동안 일시적으로 저장하는 메모리 영역
- 버퍼링 : 버퍼를 활용하는 방식, 버퍼를 채우는 동작
- 자료구조
  - 입출력 및 네트워크 관련 기능에서 이용
  - 순서대로 입력/출력/전달되므로 FIFO 방식 자료 구조 큐 활용
- 키보드 버퍼