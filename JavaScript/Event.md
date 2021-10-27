# Event

## Event 개념

- 네트워크 활동이나 사용자 상호작용 같은 사건의 발생을 알리는 객체
- 이벤트 발생
  - 마우스 클릭, 키보드 입력 등 사용자 행동
  - 특정 메서드 호출로 프로그래밍적으로도 발생 가능

## Event 기반 인터페이스

- AnimationEvent, ClipboardEvent 등
- UIEvent
  - 간단한 사용자 인터페이스 이벤트
  - Event 상속 받음
  - MouseEvent, KeyboardEvent, InputEvent, FocusEvent 등의 부모 객체 역할



## Event handler - addEventListener()

- `EventTarget.addEventListener(type, listener[, options])`
  - 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정
  - 이벤트를 지원하는 모든 객체를 대상으로 지정 가능
  - type
    - 반응할 이벤트 유형
  - listener
    - 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체
    - EventListener 인터페이스 혹은 JS function 객체(콜백 함수)여야함



## Event 취소

- `Event.prevenDefault()`
  - 현재 이벤트의 기본 동작 중단
  - 태그의 기본 동작을 작동하지 않게 막음
  - 이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지 않고 그 이벤트를 취소
    - 취소 가능 여부는 event.cancelable로 확인 가능
    - scroll 이벤트는 취소할 수 없음

