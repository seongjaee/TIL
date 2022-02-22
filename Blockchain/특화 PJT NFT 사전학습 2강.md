# 특화 PJT NFT 사전학습 2강

목차

1. Smart contract란?
2. 실습환경 준비
3. 배포
4. 호출



## 1. Smart Contract란?

1990년대 Nick Szabo가 소개한 개념

디지털 형식으로 명시된 서약(Commitment)들의 집합.

결코 스마트하지 않은 단순 컴퓨터 프로그램.

법적 맥락 없음.

다소 잘못된 용어임에도 불구하고 자리잡음.

계약 내용이 담긴 컴퓨터 코드.



블록체인에서의 정의 : 불변의 컴퓨터 프로그램 (마스터링 이더리움)

- 컴퓨터 프로그램
- 불변(immutable) 한번 배포되면 변경 불가
- 결정적, 실행한 결과가 모두 같음.
- EVM 위에서 동작
- 탈중앙화된 Worl computer, 동일한 상태 유지

Smart Contract 작성 언어

- **Solidity**
- LLL
- Viper
- Assembly



## Smart Contract 배포와 호출

Smart contract Code

( 컴파일 )

EVM Bytecode, ABI in JSON

( 트랜잭션 생성 )

{

​	from: ...,

​	to : ...,

}

( 서명 )

Sending transaction



이때 발생하는 컨트랙트에도 컨트랙트 주소 (CA Contract Address)가 있음.

이와 반대로 자신의 지갑 주소는 외부 소유 주소(external owned address)

**용어 정리**

- Bytecode
- ABI(Application Binary Interface)
- CA(Contract Address)



## 2. 실습 환경 준비

### Remix IDE

스마트 컨트랙트 IDE

## 3.Smart Contract 배포

1) 배포할 컨트랙트 준비
   - FILE_EXPLORERS > contracts 폴더 > 1_Storage.sol

2) 컴파일
   - 왼쪽 사이드바 SOLIDITY COMPILER
   - Compile 버튼 클릭
     - 배포 가능한 컨트랙트 생성
     - ABI, Bytecode 생성
   - 결과 확인, FILE_EXPLORERS > contracts / artifacts 폴더 생성 확인

3) 배포
   - DEPLOY & RUN TRANSACTIONS
     - ENVIRONMENT, ACCOUNT 선택
       - (JavaScript VM으로 내 머신에서만 배포 가능)
     - Deploy 버튼으로 배포

## 4. Smart Contract 호출

1. 호출

   - DEPLOY & RUN TRANSACTIONS, Deployed Contracts 열기

   store() 와 retreive()

   store는 set, retreive는 get.

   retreive를 호출할 땐 gas가 발생하지 않음.

   하지만 store를 호출할 땐 gas 발생.

   number라는 변수는 이더리움 네트워크 모든 컴퓨터에 있음. 모든 컴퓨터에 대해 변수 값을 할당하는 계산 작업을 해야하기 때문에 가스가 소모.

2. Deployed Contract 삭제
   - CA 복사 후 삭제

3. CA로 컨트랙트 접근
   - 복사한 CA 붙여넣기 => At Address 버튼 클릭
   - 제 3자도 컨트랙트를 불러와 number에 저장된 값 retreive 가능



## 정리

**컨트랙트 전반적인 과정**

먼저 스마트 컨트랙트 코드 작성. 

이 코드 컴파일하면, EVM Bytecode와 ABI in JSON이 추출.

그리고 이 Bytecode를 트랜잭션에 담아 트랜잭션을 생성하고,

지갑에서 개인키로 이 트랜잭션에 서명하면 블록체인 네트워크에 전송.

전세계 네트워크가 이 바이트코드 실행, 트랜잭션 전파.

바이트 코드는 블록에 담김.

CA와 ABI를 통해 배포되어있는 컨트랙트들 함수 호출 가능

