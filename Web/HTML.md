# Web_01

웹 표준 : W3C - HTML5, WHATWG - HTML Living Standard

[Can I use?](https://caniuse.com/)

## HTML

Hyper Text Markup Language

- Hyper
  - 정보가 다중으로 연결된
- Hyper Text
  - 참조(Hyper Link)를 통해 다른 페이지로 즉시 접근가능한 텍스트
  - http / html
- Markup
  - 텍스트의 역할을 표시, 마킹

- Markup Language
  - 태그 등을 이용해 문서나 데이터의 구조를 명시하는 언어
- 정리
  - 웹 페이지를 작성하기 위한, 구조를 잡기 위한 언어
  - 웹 컨텐츠의 의미와 구조를 정의하는 역할
- .html

### HTML 기본 구조

- html 요소

  - 최상위 요소
  - head와 body로 구분

- head 요소

  - 문서 제목, 문자 코드 등 **해당 문서 정보**
  - 브라우저에 나타나지 않음
  - Open Graph Protocol
    - HTML 문서의 메타 데이터를 통해 문서의 정보 전달
    - 카톡에 링크보내면 보이는 그거
    - 페이스북에서 제작
    - 메타 정보의 제목, 설명 등이 쓰여짐

- body 요소

  - 브라우저 화면에 나타나는 **실제 내용에 대한 정보**

- DOM(Document Object Model) 트리

  - 문서 객체 모델
  - 문서를 해석한 결과
  - 태그별로 객체
  - 들여쓰기로 부모, 자식 관계
  - 문서의 구조화된 표현을 제공, -> 프로그래밍 언어가 구조에 접근하도록 함, 문서 구조, 스타일 등을 변경할 수 있게함
  - Web Page의 객체 지향 표현

- 요소(element)

  - `<h1>contents</h1>` 
  - 태그(시작 태그 & 종료 태그)와 내용(contents)으로 구성
    - 태그는 컨텐츠 정보의 성격과 의미를 정의
  - 내용이 없는 태그들
    - br, hr, img, input, link, meta
  - 요소는 중첩 가능
    - 중첩을 통해 문서를 구조화
    - 태그 잘못되어도 오류 반환 안함

- 속성(attribute)

  - `<a href="https://google.com"></a>`
    - href : 속성명, "https:/..." : 속성값

  - 속성 작성방식

    - =사이에 공백 x. 속성값은 ""로 사용

  - 태그의 부가정보 설정 기능

  - 시작 태그에 작성, 이름과 값이 하나의 쌍으로 존재

  - 태그별로 사용가능한 속성이 다르지만, 태그와 상관없이 사용 가능한 속성도 있음

  - HTML Global Attribute

    - 모든 HTML 요소에 공통적으로 사용 가능한 속성
    - 몇몇 요소엔 효과 없을 수도
    - id, class

    - hidden 등등

- 시맨틱 태그

  - 의미론적 요소를 담는 태그, (div x)
  - 대표적인 태그들
    - header : 문서 전체 또는 섹션 헤더
    - nav : 내비게이션
    - aside : 사이드, 메인 콘텐츠와 관련성이 적음
    - section : 문서의 일반적인 구분, 컨텐츠 그룹
    - article : 독립적으로 구분되는 영역
    - footer : 문서 전체 또는 섹션 푸터
  - 의미 있는 정보의 그룹을 태그로 표현
  - 구역을 나누는 것 뿐만 아니라 의미를 가지는 태그를 활용하기 위한노력
  - Non semantic 요소는 div, span 등
  - 요소의 의미가 명확해지기때문에 가독성 상승, 유지보수 좋아짐
  - 검색엔진 최적화를 위해 마크업을 효과적으로 할 필요

- 시맨틱 웹

  - 웹 상에 존재하는 웹 페이지에 메타 데이터를 부여해,
  - 의미와 관련성을 가지는 거대한 데이터베이스로 구축하고자하는 발상



### HTML 문서 구조화

- 인라인 / 블록 요소
  - 블록 : 자리 다 차지
  - 인라인 : 요소 만큼만 자리 차지
- 그룹 컨텐츠
  - `<p>` : 하나의 문단
  - `<hr>` : 문단 레벨 요소에서 주제의 분리
  - `<ol>`, `<ul>` :  ol : 정렬된 목록, ul : 정렬되지 않은 목록
  - `<pre>`, `<blockquote>` : pre : 미리 서식을 지정한 텍스트, blockquote : 긴 인용문, 들여쓰기 한 것으로 표현됨
  - `<div>` : 플로우 컨텐츠를 위한 통용 컨테이너, css로 꾸미기 전에는 레이아웃이나 컨텐츠에 영향 x
- 텍스트 관련 요소
  - `<a>` : 링크
  - `<b>` vs. `<strong>` : 글씨 두껍게
    - b는 그냥 굵은 글씨, strong은 강조의 의미, 스크린 리더도 강조해서 읽음
  - `<i>` vs. `<em>` : 이탤릭체
  - `<span>`, `<br>`, `<img>`
  - 등등
- table 표
  - tr, td, th
  - thead, tbody, tfoot
  - caption
  - 등등
- form
  - 서버에서 처리될 데이터를 제공하는 역할
  - 검색, 로그인 등등
  - `<form>`기본 속성
    - action : 어디로 데이터를 보낼지
    - method : 어떤 http method
- input
  - 다양한 타입을 가지는 입력 데이터 필드
  - `<label>` : 서식 입력 요소 캡션, 사용자에게 텍스트 표시, 화면리더기가 읽어주는 등 기능
  - `<input>` 공통 속성
  - input 유형
    - input 요소의 동작은 type에 따라 달라짐
    - [input type MDN](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input)

