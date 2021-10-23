# Http Status code

- [MDN - HTTP 상태 코드](https://developer.mozilla.org/ko/docs/Web/HTTP/Status)
- https://datatracker.ietf.org/doc/html/rfc2616#section-10

- HTTP 응답 상태 코드는 특정 HTTP 요청이 성공적으로 완료되었는지 알려줌.
- 5개의 그룹으로 나누어진다.
  - 정보를 제공하는 응답
  - 성공적인 응답
  - 리다이렉트
  - 클라이언트 에러
  - 서버 에러



## 1xx

- Status-Line과 optional header만을 포함한 임시 응답을 나타냄.
- 필요한 header가 없음.

### 100 Continue

- 지금까지 상태가 괜찮으며 클라이언트는 계속해서 요청을 하거나 이미 요청을 완료했으면 무시해도 괜찮음을 알려줌.

- ```
  The client SHOULD continue with its request.
  ```

- 서버는 요청이 완료되면 마지막 응답을 반드시 보내야함.

### 101 Switching Protocols

- 서버가 프로토콜을 변경할 것임을 알려줌.



## Successful 2xx

- 클라이언트의 요청이 성공적으로 수신, 이해, 승인되었음을 나타냄.

### 200 OK

- 요청이 성공함. method에 따라 응답이 달라짐

### 201 Created

- 요청이 수행되어 그 결과로 새로운 리소스가 생성되었음.
- 오리진 서버는 201 코드를 반환하기 전에 리소스를 생성해야함.
- 액션이 즉시 수행될 수 없다면, 서버는 대신 202 Accepted를 응답해야함.

### 202 Accepted

- 요청이 처리되도록 승인되었지만, 처리가 아직 완료되지 않음
- 202 응답은 의도적으로 명확하지 않음. 

### 204 No Content

- 요청이 수행되었으나 바디를 반환하지 않아도 됨. 보통 헤더에 갱신된 메타정보를 반환할 수 있음.
- 사용자 에이전트의 경우 요청 보낸 문서의 view form이 변하지 않음.

- 204 응답은 메시지-바디를 포함해선 안됨. 그래서 항상 헤더 필드 다음 첫번째 빈 줄로 끝남.



### 205 Reset Content

- 요청이 수행되었고 유저 에이전트에게 요청 보낸 문서 view를 리셋하라고 알려줌.

## Redirection 3xx

- 요청을 수행하기 위해 유저 에이전트가 행해야할 액션을 알려줌.

### 300 Multiple Choice

- 요청에 대해 여러 응답 가능

### 301 Moved Permanetly

- 



## Client Error 4xx



## Server Error 5xx