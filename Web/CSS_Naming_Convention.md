# CSS Naming Convention

>There are only two hard things in Computer Science: cache invalidation and naming things. -- Phil Karlton

CSS에서도 이름 짓기는 어렵다.

[http://getbem.com/naming/](http://getbem.com/naming/)

## BEM : Block, Element, Modifier로 나누어 이름짓기

### Block

Block은 그 스스로 의미를 가지고 있는 녀석들.

Naming 방법

`block-name`  - 알파벳, 숫자, - 로 구성

### Element

Block의 일부분으로, 독립적인 의미는 없음

Naming 방법

`block-name__element-name` - 속한 Block 이름 뒤에 언더바(_) 두 개 그리고 요소 이름

### Modifier

Block들, Elements들의 상황, 상태를 나타냄.

Naming 방법

`block-name__element-name--mod` - 블록이나 요소 뒤에 하이픈(-) 두 개 그리고 Modifier 이름

