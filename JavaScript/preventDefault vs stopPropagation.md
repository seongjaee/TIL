## [Event.preventDefault()](https://developer.mozilla.org/ko/docs/Web/API/Event/preventDefault)

어떤 이벤트를 명시적으로 처리하지 않은 경우, 해당 이벤트에 대한 사용자 에이전트의 기본 동작을 실행하지 않도록 지정.

preventDefault()를 호출한 이벤트도 수신기 중 하나에서 stopPropagation() 또는 stopImmediatePropagation()을 호출하기 전까지는 다른 이벤트와 마찬가지로 전파.

EventTarget.dispatchEvent()로 발송한 이벤트처럼 취소 불가능한 이벤트의 경우, preventDefault()를 호출해도 아무 효과도 나타나지 않음.



## [Event.stopPropagation()](https://developer.mozilla.org/ko/docs/Web/API/Event/stopPropagation)

**`stopPropagation()`** 메서드는 현재 이벤트가 캡처링/버블링 단계에서 더 이상 전파되지 않도록 방지합니다

전파를 방지해도 이벤트의 기본 동작은 실행.

stopPropagation()이 링크나 버튼의 클릭을 막는 것은 아님.

기본 동작 방지는 preventDefault()가 하는 일.

 같은 이벤트 대상에 부착한 다른 수신기까지 막지는 않음.

이거까지 막는건 [`stopImmediatePropagation()`](https://developer.mozilla.org/ko/docs/Web/API/Event/stopImmediatePropagation)

---



HTML 상에서 사용자 이벤트는 전파됨.

a태그에 클릭이벤트 발생시 a태그의 부모 태그에 순차적으로 이벤트가 전파.

```html
<ul>
    <li>
    	<a href="#">Click!</a>
    </li>
</ul>
```

a태그를 클릭하면 li태그, ul태그로 순차적으로 젆파.

a태그의 onClick, li태그의 onClick, ul태그의 onClick이 실행.

이때 원치 않는 ul태그의 onClick까지 실행이 될 수 있음.

이것을 막기 위한게 stopPropagation()

즉, 부모 태그로의 이벤트 전파를 중지한다는 뜻.



그 반면, preventDefault()는 애초에 브라우저 행동을 막게됨.

a태그 클릭 시, click이벤트와 함께, href에 따라 웹브라우저를 이동시킴.

preventDefault()는 클릭 이벤트 외에 브라우저 행동을 막게됨.

