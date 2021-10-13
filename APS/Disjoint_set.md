# 서로소 집합, 상호 배타 집합

- 서로 중복 포함된 원소가 없는 집합.

- 트리, 연결 리스트 등으로 표현
- Union 함수와 Find 함수
- 집합은 그 집합을 대표하는 원소로 표현한다.

## 함수

- Make-Set(x) : 유일한 원소 x를 포함하는 새로운 집합 생성

  ```
  Make-Set(x)
  	p[x] <- x
  ```

- Find-Set(x) : x를 포함하는 집합을 찾는 연산

  ```
  // 재귀
  Find-Set(x)
  	IF x == p[x] : RETURN x
  	ELSE		 : RETURN Find-Set(p[x])
  ```

  ```
  // 반복
  Find-Set(x)
  	while x != p[x]
  		x = p[x]
  	return x
  ```

- Union(x, y) : x를 포함하는 집합과 y를 포함하는 집합을 통합

  ```
  Union(x, y)
  	p[Find-Set(y)] <- Find-Set(x)
  ```

- 문제점

  - Union을 반복하면 트리의 깊이가 계속 깊어진다.
  - 연산 효율이 떨어짐.

### 연산 효율 높이는 방법

#### Rank 이용한 Union

- 각 노드는 자신을 루트로 하는 subtree의 높이(rank)를 저장
- 두 집합을 합칠 때 rank가 낮은 집합을 rank가 높은 집합에 붙임

```
Make-Set(x)
	p[x] <- x
	rank[x] <- 0
```

```
Union(x, y)
	Link(Find-Set(x), Find-Set(y))
	
	
Link(x, y)
	IF rank[x] > rank[y]
		p[y] <- x
	ELSE
		p[x] <- y
		IF rank[x] == rank[y]
			rank[y]++
```

#### Path compression

- Find-Set의 과정에서 만나는 모든 노드들이 root를 가리키도록 포인터를 바꿔줌

```
Find-Set(x)
	IF x != p[x]		// x 가 루트가 아닌 경우
    	p[x] <- Find-Set(p[x])
	RETURN p[x]
```



