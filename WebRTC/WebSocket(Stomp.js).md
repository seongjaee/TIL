# WebSocket

## WebSocket

- 브라우저와 서버 사이의 상호작용 통신 세션을 설정할 수 있게 하는 기술
- 패킷(packet) 형태로 데이터 전달. 커넥션 중단, 추가 HTTP 요청 없이 양방향으로 전송
- 온라인 게임, 주식 트레이딩 등 지속적 데이터 교환 서비스에 적합
- OSI 모델 7계층에 위치 4계층 TCP에 의존
- HTTP 80포트, 443 포트 위에서 동작
- 주의
  - WebSocket은 프로토콜. 어떤 언어에 국한되지 않음.
  - JSON 객체가 아닌 String을 주고받아야함
- 웹소켓 핸드셰이크는 HTTP Upgrade 헤더를 사용해 HTTP 프로토콜에서 웹소켓 프로토콜로 변경

![img](WebSocket(Stomp.js).assets/Untitled.png)

### 연결 예시

```jsx
let socket = new WebSocket("we://<url>")
```

- `new Websocket()` 호출로 소켓 생성 시 즉시 연결 시작

- Chrome Dev tools > Network

  ![Untitled](WebSocket(Stomp.js).assets/dev-tool.png)

- 요청 헤더

  ```
  Connection: Upgrade
  Host: javascript.info
  Origin: chrome://new-tab-page
  Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits
  Sec-WebSocket-Key: CCbhgLvUoG5hbrzKGzM/nQ==
  Sec-WebSocket-Version: 13
  Upgrade: websocket
  ```

  - `Origin` : 서버에서 Origin 헤더를 보고 어떤 웹 사이트와 소켓 통신을 할지 결정. 웹소켓 객체는 크로스 오리진 지원.
  - `Connection: Upgrade` : 클라이언트 측에서 프로토콜을 변경하고 싶다는 요청
  - `Upgrade: websocket` : 변경하고자 하는 프로토콜은 websocket임을 의미
  - `Sec-WebSocket-Key` : 보안을 위해 브라우저가 생성한 키. 서버가 웹소켓 프로토콜 지원하는지 확인
  - `Sec-WebSocket-Version` : 웹소켓 프로토콜 버전 명시
  - `Sec-WebSocket-Extensions` : 브라우저에 의해 자동 생성. 데이터 전송과 관련된 무언가 또는 웹소켓 프로토콜 기능 확장과 관련된 무언가
  - `Sec-WebSocket-Protocol` : `soap` , `wamp` , SOAP나 WAMP 프로토콜을 준수하는 데이터를 전송하겠다는 의미

### 이벤트

- `open` : 커넥션 제대로 생성 시 발생
- `message` : 데이터 수신 시 발생
- `error` : 에러 발생 시 발생
- `close` : 커넥션 종료 시 발생
- `socket.send(data)` 를 통해 무언가 전송 가능

### 데이터 전송

- 웹소켓 통신은 ‘프레임’ 데이터 조각을 통해 이뤄짐.
  - 텍스트 프레임
  - 이진 데이터 프레임
  - ping/pong 프레임 : 커넥션이 유지되고 있는지 확인할 때 사용. 서버나 브라우저가 자동 생성
  - 커넥션 종료 프레임 등
- 브라우저 환경에서 개발자는 텍스트나 이진 데이터 프레임만 다룸
  - WebSocket `.send()` 는 텍스트나 바이너리 데이터만 보낼 수 있기 때문
- 데이터를 받을 때, 텍스트 데이터는 문자열 형태, 바이너리 데이터는 `Blob` 또는 `ArrayBuffet` 포맷

## STOMP

- STOMP : Simple(Streaming) Text Oriented Messaging Protocol
- 클라이언트와 서버가 주고받는 메시지를 구체적으로 정의하는 프로토콜
- WebSocket에서 주로 사용됨(WebSocket이 없이도 사용 가능, 반대로 WebSocket로 STOMP없이 사용 가능)
- WebSocket위에서 서브 프로토콜로써 사용하면 WebSocket에서 주고받는 메시지의 유형, 포맷, 내용 등을 정의하게 되어 규격에 맞는 메시지를 주고 받게 된다는 장점

