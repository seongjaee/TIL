# Auth

## Authentication

- 인증, 입증
- 자신이라고 주장하는 사용자가 누구인지 확인
- 401 Unauthorized
  - 미승인, 비인증

## Authorization

- 권한 부여, 허가
- 사용자에게 특정 리소스 또는 기능에 대한 액세스 권한을 부여하는 과정
- 보안 환경에서 권한 부여는 항상 인증을 따라야 함

- 403 Forbidden
  - 서버는 클라이언트가 누구인지는 알고 있음.

<hr>

- 세션, 토큰, 제 3자를 활용하는 등의 다양한 인증 방식 존재

- 세션 베이스
  - 클라이언트가 POST 로그인 요청
  - 서버가 세션 테이블에 저장
  - 서버가 세션 아이디와 함께 응답
  - 클라이언트 브라우저에 세션 정보 저장
  - 세션 아이디와 함께 요청
  - 세션 아이디를 세션 테이블에서 확인 후 로그인
  - 응답

## JWT

- JSON Web Token
- JSON 포맷을 활용하여 요소 간 안전하게 정보를 교환하기 위한 표준 포맷
- 암호화 알고리즘에 의한 디지털 서명이 되어있음 => JWT 자체로 검증 가능하고 신뢰할 수 있는 정보 교환 체계
- JWT 자체가 필요한 정보를 모두 갖고 있음(self-contained) => 다른 검증 수단이 필요없음
- Authentication, Information Exchange에 사용됨.
- DB를 사용한 토큰 유효성 검사가 필요 없음
  - 세션 또는 기본 토큰을 기반으로 하는 인증과의 핵심적인 차이점

### 활용 이유

- 세션에 비해 HTML, HTTP 환경에서 사용하기 용이
  - 세션 방식은 유저의 세션 정보를 서버에 보관해야함
  - JWT는 클라이언트에서 토큰 정보 저장하고 필요 요청에 토큰을 같이 보내면 그 자체가 인증 수단
- 보안 수준
  - 특정 요소 하나만 변경되어도 모든 데이터가 바뀌므로 위변조가 불가능
- JSON의 범용성
- 서버 자원 절약

### 구조

- `.` 를 이용해 3개로 구분
- Header, Payload, Signature

- Header
  - 토큰 type과 Hashing algorithm으로 구성
- Payload
  - 토큰에 넣을 정보
  - claim : 정보의 한 조각
- Signature
  - Header와 Payload의 encoding값을 더하고 private key로 hashing하여 생성

### JWT 시나리오

- 클라이언트에서 POST 로그인 요청
- 서버에서 로그인 정보를 바탕으로 비밀번호 암호화 및 JWT 발급
- JWT를 클라이언트에게 응답
- 클라이언트가 JWT를 저장
- 인증이 필요한 요청 시 저장해둔 JWT를 함께 보냄
- 서버에서 JWT Decoding하여 인증
- 응답

### JWT 로그아웃

- 브라우저에서 토큰 정보를 삭제
- JWT는 발급 이후 관리 어려움(유효한 토큰이 어딘가 살아있으면 악용 가능성). 따라서 최소한의 안전 장치가 필요.
- 안전 장치
  - 토큰 만료 시간 설정
  - 로그아웃할 때 클라이언트에서 토큰 삭제
  - 블랙 리스트 설정



## Code

- `set_password()`
  - 비밀번호 해싱을 처리
- 해싱이란?
  - 가변 크기의 입력 값에서 고정된 크기의 출력 값을 생성해내는 과정
  - 암호학에서는 암호화 해시 함수(MD5, SHA-1, SHA-2 등)에 의해 진행

- `@permission_classes`
  - view 함수 시작 시 확인되는 기본 권한 결정하는 권한 클래스 목록
  - `@api_view` 데코레이터보다 아래 위치해야함.
- `AllowAny`
  - 요청 인증 여부에 관계없이 무제한 엑세스 허용

### REST framework JWT Auth 패키지

- DRF 의 JWT Auth 지원

- `REST_FRAMEWORK`

  - `DEFAULT_PERMISSION_CLASSES`
    - 함수 시작 시 확인할 기본 권한 결정하는 권한 클래스 목록
  - `IsAuthenticated`
    - 인증된 사용자에게만 권한 부여.
  - `DEFAULT_AUTHENTICATION_CLASSES`
    - request.user 속성에 엑세스할 때 사용되는 기본 인증 사용자 집합을 결정하는 인증 클래스 목록.
    - 사용자 인증의 기본값 설정.
  - `JSONWebToken...`
    - 토큰 기반 인중 중 JWT를 활용해 JWT 자체를 검증
    - 인증 여부와 상관 없이 JWT의 유효성을 파악
  - 위의 설정은 전역 설정임.

- ```python
  # 토큰 만료기간 설정
  JWT_AUTH = {
      'JWT_EXPIRATION_DELTA' : datetime.timedelta(seconds=300)
  }
  ```

  



### JWT을 이용한 Auth

- JWT는 HTTP 요청 header에 
  - `{Authorization: 'JWT <token>'}` 형식으로 보내야함.