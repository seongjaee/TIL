# RESTful API

>  설계 방법론은 지키지 않았을 때 잃는 것보다 지켰을 때 얻는 것이 훨씬 많음

## API

- Application Programming Interface
- 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스
  - 애플리케이션과 프로그래밍으로 소통
  - 소통 방식들 : CLI 명령줄, GUI 그래픽, API 프로그래밍
- Web API
  - 웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세
  - 현재 웹 개발은 모든 걸 직접 개발보단 여러 Open API를 활용하는 추세
- 응답 데이터 타입
  - HTML, XML, JSON

## REST

- REpresentational State Transfer
- API Server를 개발하기 위한 소프트웨어 설계 방법론
  - 로이 필딩, 2000
- 네트워크 구조 원리의 모음
- REST 원리를 따르는 시스템을 RESTful라고 지칭

- 자원을 정의하는 방법에 대한 고민

- 자원과 주소 지정 방법
  1. 자원 : URI
  2. 행위 : HTTP Method
  3. 표현 : 자원과 행위를 통해 궁극적으로 표현되는 결과물, JSON으로 표현된 데이터 제공
- RESTful API
  - REST 원리를 따라 설계한 API
- 결국 URL에는 행동이 아닌 명사만 남겨두겠다! 행동은 HTTP Method로 결정!

## JSON

- JavaScript Object Notation
  - lightweight data-interchange format
  - JavaScript 표기법을 따른 단순 문자열
- 특징
  - 사람이 다루기 쉬움. 기계가 파싱하고 만들기 쉬움
  - 파이썬의 dictionary, 자바스크립트의 object, C 계열의 언어가 갖고있는 자료구조로 쉽게 변화할 수 있는 key-value 형태 구조

## RESTful API

- REST 원리를 따라 설계한 API

