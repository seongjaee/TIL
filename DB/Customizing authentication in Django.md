# Customizing authentication in Django

## Substitution a custom User model

### User 모델 대체하기

- 일부 프로젝트에서는 Django의 내장 User 모델의 제공 인증 요구사항이 적절하지 않을 수 있음
  - email을 식별 토큰으로 사용하는 게 더 적합한 사이트

- Django는 User를 참조하는데 사용하는 **AUTH_USER_MODEL** 값을 제공하여, default user model을 재정의(override) 할 수 있도록 함
- Django는 새 프로젝트를 시작하는 경우 기본 사용자 모델이 충분하더라도, **커스텀 유저 모델을 설정하는 것을 강력하게 권장**
  - 단, 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야함



### AUTH_USER_MODEL

- User를 나타내는데 사용하는 모델
- 프로젝트 진행 중에는 변경 불가능
- 프로젝트 시작 시 설정. 참조하는 모델은 첫번째 마이그레이션에서 사용할 수 있어야함.
- 기본 값: `auth.User` (auth 앱의 User 모델)
- 프로젝트 중간에 변경하는건 모델 관계에 영향을 미쳐 어려움.

- 일단 대체해놓고 보자. 나중에 수정할 수 있도록.

### Custom User 모델 정의하기

- AbstractUser를 상속받아 새로운 User 모델 작성

```python
# accounts.models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

```python
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```





## Custom user & Built-in auth forms

- Custom user모델을 사용하면 기존의 회원가입과 회원수정 form을 사용할 수 없음.  `UserCreationForm` 과 `UserChangeForm`은 Meta의 model이 `auth.User`이기 때문.

- 따라서 CustomUserCreationForm과 CustomUserChangeForm을 만들어서 사용해야함.

  Meta  클래스에 `model = get_user_model()`로 현재 활성화된 user 모델을 사용.

```python
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)
```

### get_user_model()

- 현재 프로젝트에서 활성화된 사용자 모델 반환
  - User모델 커스터마이징 했다면 Custom User 모델 반환
- Django는 User 클래스 직접 참조 대신 get_user_model()로 참조해야한다고 강조