### STOMP JS

STOMP library for JavaScript/TypeScript

- 웹 브라우저 또는 JavaScript 기반 환경에서 WebSocket 연결위에서 STOMP 제공
- Install

```bash
$ npm install @stomp/stompjs websocket --save
$ yarn add @stomp/stompjs websocket
```

- Require the module

```jsx
var Stomp = require('@stomp/stompjs')
```

- Create a STOMP Client

  - STOMP JS 클라이언트는 STOMP 서버와  `ws://` URL 을 사용해 통신.
  - 서버의 웹소켓 엔드포인트 URL로 `Stomp.client(url)` 호출해서 STOMP 클라이언트 JS 객체 생성

  ```jsx
  var url = "ws://localhost:15674/ws";
  var client = Stomp.client(url);
  ```

- Connection to the server

  - `client.connect(login, passcode, connectCallback, errorCallback, closeEventCallback, host);`

  - `client.connect(headers, connectCallback, errorCallback, closeEventCallback);`

  - STOMP client 생성 후, `connect()` 메서드 호출로 유효한 연결과 STOMP 서버에 인증.

  - 연결은 비동기적으로 성립. 유효한 연결 완료를 알림받기 위해서는 

    ```
    connect_callback
    ```

     함수를 

    ```
    connect()
    ```

     메서드에 넘겨주어야 함.

    - connect() 에 넘겨준 connect_callback 함수는 클라이언트가 STOMP 서버와 연결되고 인증받으면 호출됨.

  - 연결 실패 시 `connect()` 에 넘겨준 `error_callback` 함수가 호출됨.

  - 연결 끊기는 `disconnect()` 메서드. 연결 끊기도 비동기적. 유효한 연결 끊기를 알림받기 위해서는 `disconnect()` 에 콜백을 넘기면 됨.

- Heart-beating

  - client 객체는 heartbeat 필드가 있음
  - outgoing, incoming 필드로 heart-beating 설정 가능

- Auto Reconnect

  - client가 연결 실패 시 자동 재연경을 지원. reconnect_delay 필드로 설정. 기본값은 0으로 자동 재연결 해제.

  ```jsx
  // Add the following if you need automatic reconnect (delay is in milli seconds)
    client.reconnect_delay = 5000;
  ```

- Send messages

  - `send()` 메서드로 STOMP 메시지 전송

  ```jsx
  client.send(destination, headers, body);
  ```

- Subscribe and receive messages

  - 브라우저에서 메시지를 받기 위해서는 STOMP 클라이언트가 먼저 목적지를 구독해야함
  - `subscribe()` 메서드로 구독

  ```jsx
  var subscription = client.subscribe(destination, callback);
  ```

  - `subscribe()`는 JS객체를 리턴. `{ subscriptionID: id }`
  - subscribe 메서드에 ID를 넘기지 않으면 자동으로 유니크한 ID를 생성.

- Acknowledgement

  - 기본값으로, STOMP 메시지는 클라이언트에게 전송되기 전에 서버에 의해 자동적으로 승인됨

- Transcations

  - 메시지는 한 트랜잭션 안에 전송되고 승인될 수 있음
  - 트랜잭션은 클라이언트의 begin()  메서드로 시작
  - begin() 메서드는
    - 트랜잭션 ID 속성
    - commit(), abort() 메서드
    - 를 갖는 JavaScript 객체 반환
  - 클라이언트는 트랜잭션 지정으로 트랜잭션 안에서 메시지를 전송/승인 가능

  ```jsx
  // start the transaction
    var tx = client.begin();
    // send the message in a transaction
    client.send("/queue/test", {transaction: tx.id}, "message in a transaction");
    // commit the transaction to effectively send the message
    tx.commit();
  ```