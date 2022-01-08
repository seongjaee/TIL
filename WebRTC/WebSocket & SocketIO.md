# WebSocket & Socket.IO

## 1. WebSocket

### http

**통신 과정**

- 유저가 request 보냄
- 서버가 response 응답

**stateless, 무상태성**

- 요청이나 응답후에는 유저를 기억하지 못함.

### WebSocket

마찬가지로 프로토콜

주소 http처럼 ws로 시작

**통신 과정**

- 유저가 WebSocket requset 보냄
- 서버가 WebSocket accpet or 거절

- 위의 악수가 성립하면 연결(connection)이 성립(establish)

  브라우저와 서버가 양방향으로 연결

- 브라우저와 서버가 서로에게 언제든 메시지를 보낼 수 있는 상태

**[웹소켓API - MDN](https://developer.mozilla.org/ko/docs/Web/API/WebSockets_API)**

- JavaScript는 Websocket API를 제공한다.

**ws**

- [Node.js WebSocket 라이브러리](https://www.npmjs.com/package/ws) 이다.
- *ws is a simple to use, blazing fast, and thoroughly tested WebSocket client and server implementation.*

**주의**

- WebSocket은 프로토콜이다. 어떤 언어에 국한되는 게 아니다.
  - Frontend와 Backend는 JSON 객체가 아니라 String을 주고 받아야한다.

## 2. [Socket.io](https://socket.io/)

> *Bidirectional and low-latency communication for every platform*

- 효율성
- 지속성
- 확장가능성

#### **What Socket.IO is**

*Socket.IO is a library that enables **real-time, bidirectional and event-based communication** between the browser and the server.* 

- WebSocket 연결이 가능하면 WebSocket 연결을 시도, 
- 불가능한 경우 HTTP long polling으로 시도
  - => WebSocket이 불가능한 경우도 실시간, 양방향, 이벤트 기반 연결을 제공해준다.

#### **What Socket.IO is NOT**

*Socket.IO is **NOT** a WebSocket implementation.*

*Socket.IO is not meant to be used in a background service, for mobile applications.*

#### **Features**

- reliability
  - WebSocket 연결이 안되면 HTTP long-polling으로
- automatic reconnection
- 등등

