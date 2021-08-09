# ARIA

> Accessible Rich Internet Applications

[MDN - ARIA](https://developer.mozilla.org/ko/docs/Web/Accessibility/ARIA)

**접근가능한 리치 인터넷 어플리케이션**

장애를 가진 사용자가 웹 콘텐츠와 웹 어플리케이션(특히 JavaScript를 사용하여 개발한 경우)에 더 쉽게 접근할 수 있는 방법을 정의하는 여러 특성을 말합니다.

[MDN - An_overview_of_accessible_web_applications_and_widgets](https://developer.mozilla.org/ko/docs/Web/Accessibility/An_overview_of_accessible_web_applications_and_widgets)

스크린 리더와 같은 보조기기에게 필요한 정보들을 추가적으로 제공하기 위한 방법.

마크업에 특별한 속성들을 추가해 디테일한 정보를 제공한다.

HTML5에서 사용할 수 있는 옵션을 확장하는 이정표 역할도 제공.

ARIA 는 **roles, states, properties** 속성 세 개를 정의한다.

- Roles
  - slider, menu bar, dialog같은 HTML에서 사용하지 못하는 위젯 설명
  - Role이란 접근성 관련 용어에서 특정 UI패턴을 의미함.

- Properties
  - 위젯의 특징 설명, 드래그 가능, 요소 필요, 팝업이 뜸 등
- State
  -  요소의 현재 상태. 보조기기에서 요소의 접근이 불가하거나, 숨겨져 있는 상태 명시

