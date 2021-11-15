# Server & Client

### Server

- 클라이언트에게 정보나 서비스를 제공하는 컴퓨터 시스템
- 정보 & 서비스 제공
  - template 또는 JSON
- DB와 통신, 데이터 CRUD

### Client

- 서버에게 그 서버가 맡는 서비스를 요청
  - 서비스 요청을 위해 필요한 인자를 서버가 요구하는 방식에 맞게 제공
- 서버로부터 반환되는 응답을 사용자에게 적절한 방식으로 표현하는 기능을 가진 시스템
- 정보 요청 & 표현



## CORS

### 이슈

- 클라이언트에서 GET 요청으로 데이터를 받아오려고 할 때

- ...blocked by CORS Policy: No 'Access-Control-Allow-Origin' header...

- 서버 측에서는 응답을 했으나, 클라이언트에서 CORS Policy에 의해 block 당함.

### Same-origin policy(SOP)

- 동일 출처 정책
- 특정 출처에서 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용하는 것을 제한하는 보안 방식
- 잠재적으로 해로울 수 있는 문서를 분리함으로써 공격 방지
- 출처(Origin)
  - 두 URL의 Protocol, Port, Host가 모두 같아야 동일한 출처

### Cross-Origin Resource Shraing(CORS)

- 교차 출처 리소스 공유
- **추가 HTTP header를 사용**하여, 특정 출처에서 실행중인 웹 애플리케이션이 **다른 출처의 자원에 접근할 수 있는 권한을 부여**하고 **브라우저에 알려**주는 체제
- 리소스가 자신의 출처와 다를 때 교차 출처 HTTP 요청을 실행
- 보안상의 이유로 브라우저는 교차 출처 HTTP요청을 제한(SOP를 따름)
- 다른 출처의 리소스를 불러오려면 그 출처에서 올바른 CORS header를 포함한 응답을 반환해야함



### CORS Policy

- 교차 출처 리소스 공유 정책
- 다른 출처에서 온 자원을 공유하는 것에 대한 정책
- 교차 출처 접근 허용하려면,
  - CORS를 사용해 교차 출처 접근을 허용하려면
  - HTTP의 일부로, 어떤 호스트에서 자신의 컨텐츠를 불러갈 수 있는지 서버에서 지정

### 왜 CORS인가

- 브라우저 & 웹 애플리케이션 보호
  - 악의적인 사이트의 데이터 사전 차단
  - 응답 자원의 최소한의 검증
  - 서버는 정상적으로 응답하지만 브라우저에서 차단
- 서버의 자원 관리
  - 누가 해당 리소스에 접근할 수 있는지 관리

### CORS 허용 방법

- CORS HTTP 응답 헤더 예시
  - 'Access-Control-Allow-Origin'

### Access-Control-Allow-Origin 응답 헤더

- 이 응답이 출처로부터 요청 코드와 공유될 수 있는지 나타냄
- `*`을 통해 모든 도메인에서 접근 가능함을 표시
- `Access-Control-Allow-Origin: *`
- `*` 외 특정 origin 하나를 명시할 수 있음

### 시나리오

1. 클라이언트가 A 서버로 요청
2. A 서버는 Access-Control-Allow-Origin에 특정한 origin을 포함시켜 응답
3. 브라우저는 응답에서 Access-Control-Allow-Origin를 확인한 후 허용 여부 결정

### django-cors-headers 라이브러리

- 응답에 CORS 헤더를 추가해주는 라이브러리
- 다른 출처에서 보내는 django 애플리케이션에 대한 브라우저 내 요청을 허용함



