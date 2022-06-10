# Ethereum 연습 01

## 1. 소유 계정의 잔액 조회

https://ethdocs.org/en/latest/ether.html

### Ether와 Wei

Ether는 Ethereum의 통화 이름. EVM(Ethereum Virtual Machine) 내에서 계산 비용 지불에 사용. ether용 가스(gas) 구입을 통해 간접적으로 이루어짐.

#### Denomination

디노미네이션.

사전 : 통화단위의 호칭의 절하.

이더리움은 ether 단위로 사용되는 디노미네이션 metric 시스템을 가지고 있음. 각 디노미네이션은 고유의 이름이 있음.

Wei는 ether의 가장 작은 디노미네이션 (base unit)임.

많이 혼동하지만 이더리움은 통화 단위가 아님.

| Unit                    | Wei Value | Wei                       |
| ----------------------- | --------- | ------------------------- |
| **wei**                 | 1 wei     | 1                         |
| **Kwei (babbage)**      | 1e3 wei   | 1,000                     |
| **Mwei (lovelace)**     | 1e6 wei   | 1,000,000                 |
| **Gwei (shannon)**      | 1e9 wei   | 1,000,000,000             |
| **microether (szabo)**  | 1e12 wei  | 1,000,000,000,000         |
| **milliether (finney)** | 1e15 wei  | 1,000,000,000,000,000     |
| **ether**               | 1e18 wei  | 1,000,000,000,000,000,000 |

### 소유 계정의 잔액 조회 코드

```javascript
const address = ethereum.selecetedAddress

ethereum.request({
    method: 'eth_getBalance',
    params: [address, 'latest']
})
    .then(res => {
    	const wei = parseInt(res);
    	const ether = wei / (10 ** 18)
    	console.log(ether)
	})

// 0.989968499998929
```



## 2. RPC API를 통해 데이터를 포함한 트랜잭션 보내기

Metamask playground 이용

https://metamask.github.io/api-playground/api-documentation

### 트랜잭션 보내기

1. **호출**

```
{
    "jsonrpc": "2.0",
    "method": "eth_sendTransaction",
    "params": [
        {
            "from": "0x2b8da8bA7614b7a1d288173BB38d71eE63Be49dE",
            "to": "0x14DDf13F5C715D6cdDeF81b077CACF21C236282c",
            "gas": "0x9c40",
            "gasPrice": "5f5e100",
            "value": "0x9c40",
            "data": "0x68656c6c6f20657468657265756d"
        }
    ],
    "id": 0
}
```

2. **응답**

```
{
  "jsonrpc": "2.0",
  "result": "0xc1a09256a7b1985fdfec5329c3499f7aa3241405a08e0ee1d6bb4ec0d9b6adb1",
  "id": 0
}
```

## 3. 보낸 트랜잭션 결과 확인

Metamask playground **RPC API**

`getTransactionByHash` **요청**

```javascript
{
    "jsonrpc": "2.0",
    "method": "eth_getTransactionByHash",
    "params": [
        "0x17c5df9e654e27ef2b219352c9b82c45890ad4135d6ade2e03301f947967dd5a"
    ],
    "id": 0
}
```

**응답 결과**

```javascript
{
    "jsonrpc": "2.0",
    "result": {
        "accessList": [],
        "blockHash": "0x820d324b750ffa1c50d5c6b815707de86abb6a8e0d89ad8f349c553cdee8c996",
        "blockNumber": "0xb7156a",
        "chainId": "0x3",
        "from": "0x2b8da8ba7614b7a1d288173bb38d71ee63be49de",
        "gas": "0x9c40",
        "gasPrice": "0x59682f0d",
        "hash": "0x17c5df9e654e27ef2b219352c9b82c45890ad4135d6ade2e03301f947967dd5a",
        "input": "0x68656c6c6f20657468657265756d",
        "maxFeePerGas": "0x59682f0d",
        "maxPriorityFeePerGas": "0x59682f00",
        "nonce": "0x1",
        "r": "0x45f1e6063e33a2ec07cfb2ca04a86e2c4c0b7beecd569c4f0db9d7ddf76e394",
        "s": "0x57d64d49d27ca1cdbf39316dcd0f9a34803ec4c36465812d182cae86a825e72d",
        "to": "0x14ddf13f5c715d6cddef81b077cacf21c236282c",
        "transactionIndex": "0x8",
        "type": "0x2",
        "v": "0x1",
        "value": "0x9c40"
    },
    "id": 0
}
```



**브라우저 콘솔**

`getTransactionReceipt` **요청**

```javascript
ethereum.request({
  method: 'eth_getTransactionReceipt',
  params: ["0x17c5df9e654e27ef2b219352c9b82c45890ad4135d6ade2e03301f947967dd5a"]
})
  .then(res => console.log(res))
```

**응답**

```javascript
{
    blockHash: "0x820d324b750ffa1c50d5c6b815707de86abb6a8e0d89ad8f349c553cdee8c996",
	blockNumber: "0xb7156a",
	contractAddress: null,
	cumulativeGasUsed: "0x63374f",
	effectiveGasPrice: "0x59682f0d",
	from: "0x2b8da8ba7614b7a1d288173bb38d71ee63be49de",
	gasUsed: "0x52e8",
	logs: [],
	logsBloom: "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
	status: "0x1",
	to: "0x14ddf13f5c715d6cddef81b077cacf21c236282c",
	transactionHash: "0x17c5df9e654e27ef2b219352c9b82c45890ad4135d6ade2e03301f947967dd5a",
	transactionIndex: "0x8",
	type: "0x2",
}
```



### Transaction과 Transaction Receipt

https://ethereum.org/en/developers/docs/transactions/

#### What's a Transaction

이더리움 트랜잭션은 외부 소유 계좌(즉 컨트랙트가 아닌 사람이 관리하는 계좌)에 의해 시작된 액션을 말함. 

EVM의 상태를 바꾸는 트랜잭션은 네트워크 전체로 브로드캐스트되어야함. 모든 노드들이 EVM에서 실행될 트랜잭션에 대한 요청을 브로드캐스트 할 수 있음. 이 이후, 채굴자는 트랜잭션을 실행하고 나머지 네트워크에 상태 변화 결과를 전파함.

트랜잭션엔 수수료가 필요하고, 반드시 채굴되어야 유효함.

제출된 트랜잭션은 다음의 정보를 포함

- `recipient` : 수신 주소(외부 소유 계좌의 경우, 가치 전송. 컨트랙트 계좌의 경우, 컨트랙트 코드 실행)
- `signature` : 전송자의 식별자.
- `value` : 전송자가 수신주소에 보낼 ETH의 양. wei.
- `data` : 임의 데이터 포함하는 옵션 필드
- `gasLimit` : 트랜잭션에 소비될 수 있는 최대 가스 양.
- `maxPriorityFeePerGas` : 채굴자에게 팁으로써 포함될 최대 가스 양
- `maxFeePerGas` : 트랜잭션에 지불할 최대 가스 양

https://ethereum.org/en/glossary

#### Transaction

특정 주소를 대상으로, 발신 계정이 서명한 이더리움 블록체인에 커밋된 데이터입니다. 트랜잭션에는 해당 트랜잭션의 가스 제한과 같은 메타데이터가 포함.

#### Transaction receipt

이더리움 클라이언트가 특정 거래의 결과를 나타내기 위해 반환하는 데이터. 트랜잭션의 해시, 블록 번호, 가스 사용량, 스마트 컨트랙트 배포 시 컨트랙트 주소 등이 포함.
