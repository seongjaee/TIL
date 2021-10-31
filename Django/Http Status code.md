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
- DELETE 요청에 대한 응답으로 사용



### 205 Reset Content

- 요청이 수행되었고 유저 에이전트에게 요청 보낸 문서 view를 리셋하라고 알려줌.

## Redirection 3xx

- 요청을 수행하기 위해 유저 에이전트가 행해야할 액션을 알려줌.

### 300 Multiple Choice

- 요청에 대해 여러 응답 가능

### 301 Moved Permanetly

- 요청받은 리소스가 새로운 URL로 변경됨. 앞으로 해당 리소스에 대한 참조는 반환된 URL을 사용해야함.

### 302 Found

- 요청받은 리소스가 임시적으로 다른 URL로 변경됨. 앞으로의 요청을 현재 URL로 진행해야함.

### 303 See Other

- 요청에 대한 응답을 다른 URI에서 받을 수 있음. 따라서 해당 리소스로 GET 요청을 보내야함.
- 다른 URL은 응답의 Location 필드에 주어질 수 있음.

### 304 Not Modified

- 클라이언트가 GET 요청을 보냈고 승인이 났는데 문서가 수정되지 않는 경우, 서버가 보낼 수 있는 상태 코드.

### 307 Temporary Redirect

- 요청받은 리소스가 임시적으로 다른 URL로 변경됨.
- 302 Found와 동일한 의미를 갖지만, 유저 에이전트는 HTTP 메소드를 변경해선 안된다는 차이점.



## Client Error 4xx

- 클라이언트에 오류가 있는 것 같을 때 발생.



### 400 Bad Request

- 서버가 잘못된 문법으로 인해 이해할 수 없는 요청.

### 401 Unauthorized

- 이 요청은 유저 authentication이 필요함을 알림.
- 클라이언트는 요청한 응답을 받기위해서는 인증해야함.

### 403 Forbidden

- 서버가 요청을 이해했지만 수행하기를 거부함.

### 404 Not Found

- 요청 URI를 찾을 수 없음. 서버가 요청 거부에 대한 이유를 드러내고 싶지 않을 때 자주 사용. 인증받지 않은 클라이언트에게 리소스를 숨기기위해 403 대신 사용 가능.

### 405 Method Not Allowed

- 요청 메서드가 요청 URI에서 허락되지 않음.

## Server Error 5xx

- 서버가 요청을 수행할 수 없을 때.

### 500 Internal Server Error

- 서버가 처리 방법을 모르는 상황이 발생.