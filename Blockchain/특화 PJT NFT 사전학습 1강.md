# 특화 PJT NFT 사전학습 1강

> 기본 개념과 Ropsten 네트워크 실습

**목차**

1. 블록체인 분류
2. 이더리움 네트워크
3. Ropsten 실습 환경 준비
4. Ropsten 테스트넷 실습



## 1. 블록체인 분류

- public
  - 누구나 네트워크에 참여
  - Bitcoin, **Ethereum**, Zcash, Litecoin, ...
- private
  - 하나의 조직 혹은 기관이 관장하는 네트워크, 승인된 주체만 자료를 읽고, 지정 노드만 거래를 승인
  - Quorum, MultiChain, Iroha, Monax, ...
- consortium
  - 이해 관계자 간에 컨소시엄을 구성하여 네크워크를 구성, 네트워크 참여자에 의해 접근 허용
  - Hyperledger Fabric, Tendermint, R3 Corda, Private Technologies, ...



## 2. 이더리움 네트워크

**퍼블릭 네트워크**

퍼블릭 이더리움 네트워크로는 크게 메인넷과 테스트넷으로 구분.

메인넷 : 거래소에서 직접 사고 팔 수 있는 이더리움을 거래하고 스마트 컨트랙트 등 Dapp 개발

테스트넷 : 메인넷에 아직 올라가기에 준비가 덜 됐을 때 가볍게 시험해볼 수 있는 네트워크

각 네트워크 Id가 존재, Id에 맞게 거래하거나 트랜잭션 보냄.

메인넷에서 거래되는 이더리움과 테스트넷에서 거래되는 그것과 큰 가치 차이.

ehternodes.org 에서 현재 이더리움 메인넷을 이루고 있는 클라이언트 SW의 종류를 볼 수있음. 이더리움은 프로토콜만 맞다면 어떤 클라이언트에서도 거래가 가능. 

가장 대표적인 gath. 이후로 openethereum 등. SSAFY에서는 besu 사용.

**클라이언트(Clinet)란?**

- 네트워크에 노드로 참여하며, RPC(Remote Procedure Call) 요청을 수신, 결과 반환하는 Endpoint

**프라이빗 네트워크**

- 누구나 공개된 Clinet SW로 프라이빗 네트워크 구축 가능
- besu는 엔터프라이즈 환경에 맞게 개량된 Hyperledger의 ethereum 프로젝트



## 3. Ropsten 실습 환경 준비

### MetaMask 설치

MetaMask 지갑

지갑이란?

블록체인 네트워크를 사용할 수 있도록 계정의 개인키를 관리하는 프로그램, 개인키로 사인하여 트랜잭션을 보냄.

- 계정 생성 절차
  - 개인키 생성 : 256 bit의 무작위 숫자 => 64자리의 Hex값으로 인코딩
  - 타원곡선전자서명 알고리즘(ECDSA, secp256k1)을 사용해 공개키 생성
  - Keccak-256 hashing의 마지막 20Byte 선택
  - = 계정주소

MetaMask 설치

니모닉(Mnemonic) : 영단어 조합으로 개인키를 보관

니모닉을 유출당하면 곧 마스터키 유출, 모든 자산을 잃을 가능성.

잘 보관하자.

### 계정 생성



### 네트워크 연결



### 테스트 이더 받기

Faucet(수도꼭지)

테스트넷 환경을 사용할 수 있도록 가치없는 통화를 무료로 제공하는 자금원

rETH 또는 ROP로 표기하기도.



## 4. Ropsten 테스트넷 실습

### MetaMask에서 트랜잭션 보내기

1. Account2 생성 혹은 받을 계정 준비
2. send 클릭

EDIT에서 가스비 조정 가능

가스비가 높은 것 우선으로 처리.

디폴트는 가스비가 조금 높음.

### MetaMask Provider API 활용 실습

프로바이더(Provider)란?

클라이언트를 통해 이더리움 네트워크에 접근할 수 있도록 제공된 JavaScript 객체(Object)

EIP-1193에 정의

https://docs.metamask.io/guide/ethereum-provider.html

개발자 도구 콘솔창에서 ethereum 입력으로 확인 가능 

`ethereum.isConnected()` 로 연결 확인 가능

`ethereum.enable()` 로 계정 활성화

`ethereum.selectedAddress`로 활성화된 계정 확인

### Ethereum Provider로 RPC API 보내기

RPC(Remote Procedure Call)

`ethereum.request(args)`

- `eth_blockNumber` 로 RPC 요청하기

  ```javascript
  ethereum.request({
      method: 'eth_blockNumber',
      params: []
  }).then(res => console.log(res))
  
  // 0xb70bdf
  
  console.log(parseInt('0xb70bdf', 16))  // 11996127
  ```

  현재 11996127개의 블록이 쌓여있음



## 주요 개념 정리

https://eips.ethereum.org/EIPS/eip-1193#definitions

- 이더리움 네트워크의 종류와 특징
  - public
  - private
  - consortium
- 용어
  - 클라이언트
    - 프로바이더로부터 RPC(Remote Procedure Call) 요청을 수신, 결과 반환하는 Endpoint
  - 프로바이더
    - consumer에게 이용가능하도록 만들어진 JavaScript 객체. 클라이언트를 통해 이더리움에 액세스를 제공.
  - 지갑과 계정
    - 지갑 : private key를 관리, 서명작업 수행, 프로바이더와 클라이언트 사이의 미들웨어 역할, 을 하는 end-user 애플리케이션
  - 수도꼭지(Faucet)
  - 가스
  - 이더리움에서 RPC(Remote Procedure Call)
    - 프로바이더나 해당 지갑이나 해당 클라이언트가 처리해야할 절차에 대해, 프로바이더에게 제출된 모든 요청.