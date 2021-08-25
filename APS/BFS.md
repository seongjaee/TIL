# BFS (너비 우선 탐색)

- 비선형 구조인 그래프는 그래프의 모든 자료를 빠짐없이 검색하는 게 중요
- 모든 자료를 검색하는 두 가지 방법
  - 깊이 우선 탐색(Depth First Search, DFS)
  - 너비 우선 탐색(Breadth First Search, BFS)
- 너비 우선 탐색은
  - 현재 노드에서 가까운 노드들을 먼저 살펴봄
  - 인접한 모든 노드에 대해 탐색하고, 목표 노드가 없으면 한번 더 깊이 들어가서 탐색
- 가까운 노드 먼저 탐색 -> 선입선출 -> 큐로 구현가능

- 큐를 이용한 BFS 과정
  1. 시작 정점 v 방문
  2. 정점 v에서 인접한 정점들을 모두 enQueue
  3. 큐에서 deQueue 해서 방문
  4. 큐가 빌 때까지 2. 3. 반복

## [큐](./Queue.md)

- 파이썬에서 큐 구현
  1. 직접 큐 클래스 구현
  2. 리스트를 큐처럼 사용 - `pop(0), append()`
  3. `deque` 모듈

## 코드

```python
# G: 그래프 인접 리스트
def BFS(G, v):
    visited = [0] * (n+1)
    queue = []
    q.append(v)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
        for i in G[t]:
            if not visited[i]:
                queue.append(i)
```



```python
# BFS 진행 중 만나는 노드들의
# 출발점으로부터의 거리를 표시
def BFS(G, v, n):
    visited = [0] * (n+1)
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        t = queue.pop(0)
        for i in G[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
```

- 위 코드처럼 작성하면 출발 정점으로부터 다른 정점까지의 거리를 알 수 있다.
- BFS는 최단경로를 탐색할 때 유용하다. DFS는 찾은 경로가 최단 경로인지 장담하기 어렵지만, BFS는 최단경로를 장담할 수 있다.