# HTTP

- HyperText Tranfer Protocol
- 웹 상에서 컨텐츠를 전송하기 위한 약속
- HTML 문서 같은 리소스들을 가져올 수 있도록 하는 프로토콜
- 웹 상에서 모든 데이터 교환의 기초
  - 요청(request)
  - 응답(responce)
- 기본 특성
  - Stateless
  - Connectless
- => 쿠키와 세션을 통해 서버 상태를 요청과 연결하도록 함

- HTTP 메시지
- 요청
  - Path
  - Method
  - Headers
  - protocol version
- 응답
  - Status code
  - status message
  - headers
  - protocol version
- HTTP request methods
  - 자원에 대한 행위를 정의
  - 주어진 리소스에 수행하길 원하는 행동을 나타냄
  - GET, POST, PUT, DELETE
- HTTP response status code
  - Informational response 1xx
  - Successful response 2xx
  - Redirection messages 3xx
  - Client error responses 4xx
  - Server error responses 5xx

- 웹에서의 리소스 식별
  - 리소스: HTTP 요청의 대상, 문서 또는 사진 기타 어떤 것
  - URI(Unifrom Resource Identifire)를 통해 식별
- URL (Uniform Resource Locator)
  - 통합 자원 위치
  - 네트워크 상에 자원이 어디있는지 알려주기 위한 약속
  - 과거에는 실제 자원 위치였으나, 현재는 추상화된 의미론적인 구성
  - 웹 주소, 링크
- URN (Uniform Resource Name)
  - 통합 자원 이름
  - URL과 달리 자원의 위치에 영향을 받지않는 유일한 이름 역할

- URI (Uniform Resource Identifier)
  - 통합 자원 식별자
  - 인터넷의 자원을 식별하는 유일한 주소
  - 하위 개념
    - URL, URN
  - URL을 사용하는 비중이 크기 때문에 일반적으로 URL은 URI와 같은 의미처럼 사용되기도 함

- URI 구조

  - Scheme
    - 브라우저에서 사용해야하는 프로토콜
    - http(s), data, file, ftp, malito
  - Host (Domain name)
    - 요청받는 웹 서버 이름
    - IP address를 직접 사용할 수 있지만, 편의를 위한 이름으로 사용
    - `www.naver.com`
    - google IP address : 142.251.42.142
  - Port
    - 리소스에 접근하는데 사용되는 기술적인 문(gate)
    - 표준 포트
      - HTTP 80
      - HTTPS 442
  - Path
    - 웹 서버 상의 리소스 경로
    - 현재는 실제 위치가 아닌 추상화 형태 구조로 표현
  - Query (Identifier)
    - Query String Parameter
    - 웹 서버에 제공되는 추가적인 매개변수
    - &로 구분되는 key-value 목록
  - Fragment
    - Anchor
    - 리소스 안에서의 북마크의 한 종류
    - 브라우저에게 HTML의 특정 부분을 보여주기 위한 방법
    - fragment identifier라고 부르며 # 뒤의 부분은 서버에 보내지지 않음

  