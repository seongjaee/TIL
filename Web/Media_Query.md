# Media Query

반응형 웹페이지를 위해 bootstrap grid system breakpoints를 사용한다.

Breakpoints 문서를 보다보면 [Media Query](https://getbootstrap.com/docs/5.1/layout/breakpoints/#media-queries) 얘기가 나온다.

`@media (min-width: 576px) { ... }`

MDN 문서에서 media query를 찾아보면 다음과 같이 나온다.

[MDN-Using media queries](https://developer.mozilla.org/ko/docs/Web/CSS/Media_Queries/Using_media_queries)

> **미디어 쿼리**는 단말기의 유형(출력물 vs. 화면)과, 어떤 특성이나 수치(화면 해상도, [뷰포트](https://developer.mozilla.org/ko/docs/Glossary/Viewport) 너비 등)에 따라 웹 사이트나 앱의 스타일을 수정할 때 유용합니다.

`( )`안에 조건을 넣고 해당 조건을 만족하면 `{ }`안의 스타일이 적용된다.

`@media (min-width: 30em) and (orientation: landscape) { ... }`

와 같이 연산자를 이용해 조합할 수도 있다.

`@media print { ... }`

와 같이 프린터에게 작용할 스타일을 지정할 수 도 있다.

미디어의 유형이나 기능을 특정해 스타일을 수정할 때 사용한다.

