# Python GIL(Global Interpreter Lock)

- [https://docs.python.org/ko/3/glossary.html#term-global-interpreter-lock](https://docs.python.org/ko/3/glossary.html#term-global-interpreter-lock)

- 한 번에 하나의 스레드만이 파이썬 **바이트 코드**를 실행하도록 보장하기 위해 CPython 인터프리터가 사용하는 메커니즘
  - 바이트 코드 : 파이썬 소스 코드는 바이트 코드로 컴파일됨. CPython 인터프리터에서 파이썬 프로그램의 내부 표현임

- (중요한 빌트인 타입을 포함한) 객체 모델이 동시 액세스(concurrent access)로부터 안전하게 만듦으로써, CPython 구현을 단순화함.

- 이러한 전체 인터프리터 잠금은 멀티 프로세서 머신이 제공하는 많은 병렬성(parallelism)을 희생하면서, 인터프리터를 멀티스레드화하기 쉽도록 한다.

- 하지만 표준 확장 모듈 또는 써드 파티 확장 모듈 중 몇몇은 GIL을 풀도록 설계되었다. 압축이나 해싱 등의 계산 집약적인 업무를 할 때는. 그리고 I/O중에는 GIL이 항상 풀린다.

- "Free-threaded"한 인터프리터를 만드려는 노력들은 성공하지 못했다. 왜냐면 보통의 싱글 프로세서 경우에서 성능이 저하되었기 때문이다. 이런 성능 이슈를 해결하려다 구현이 훨씬 복잡해져 유지 비용이 더 들어갈 것으로 여겨짐.

