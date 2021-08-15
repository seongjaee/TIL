# 패턴 매칭

긴 문자열에서 작은 문자열(패턴)이 포함되어 있는지(어디에 있는지, 몇 개 있는지) 확인하는 알고리즘

## 패턴 매칭 알고리즘

### 브루트-포스

- text[i] == pattern[j] -> i ++, j ++
- text[i] != pattern[j] -> i -= j, j = 0

```python
# p : 찾고자하는 패턴
# t : 전체 텍스트
M = len(p)
N = len(t)

def brute_force(p, t):
    i = 0  # t의 인덱스
    j = 0  # p의 인덱스
    while j < m and i < n:
        if t[i] != p[j]:
            i -= j  # 비교를 시작한 위치로 돌아감
            j -= 1  # 초기화
        i += 1
        j += 1
        
    if j == m:  # 검색 성공
        return i - M
    else:  # 검색 실패
        return -1
```

- 시간복잡도 : O(MN)



<br/>



### KMP 알고리즘

- 불일치가 발생한 텍스트의 앞부분에 어떤 문자가 있는지 미리 알고 있음

- 불일치가 발생한 앞 부분에 대해서는 다시 비교하지 않고 진행

- 패턴을 전처리 -> 베열 next[M]을 구해서 잘못된 시작을 최소화

  - next[M] : 불일치 발생 시 이동할 다음 위치

- 시간복잡도 : O(M+N)

- 아이디어 설명

  - text = '...abcdabcd...'
  - p = 'abcdabcef'
  - abcdabc까지는 매치되고, e에서는 실패한 상황.
  - 이 때 패턴의 abc와 실패 직전의 abc는 동일하다.
  - 따라서 다음 비교는 실패 직전의 abc부터 비교시작하면 된다.

- 매칭이 실패했을 때 돌아갈 곳을 계산

  - 패턴의 각 위치에 대해 매칭에 실패했을 때 돌아갈 곳을 준비해둠

  - 즉, p = 'abcdabcef'에서 돌아갈 곳은 -1,0,0,0,0,1,2,3,0 LPS

    - 구하는 방법

    - 패턴의 앞부분이 반복되는 곳을 찾는다.

    - 반복되는 부분부터 1, 2, 3, ...

      ```python
      # 패턴으로부터 next 배열 만드는 법
      
      cnt = 0  # 일치한 개수
      next = [0] * M
      i = 1
      
      # 패턴을 순회하면서
      while i < M:
           # 일치한 경우
          if p[i] == p[cnt]: 
          	cnt += 1
              next[i] = cnt
             	i += 1
              
          # 불일치한 경우
          else:
              # 일치 중이다가 불일치한 경우
              if cnt != 0:
                  # 혹시 이 앞에서부터 시작하면
                  # 연속 일치가 더 길 수 도 있어
                  cnt = next[cnt-1]
                  
              # 불일치가 유지 중인 경우
              else:  
                  next[i] = 0
                  i += 1
      ```



<br/>



### 보이어-무어 알고리즘

- 오른쪽에서 왼쪽으로 비교
- 대부분의 상용 SW에서 채택 중인 알고리즘
- 오른쪽 끝에 있는 문자가 불일치 하고 이 문자가 패턴 내에 존재하지 않는 경우, 이동 거리는 패턴의 길이만큼.
- 오른쪽 끝에 문자가 불일치하고 이 문자가 패턴 내에 존재할 경우, 패턴에서 일치하는 문자와 불일치 난 위치를 맞춰줌.
- 해당 글자에서 불일치가 일어날 경우 몇 칸을 건너뛸 것인지를 담은 skip 배열을 만듬.
- 최악의 경우 : \Theta(MN)
- 일반적으로는 \Theta(N) 보다 시간이 덜 듬.



<br/>



### 카프-라빈 알고리즘

- 해시 기법 이용

- 시간 복잡도 : \Theta(N)