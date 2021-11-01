# JavaScript 02

## AJAX

- **Asynchronous JavaScript And XML**, 비동기식 JS 와 XML
- 서버와 통신하기 위해 XMLHttpRequset 객체를 활용
- JSON, XML, HTML, 텍스트 형식 등 다양한 포맷을 주고 받기 가능
- 최근에는 XML보단 JSON을 더 많이 사용
- 페이지 전체를 새로고침하지 않아도 수행되는 *"비동기성"*
  - 사용자의 event에 대해 전체 페이지가 아니라 일부분만 업데이트
- AJAX로 가능한 작업
  - 페이지 새로고침 없이 서버에 요청
  - 서버로부터 데이터를 받고 작업을 수행

### AJAX의 배경

- Google Maps & Gmail에 활용되는 기술을 설명하기 위해 등장한 용어
- 특정 기술이 아닌 기존 여러 기술을 사용하는 새로운 접근법에 대한 용어
- Gmail
  - 메일 전송 요청이 모두 처리 되기전에 다른 페이지로 넘어가도 메일은 전송됨
- Google Maps
  - 스크롤, 줌 등 하나하나가 모두 요청이지만, 페이지는 갱신되지 않음

### XMLHttpRequest 객체

- 서버와 상호작용하기 위해 사용됨.
- 전체 페이지 새로고침 없이 데이터를 받아올 수 있음
- 사용자 작업 방해 없이 페이지 일부 업데이트
- 이름과 달리 XML말고도 모든 종류 데이터 받아올 수 있음
- `XMLHttpRequest()`

## Asynchronous JavaScript(비동기 자바스크립트)

- 동기식
  - 순차적, 직렬적 Task 수행
  - 요청을 보낸 후 응답을 받아야만 다음 동작이 이루어짐. -> blocking
  - JavaScript는 single threaded기 때문

- 비동기식
  - 병렬적 Task 수행
  - 요청을 보낸 후 응답을 기다리지 않고 다음 동작이 이루어짐 -> non-blocking
  - JavaScript는 single threaded기 때문

- 왜 비동기식이어야하는가?

  - **"human-centered design with UX"**
  - 사용자 경험!

  - 매우 큰 데이터를 동반하는 앱의 경우, 
  - 동기식 코드라면 데이터를 모두 불러온 뒤 앱이 실행
    - 데이터를 모두 불러올 때까지 앱이 멈춰있음.
    - 화면이 멈추고 응답하지 않는 것 같은 UX
  - 비동기식 코드라면 데이터를 요청하고 응답 받는 동안, 앱 실행을 함께 진행
    - 데이터 불러오는 동안 지속적으로 응답하는 화면, 쾌적한 UX
  - 따라서 많은 웹 API 기능은 비동기 코드를 사용하여 실행됨

- Threads

  - 프로그램이 작업을 완료하기 위해 사용할 수 있는 단일 프로세스
  - 각 thread는 한 번에 하나의 작업만 수행

- **JavaScript는 single threaded다.**

  - 컴퓨터가 여러 개의 CPU가 있더라도 main thread라 불리는 단일 스레드에서만 작업 수행
  - 즉 이벤트를 처리하는 Call Stack이 하나인 언어
  - 이 문제를 해결하기 위해 JavaScript는
    - 즉시 처리하지 못하는 이벤트들을 다른 곳(Web API)으로 보내서 처리하도록함.
    - 처리된 이벤트들은 처리된 순서대로 대기실(Task queue)에 줄을 세워 둠
    - Call Stack이 비면 담당자(Event Loop)가 대기 줄에서 가장 앞의 이벤트를 Call Stack으로 보냄

### Concurrency model

- Event loop를 기반으로 하는 동시성 모델
- Call Stack
  - 요청이 들어올 때마다 요청을 순차 처리하는 Stack 형태 자료 구조

- Web API
  - 브라우저 영역에서 제공하는 API
  - setTimeout(), DOM events, AJAX로 데이터 가져오기 등 처리
- Task Queue
  - 비동기 처리된 callback 함수가 대기하는 Queue 형태 자료구조
  - main thread 끝난 후 실행
- Event loop
  - Call Stack이 비어있는지 확인
  - 비었다면 Task Queue에 대기 중인 callback 함수 있는지 확인
  - 있다면 가장 앞에 있는 callback 함수를 Call Stack으로 가져옴

- Zero delays

  - 실제로 0ms 후 callback 함수가 시작된다는 의미가 아님
  - delay는 요청을 처리하는데 필요한 최소 시간.

