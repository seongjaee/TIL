# Django - Authentication

## Django Authentication System

- Django 인증 시스템은 `django.contrib.auth`에 Django contrib module로 제공
- settings.py `INSTALLED_APPS` 에 
  - `django.contrib.auth` : 인증 프레임워크 핵심, 기본 모델 포함
  -  `django.contrib.contenttypes` : 사용자가 생성한 모델과 권한 연결
- Django 인증 시스템은 인증(Authentication)과 권한(Authorization) 부여 제공
- auth와 관련된 django 앱은 `accounts`로 짓는 것이 관례
  - `accounts`로 지어야 사용하기 편한 기능들이 있음



## Django 에서의 Session

- Django의 세션은 미들웨어를 통해 구현
  - 미들웨어 MIDDLEWARE : 요청과 응답 처리 중간에서 작동하는 시스템, 주로 데이터 관리, 앱 서비스, 메시징, 인증 및 API 관리 담당
- db-backed sessions 저장 방식이 기본값
- 세션 정보는 Django DB `django_session` 테이블에 저장
- 세션은 서버의 리소스를 활용하기 때문에 모든 걸 세션으로 구현하면 서버에 부하

- MIDDLEWARE 에서 인증 시스템
  - `SessionMiddleware` : 요청 전반에 걸쳐 세션 관리
  - `AuthenticationMiddleware` : 세션을 사용하여 사용자를 요청과 연결



## 로그인

- Session CREATE - 로그인
- Django는 인증에 관한 built-in forms 제공

- AuthenticationForm
  - 사용자 로그인을 위한 form
  - request를 첫번째 인자로 함
  - `forms.Form` 를 상속받은 클래스

- `login()`
  - 현재 세션에 연결하려는 인증된 사용자가 있는 경우 사용
  - view 함수에서 사용
  - HttpRequest 객체와 User 객체 필요
  - session framework를 사용해 세션에 user ID 저장 (=로그인)
  - view의`login` 함수와 구분하기위해 이름 변경
  - 로그인된 사용자는 django DB django_session 에 저장됨



- `get_users()`
  - `AuthenticationForm`의 인스턴스 메서드
  - 인스턴스 생성 시 `user_cache`는 None으로 할당되며 유효성 검사 통과 시 로그인 한 사용자 객체로 할당
  - 인스턴스의 유효성을 확인한 후 user를 제공하려는 구조



## Template에서 인증 데이터 

- request 에 user 정보가 들어있음.
  - DTL 에서 `{{ user }}`로 사용자 정보에 접근 가능
- settings.py의 `TEMPLATES`안에  `context_processors`
  - 템플릿이 렌더링 될 때 자동으로 호출 가능한 컨텍스트 데이터 목록
  - 작성된 프로세서는 RequestContext에서 사용 가능한 변수로
  - 여기에 auth 적혀있음.



## 로그아웃

- Session DELETE - 로그아웃

- `logout()`함수
  - HttpRequest 객체를 인자로, 반환 값 없음
  - 사용자가 로그인하지 않았어도 오류 발생 x
  - session data를 DB에서 삭제, 클라이언트 쿠키에서도 삭제
  - 이전 사용자의 세션 데이터에 액세스 방지





## 로그인 사용자 접근 제한

- 로그인하지 않은 경우 접근을 제한하는 방법

  1. `is_authenticated` 속성을 이용
     - User model의 속성, 모든 User 인스턴스에 True,
     - AnonymousUser에 대해서는 항상 False
     - `is_anonymous` 속성도 있음
     - 권한과 관련이 없으며, 유효한 세션을 가지고 있는지 확인하지 않음
  2. `@login_required` 데코레이터 이용
     - 사용자가 로그인되어 있지 않으면 `settings.LOGIN_URL`에 설정된 문자열 기반 절대 경로로 redirect
     - 로그인 되어있으면 정상적으로 view함수 실행
     - 인증 성공 시 "next" 쿼리 문자열 매개변수에 redirect 되어야하는 경로가 저장됨

- "next" 쿼리 문자열 매개변수

  - 주소를 keep해두는 것
  - 별도 처리하지 않으면 작동안함
  - `return redirect(request.GET.get('next') or '<app:url>')`

- 주의

  - `@login_required`와 `@require_POST` 동시하면 문제 발생

  - 비로그인 시 접근하면 login_required 에 의해 로그인 페이지로 이동하고,

    next 쿼리대로 주소 리다이렉트 GET요청을 보냄.

    이때 POST만 허용해뒀으므로 405 에러발생

  - 따라서 `@login_required`는 GET method 처리할 수 있는 view함수에서만 사용



## 회원가입

- DB에 사용자 CREATE - 회원가입

- `UserCreationForm`
  - 새로운 사용자 생성 ModelForm
  - username, password1, password2, 세 개 필드 가짐

## 회원탈퇴

- DB에 사용자 DELETE - 회원탈퇴
- request에 user 정보가 담겨져있으니 `request.user.delete()` 로 삭제. 

- 탈퇴 후 유저의 세션 데이터를 지워 로그아웃.



## 회원정보 수정

- 회원정보 수정은 비밀번호가 아닌 것만 수정, 비밀번호는 따로 수정

- `UserChangeForm`

  - 사용자 정보, 권한 변경을 위해 admin 인터페이스에서 사용하는 ModelForm

- `UserChangeForm` 문제점

  - 일반 사용자가 접근하면 안되는 필드까지 모두 수정 가능
  - 따라서 UserChangeForm을 상속받아 새로운 CustomUserChangeForm 서브 클래스 작성 후 접근 가능한 필드 조정
  - 매우 중요

  - ```python
    from django.contrib.auth.forms import UserChangeForm
    from django.contrib.auth import get_user_model
    
    
    class CustomUserChangeForm(UserChangeForm):
        
        class Meta:
            model = get_user_model()
            fields = ('email', 'first_name', 'last_name',)
    ```

- `get_user_model()`

  - 현재 프로젝트의 모든 사용자 모델 반환
  - django는 User 클래스 직접 참조 대신 `get_user_model()` 사용하여 참조해야한다고 강조, 권고!



## 비밀번호 변경

- `PasswordChangeForm`

  - 비밀번호 변경 Form
  - 이전 비밀번호 입력해서 비밀번호 변경
  - 이전 비밀번호 없이 비밀번호 설정하는 `SetPasswordForm` 상속받은 서브 클래스
  - 첫번째 인자가 user임. 슈퍼 클래스가 그래서.

- 비밀번호 변경시 세션 무효화 방지

  - 비밀번호 변경하면 기존 세션 사용자 인증 정보가 일치하지 않아 로그아웃됨.

  - `update_session_auth_hash(request, user)`를 이용

  - 새로운 password hash로 session 업데이트

    

