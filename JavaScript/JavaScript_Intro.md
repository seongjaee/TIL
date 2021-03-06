# JavaScript_Intro

- JavaScript의 필요성
  - 브라우저 화면을 동적으로 만들기 위함
  - 브라우저를 조작할 수 있는 유일한 언어
  - 가장 많이 사용되고 있는 프로그래밍 언어



## History of JS

- 팀 버너스리
  - WWW, URL, HTTP, HTML 최초 설계자
  - 웹의 아버지!
- 브랜던 아이크
  - JS 최초설계자
  - Mozilla 재단 공동 설립자
  - 파이어폭스 전신인 코드네임 피닉스 프로젝트 진행

- 역사
  - 1994년 NN 브라우저가 독점, 표준
  - 브랜던 아이크가 회사 내부 프로젝트 중 JS 개발
  - Mocha -> LiveScript -> JavaScript
  - MS에서 JS를 커스터마이징한 JScript를 만들어 IE 1.0에 탑재
  - 전쟁 시작, 넷스케이프 vs MS
  - 빌 게이츠 주도 하 IE 4 발표 브라우저 시장 장악 시작
    - 윈도우 OS 시장 점유율 90%를 무기로 공격적인 마케팅
    - 결국 2001년 IE의 점유율은 90%
  - 1998년 넷스케이프에서 나온 브랜던 아이크들 모질라 재단 설립
    - 파이어폭스로 IE에 대항
- 제 1차 브라우저 전쟁(1995~2008)
  - MS의 폭발적 성장, IE3 에서 자체적인 JScript 지원, 호환성 문제로 크로스 브라우징 등의 이슈 발생
- 제 2차 브라우저 전쟁(2009~)
  - MS vs Google
  - Google의 Chrome 발표
  - 3년만에 파이어폭스 점유율 돌파, 2012년 전 세계 점유율 1위
  - 승리 요인
    - 압도적인 속도
    - 강력한 개발자 도구 제공
    - 웹 표준 잘 지킴

- 파편화와 표준화
  - 제1차 브라우저 전쟁 이후 많은 브라우저에서 "자체 JS "사용
  - 결국 서로 다른 JS들, 크로스 브라우징 이슈
    - 같은 페이지인데도 브라우저에 따라 동작하지 않음
  - => 웹 표준의 필요성 제기
  - 크로스 브라우징
    - 각각의 브라우저마다 다르게 구현되는 기술을 비슷하게 만들되, 어느 한쪽에 치우치지 않도록 웹 페이지를 제작하는 방법론(동등성)
    - 브라우저마다 렌더링에 사용하는 엔진의 차이가 있음.
  - 1996년 넷스케이프 표준 제정 필요성 주장
    - ECMA 인터네셔널(정보와 통신 시스템을 위한 국제적 표준화 기구)에 표준 제정 요청
  - 1997년 ECMAScript1 탄생
  - 제1차 브라우저 전쟁 이후 다같이 표준화에 적극적으로 힘을 모음
    - MS 빼고

- JavaScript ES6+
  - 2015년 ES2015 탄생
  - "Next-gen of JS"
  - JS의 고질적인 문제들 해결
  - 많은 변화를 맞이한 버전
  - 이때부터 버전순서가 아닌 출시연도를 붙이는 것이 공식명칭, 그러나 통상적으로 ES6으로 부름.
  - 현재는 표준 대부분이 ES6+로 넘어옴

- Vanilla JavaScript

  - 크로스 브라우징, 간편한 활동 등을 위해 많은 라이브러리(jQuery 등) 등장 하지만, ES6 후 점점 사라짐

  - ES6 이후, 순수 자바스크립트 활용 증대




### JS의 인기 비결

- 2005, Google Maps로 AJAX 인기

- 2007, iPhone 인터넷이 핸드폰으로도 가능해짐
- 2008, 자바스크립트 실행 속도가 빠른 크롬(V8 엔진) 등장
- 2009, Node.js 등장. 자바스크립트가 브라우저 영역에서 벗어남.