- 순차적 비동기 처리

  - 결국 Web API로 들어오는 순서는 중요치 않음, 어떤 이벤트가 먼저 처리되느냐가 중요
  - 이를 해결하기 위한 순차적인 비동기 처리를 위한 2가지 작성 방식

  1. Async callbacks
     - 백그라운드에서 실행을 시작할 함수를 호출할 때 인자로 지정된 함수
     - addEventListener() 의 두번째 인자
  2. promise-style
     - Modern Web APIs 에서의 새로운 코드 스타일
     - XMHttpRequset 객체를 이용하는 구조보다 좀더 현대적인 버전



## Callback Function

- callback function

  - 다른 함수에 인자로 전달된 함수
  - 외부 함수 내에서 호출되어 작업을 완료
  - 동기식, 비동기식 모두 사용
  - 비동기 작업 완료 후 코드 실행을 계속하는데 사용되는 경우를 비동기 콜백이라고 함

- JavaScript의 함수는 First Class Object

  - 일급 객체
    - 다른 객체들에 적용할 수 있는 연산을 모두 지원하는 객체
  - 일급 객체의 조건
    - **인자**로 넘길 수 있어야함
    - **함수의 반환 값**으로 사용 가능해야함
    - **변수에 할당**할 수 있어야함

- Async callbacks

  - 백그라운드에서 코드 실행을 시작할 함수를 호출할 때 인자로 지정된 함수

  - 백그라운드 코드 실행이 끝나면 callback 함수를 호출하여 작업 완료를 알리거나 다음 작업을 실행하게 할 수 있음

  - callback 함수가 다른 함수의 인자로 전달될 때, 함수의 참조를 인수로 전달할 뿐, 즉시 실행이 아님. 함수의 body에서 called back 됨.

    정의된 함수는 때가 되면 callback 함수를 실행하는 역할.

- 콜백 함수 사용 이유

  - 명시적 호출이 아닌 특정 루틴 또는 action에 의해 호출됨.
  - 비동기 로직을 수행할 때 callback 함수가 필수적임.

- callback Hell

  - 순차적인 연쇄 비동기 작업을 처리하기 위해 callback 함수를 호출하고 또 callback 함수를 호출하고... 반복
  - 연쇄 비동기 작업을 마주하는 상황 = callback Hell, pyramid of doom

  - 위의 상황이 발생하면 디버깅, 코드 가독성 통제 어려움

- callback Hell 해결
  - Keep your code shallow
  - Modularize
  - Handle every single error
  - **Promise callbacks**



## Promise

### Promise object

- 비동기 작업의 최종완료 또는 실패를 나타내는 객체
  - 미래의 완료 또는 실패와 그 결과값을 나타냄
  - 미래의 어떤 상황에 대한 약속
- 성공(이행) 시
  - `.then()`
- 실패(거절) 시
  - `.catch()`



### Promise methods

- `.then(callback)`
  - 이전 작업이 성공했을 때 수행할 작업을 나타냄
  - 각 callback 함수는 이전 작업의 성공 결과를 인자로 받음
  - 성공했을 때의 코드를 callback 함수 안에 작성
- `.catch(callback)`
  - `.then` 이 하나라도 실패하면 동작
  - 이전 작업 실패로 생성된 error 객체를 catch 블록 안에서 사용 가능
- 각각의 .then() 블록들은 서로 다른 promise를 반환
- .then() 을 여러 개 사용(chaining)하여 연쇄적인 작업 가능
- 즉, 비동기 작업을 순차적으로 수행할 수 있음.
- .then(), .catch() 모두 promise를 반환하기 때문에 chaining 가능
- 주의 
  - 반환 값이 반드시 있어야함.
  - 없으면 callback함수가 이전 promise를 인자로 받을 수 없음.

- `.finally(callback)`
  - Promise 객체 반환.
  - 결과와 상관없이 반드시 실행됨
  - 어떤 인자도 전달받지 않음.
  - .then(), .catch() 블록에서의 코드 중복 방지 시에 사용



### Promise가 보장하는 것

- Event Queue에 배치되는 엄격한 순서로 호출됨
- 여러 개의 callback 함수를 추가(Chaining) 가능





## Axios

- "Promise based HTTP client for the browser and Node.js"
- 브라우저를 위한 Promise 기반의 클라이언트
- AJAX 요청이 편리해짐





### async & await

- 비동기 코드를 작성하는 새로운 방법
- 기존 Promise 시스템 위에 구축된 syntactic sugar
  - Promise 구조의 then chaining을 제거
  - 비동기 코드를 조금 더 동기 코드 처럼 표현









- 2007 iPhone 인터넷이 핸드폰으로도 가능해짐
- 2008 자바스크립트 실행 속도가 빠른 크롬 등장
- Adobe 사망