# Handling HTTP requests

- Django에서 HTTP 요청 처리하는 방법
  - Django shortcut functions
  - View Decoratos
  - 등등



## Django shortcut functions

- django.shortcuts 패키지
- shortcuts function 종류
  - `render()`
  - `redirect()`
  - `get_object_or_404()`
  - `get_list_or_404()`



### `get_object_or_404()`

- 모델 manager objects에서 `get()`을 호출

  해당 객체가 없다면 DoesNotExist 예외 대신 Http 404 raise

- `get()`의 경우, 데이터가 없으면 에러를 발생시키고 브라우저는 http 500을 발생. 500은 명확한 이유를 알 수 없는 에러임.
- 사용자를 위한 적절한 예외 처리가 필요함.





## Django View decorators

- 다양한 HTTP 기능을 지원하기 위해 뷰에 적용할 수 있는 데코레이터

> - Decorator
>   어떤 함수에 기능을 추가하고 싶을 때, 함수 수정 없이 기능을 연장해주는 함수



- Allowed HTTP methods
  - 요청 메서드에 따라 view 함수에 대한 액세스 제한
  - 조건 미충족시 HttpResponseNotAllowed(405)를 리턴
  - `require_http_methods()`, `require_POST()`, `require_safe()`

- `require_http_methods()`
  - GET, POST 요청만 가능

- `require_POST()`
  - POST 요청만 가능