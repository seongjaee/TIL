# EAFP & LBYL

[파이썬 용어집(Python glossary)](https://docs.python.org/3/glossary.html#term-eafp)



코딩 스타일, 접근방법



## EAFP

> Easier to ask for forgiveness than permission
>
> "허락보다 용서를 구하기가 쉽다."

(파이썬의 스타일)

우선 검사를 수행하지 않고 일단 실행한 후 예외처리를 진행하는 스타일

파이썬 코드가 문제 없이 실행될 것을 전제로 코드를 실행

`try...except` 구문이 많아지는 게 특징.



## LBYL

> Look before you leap
>
> "뛰기 전에 보라."

어떤 것이 실행하기 전에 미리 에러가 날만한 요소들을 조건문으로 사전적으로 검사한 후 수행

`if...else` 구문이 많아지는 게 특징.

