# 피보나치 수를 구하는 여러가지 방법

## Fibonacci Numbers

- 피보나치 수는 첫째 둘째 항이 1이고 (또는 첫째항 0, 둘째항 1)

  나머지 항은 바로 앞 두 항의 합인 수열이다.

> TMI
>
>  레오나르도 피보나치는 1100년대 ~ 1200년대 이탈리아 피사 출신 수학자다.
>
> 사실 피보나치는 보나치의 아들이라는 뜻.



## 1. 재귀 함수

- 자기 자신을 호출하여 순환 수행하는 함수

- 재귀 호출 방식을 사용하면 프로그램을 간단하게 작성할 수 있다는 장점이 있다.

  

### 피보나치 수 재귀 함수 알고리즘

```python
def fibo(n):
    if n < 2: return n
    return fibo(n-1) + fibo(n-2)
```



### 메모이제이션, Memoization

- 재귀 호출에는 무수히 많은 중복 호출이 존재한다. 즉 불필요한 연산을 많이 하게 된다.

- **메모이제이션**은 이전에 계산한 값을 메모리에 저장해서 중복 계산하지 않도록 하여 전체적인 실행 속도를 빠르게 하는 기술. 동적 프로그래밍의 핵심

- 위의 fibo에서

  - fibo(5) 는 fibo(2)를 총 3번 호출.

  - fibo(n) 은 시간복잡도 Theta(2^n)임.

  - 메모이제이션을 사용하면, 실행시간을 Theta(N)까지 줄일 수 있다.

    ```python
    def fibo_memo(n):
        global memo
        if n not in memo:
            memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
        return memo[n]
        
    memo = {0: 0, 1: 1}
    ```



## 2 . DP(Dynamic Programming), 동적 계획법

- 동적 계획 알고리즘은 최적화문제를 해결하는 알고리즘이다.

- 크기가 작은 부분 문제들을 모두 해결한 후, 그 해를 이용하여 큰 크기의 부분 문제들을 해결해나가면서, 최종적으로 원래 문제를 해결하는 알고리즘.
- 해결 과정

1. 문제를 부분 문제로 분할

2. 가장 작은 부분 문제부터 해를 구한다.

3. 테이블에 결과를 저장하고 저장된 부분문제의 해를 이용해 상위 문제의 해를 구한다.

### 피보나치 수 DP 알고리즘

```python
def fibo_dp(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1]+f[i-2])
        
    return f[n]
```

- 위에 있던  재귀 함수를 하향식 DP, 지금의 반복 구조를 상향식 DP로 볼 수도 있다.

- 메모이제이션을 재귀적 구조보다 반복적 구조로 DP를 구현하는게 효율적.

## 3. 반복문 풀이

- 저장없이 피보나치 수 하나만을 구할 때는 반복문을 이용할 수 도 있다.
- 파이썬에서는 튜플을 이용해 스왑을 간단히 할 수 있다.

```python
def fibo(n):
    if n < 2:
        return n
    
    f0, f1 = 0, 1
    for i in range(n-1):
        f1, f0 = f0 + f1, f1
        
    return f1
```



## 4. 행렬 곱셈

- 위의 방법들은 n이 커질수록 메모리와 시간이 많이 필요해진다.
- n이 큰 경우 행렬 곱셈과 분할 정복을 통해 해결할 수 있다.

### 피보나치 행렬식

- 피보나치 수열을 이용해서 다음과 같은 행렬식을 만들 수 있다.

![image01](Fibonacci.assets/image01.png)

- 더 나아가 2x2 행렬로 만들면

![image02](Fibonacci.assets/image02.png)

​	까지 만들 수 있다.

- 따라서 귀납적으로 다음과 같다.

![image03](Fibonacci.assets/image03.png)

- 그런데 F2 = F1 = 1, F0 = 0 이므로 최종적으로 다음 식을 얻을 수 있다.

![image04](Fibonacci.assets/image04.png)

- 위의 식을 이용해서 행렬 곱셈으로 피보나치 수를 구할 수 있다. 특히 [분할 정복을 이용한 거듭제곱](https://github.com/seongjaee/algorithm-study/blob/main/Codes/Divide_n_conquer/power.md#행렬-제곱)을 하면 빠르게 구할 수 있다.

