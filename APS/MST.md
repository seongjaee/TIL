# 최소 비용 신장 트리(MST)

- 신장 트리
  - n 개의 정점으로 이루어진 무향 그래프에서 n개의 정점과 n-1개 간선으로 이루어진 트리
- 최소 신장 트리(MST)
  - 무향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리



## Prim 알고리즘

- 하나의 정점에서 연결된 간선들 중에 하나씩 선택하는 MST를 만드는 방식
  1. 임의 정점 하나 선택
  2. 선택한 정점과 인접한 정점 중 최소 비용의 간선이 존재하는 정점 선택
  3. 모든 정점이 선택될때까지 1, 2 반복
- 서로소인 2개의 집합 정보 유지
  - 트리 정점 : MST에 포함된 정점들
  - 비트리 정점 : 포함되지 않은정점들

### 수도 코드

```
MST_PRIM(G, r)						// G : 그래프, r : 시작 정점
	FOR u in G.V
		u.key <- inf				// u.key : u에 연결된 간선 중 최소 가중치. u를 MST에 추가하는데 필요한 가중치
		u.pi <- NULL				// u.pi : 트리에서 u의 부모
    r.key <- 0
    Q <- G.V						// 우선순위 Q에 모든 정점 넣음
    WHILE Q != 0
    	u <- EXTRACT_MIN(Q)			// key값이 최소인 정점 가져오기
    	FOR v in G.Adj[u]			// u의 인접 정점들
    		IF v in Q AND w(u, v) < v.key	// Q에 있는 v의 key값 갱신
    			v.pi <- u
    			v.key <- w(u, v)
```

### 파이썬 코드

```python
def prim(start, V):
    key = [INF] * V
    key[start] = 0
    MST = [0] * V
    pi = [0] * V
    # 신장 트리에 V개의 정점을 추가해야함
    for _ in range(V):
        # MST에 포함되지 않은 정점 중 key[u]가 최소인 u찾기
        u = 0
        minV = INF
        for i in range(V):
            if MST[i] == 0:
                if key[i] < minV:
                    u = i
                    minV = key[i]
        MST[u] = 1  # MST에 추가
        for v in range(V):
            # v가 MST에 포함되지 않았고, u와 인접해있다면
        	if MST[v] == 0 and adj[u][v] != 0:  
                # 기존 키값보다 더 작으면 갱신
                if key[v] > adj[u][v]:  
                    key[v] = adj[u][v]
```



## KRUSKAL 알고리즘

- 간선을 하나씩 선택해서 MST를 찾는 알고리즘

  1. 처음에 모든 간선을 가중치에 따라 오름차순으로 정렬

  2. 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킴

      a. 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택

  3. n-1개의 간선이 선택될 때까지 반복

- 해당 간선을 추가하면 사이클이 생기는지 확인해야함.



### 수도 코드

```
MST-KRUSKAL(G)				// G: 그래프
	A <- 0					// 선택된 간선들의 집합
	For v in G.V			// G.V: 정점 집합 
		Make-Set(v)			// 그래프 각각의 정점들을 원소로 하는 집합 생성
		
	G.E 가중치 기준 정렬
	
	For 가중치 최소 간선 (u, v) in G.E 선택 n-1개		// G.E: 간선 집합
		IF Find-Set(u) != Find-Set(v)		// 사이클이 존재하지 않으면
			A <- A + {(u, v)}				// A에 추가
			Union(u, v)						// 두 정점이 포함된 집합 통합
			
	RETURN A
```

