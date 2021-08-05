# css 디버깅에 대해서...:cry:

css 스타일 레이아웃을 만지다보면 원하는 결과가 나오지 않을 때가 많다.

그럴때 안된다고 코드를 바로 지우는게 아니라 왜 안되는지 확인하자.

크롬 개발자 도구에서 Elements Style 탭에서 현재 요소에 적용된 스타일을 확인할 수 있다.

위에서부터 스타일 우선순위가 높다.

특히 맨위 `element.style`는 우선순위가 가장 높은(`!important`을 제외하고) 인라인 스타일이다.

중간에 `user agent stylesheet`는 브라우저가 알아서 적용한 스타일.

`Inherited from ...`은 상속받은 스타일로 어디서 상속을 받았는지 확인할 수 있다.

상속의 경우, 상속이 되는 속성과 되지 않는 속성이 있다. 꼭 해보고 확인하자.

적용되지 않는 스타일은 중간에 빗금이 그어져 있다.

뇌피셜말고 진짜 확인하자. 상속은 왜 안됐는지 누가 방해하는지

되더라도 "됐네 난 천재야" 하고 넘어가지말고 왜 됐는지 이해해야한다.

공식문서를 가까이 하자.

[https://developer.mozilla.org/ko/](https://developer.mozilla.org/ko/)

[https://getbootstrap.com/docs/5.1/getting-started/introduction/](https://getbootstrap.com/docs/5.1/getting-started/introduction/)

