# 특화 PJT NFT 사전학습 4강

FundRaising 구현하기

## 1. FundRaising 시작하기

특정 사람에게 모금을 해서 기부를 하는 프로세스를 가지고 있음

**기능 설명**

- 일회성으로 동작하는 모금 컨트랙트
- 일정 기간 동안만 이더를 지불하여 모금에 참여할 수 있음.
- 모금, 현재 모금액 확인, 모금액 수령 기능 제공



### 생성자 선언

- 생성자 매개변수 추가 및 상태 변수에 저장
- 컨트랙트 배포 시 모금 기간과 모금액 수령자를 지정하도록 변경

```solidity
uint public constant MINIMUM_AMOUNT = 1e16;
    uint public fundRaisingCloses;
    address public beneficiary;

    constructor (uint _duration, address _beneficiary) {
        fundRaisingCloses = block.timestamp + _duration;  // block.timestamp : 현재 블록의 유닉스 타임스탬프 값
        beneficiary = _beneficiary;
    }
```





## 2. `fund()`

- `payable` : 이더 전송이 일어나는 함수
  - `msg.value` : 트랜잭션에 얼마를 보냈는지 알 수 있는 전역 변수

- 솔리디티에서는 유효성 체크를 위해 if문 보다는 `require` 를 사용을 권함.
  - `require(판별문, "에러 메시지")`
  - 판별문이 true가 아니면 에러메시지 출력 후 함수 종료
  - 함수 실행을 미리 막아 가스비 소모를 막음

```solidity
address[] funders;

    // 1. 0.01 ether 이상으로 모금에 참여 가능
    // 2. 지정된 모금 시간 이내에만 참여 가능 
    // 3. 모금이 완료되면 모금자를 저장
    function fund() public payable {  // payable : 이더를 받을 수 있도록하는 키워드
        require(msg.value >= MINIMUM_AMOUNT, "MINIMUM AMOUNT: 0.01 ether");
        require(block.timestamp < fundRaisingCloses, "FUND RAISING CLOSED");
        
        address funder = msg.sender;  // 메시지 송신자를 알 수 있는 전역 변수
        funders.push(funder);
    }
```



## 3. `currentCollection()`

```solidity
// 1. 현재까지 모금된 금액을 누구나 확인 가능
    function currentCollection() public view
    returns(uint256){
        return address(this).balance;  // address의 잔액 확인
    }
```



## 4. `withdraw()`

- `modifier` 
  - 함수 변경자, 함수 실행 전, 실행 후 특정 기능을 하도록 설정 가능.
  - 특정 로직을 재사용 가능하다는 장점.
  - 함수를 실행 전에 require를 사용해 불필요 gas 소모 줄임.
  - `_` : 함수가 실행되는 시점.

```solidity
modifier onlyBeneficiary() {
        require(msg.sender == beneficiary);
        _;
    }

    // 1. 지정된 수령자만 호출 가능
    // 2. 모금 종류 이후에만 호출 가능
    // 3. 수령자에게 컨트랙트가 보유한 이더를 송금
    function withdraw() public payable onlyBeneficiary {
        require(block.timestamp > fundRaisingCloses);
        msg.sender.transfer(address(this).balance);  // <address payable>.transfer(amount) : 요청 주소에게 보유 이더 송금

    }
```

