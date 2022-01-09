# WebRTC

[WebRTC 프로토콜 소개 - MDN](https://developer.mozilla.org/ko/docs/Web/API/WebRTC_API/Protocols)

> Web Real-Time Communication

중간자 없이 브라우저 간에 오디오, 영상 미디어를 스트림. 임의의 데이터도 교환.

두 피어간의 커넥션은 `RTCPeerConnection`인터페이스를 통해 이루어짐. 

**P2P**

>  peer-to-peer

- 동등 계층간 통신망

- 서버가 필요없이 망 구성에 참여하는 컴퓨터끼리 리소스를 공유

**ICE(Interactive Connectivity Establishment)**

- 브라우저가 peer를 통한 연결이 가능하도록 하게 해주는 프레임워크

- ICE는 STUN와 TURN 서버를 사용.

**STUN(Session Traversal Utilities for NAT)**

- public address를 발견하거나 peer 간의 직접 연결을 만는 등 라우터의 제한을 결정하는 프로토콜

- 클라이언트가 STUN 서버에 요청을 보내, **자신의 public address**와 **라우터의 NAT 뒤에 있는 클라이언트가 접근 가능한지** 등의 응답을 받음.

**NAT(Network Address Translation)**

- 네트워크 주소 변환
- 단말에 공개 IP주소를 할당하기 위해 사용.
- 여러 대의 호스트가 하나의 공개 IP 주소 사용
- 내부 네트워크 IP주소와 외부에 노출되는 주소를 다르게 유지하는 보안

**TURN(Traversal Using Relays around NAT)**

- Symmetric NAT 제한을 우회.
- TURN 서버와 연결 후, 모든 peer들에게 저 서버에 모든 패킷을 보내고 다시 나에게 전달해달라고 요청.