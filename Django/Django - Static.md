# Django - Static

## Static files

- 정적 파일
- 응답 시 파일을 요청한 그대로 보여주면 되는 파일

- 일반적으로 이미지, 자바 스크립트, CSS 같은 미리 준비된 추가 파일을 제공

  

1. django.contrib.staticfiles 가 INSTALLED_APPS에 포함되어있는 지 확인

2. settings.py에서 STATIC_URL을 정의

3. 템플릿에서 static 템플릿 태그를 사용하여 지정된 상대경로에 대한 URL 빌드

   ```html
   {% load static %}
   
   <img src="{% static 'my_app/example.jpg' %}" alt=...>
   ```

   

4. 앱의 static 폴더에 정적 파일을 저장

   `my_app/static/my_app/example.jpg`



- **Django template tag**
  - `load`
    - 사용자 정의 템플릿 태그 세트를 로드
    - 로드하는 라이브러리, 패키지에 등록된 모든 태그와 필터를 로드
  - `static`
    - STATIC_ROOT에 저장된 정적 파일에 연결



- **STATIC_ROOT**
  - collectstatic이 배포를 위해 **정적 파일을 수집**하는 디렉토리의 절대 경로
  - django 프로젝트에서 사용하는 **모든 정적 파일을 한 곳**에 모아 넣는 경로
  - 개발 과정에서 setting.py의 DEBUG 값이 True면 작용되지 않음
  - 배포 환경에서 django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위함
- **STATIC_URL**
  - STATIC_ROOT에 있는 정적 파일을 참조할 때 사용할 URL
  - 개발단계에서는 app/static 경로와 STATICFILES_DIRS에 정의된 추가 경로 탐색
  - 실제 파일이 아니라, URL로만 존재
- **STATICFILES_DIRS**
  - 기본 경로 외에 추가적인 정적 파일 경로 목록 정의 리스트





## 이미지 업로드 기본설정

- **Media file**
  - 사용자가 웹에서 업로드하는 정적 파일
  
- **ImageField**
  - 이미지 업로드에 사용하는 모델 필드
  - FileField를 상속받음. 객체가 유효한 이미지인지 검사함.
  - 최대 길이가 100자인 문자열로 DB에 생성.
  - DB에는 파일 경로만 저장.
  - 사용하려면 Pillow 라이브러리가 필요

- **FileField**
  - 파일 업로드에 사용하는 모델 필드
  - 2개의 선택인자
    - upload_to : 업로드 디렉토리와 파일 이름 설정
    - storage
  - `upload_to`
    - 문자열 경로 지정 방식
      - upload_to='uploads/' => MEDIA_ROOT/uploads/에 업로드
      - upload_to='uploads/%Y/%m/%d/' => MEDIA_ROOT/uploads/2021/01/01에 업로드

- **MEDIA_ROOT**
  - 사용자가 업로드한 미디어 파일들을 보관할 디렉토리의 절대경로
  - DB에 저장되는 건 파일의 경로

- **MEDIA_URL**
  - MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL
  - 업로드된 파일의 URL을 만들어 준다.
  
- [개발 단계에서 사용자가 업로드한 파일 제공하기](https://docs.djangoproject.com/ko/3.2/howto/static-files/#serving-files-uploaded-by-a-user-during-development)

  ```python
  from django.conf import settings
  from django.conf.urls.static import static
  
  urlpatterns = [
     ...
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

  



## 이미지 업로드 CREATE

- Model field option - "blank"
  - True면 필드를 비워 둘 수 있음
  - 유효성 검사에서 사용됨.
- Model field option - "null"
  - True면 빈 값을 DB에 NULL로 저장
  - 문자열 기반 필드에서는 사용하지 않아야함.
- blank vs null
  - blank : Validation-related
  - null : DB-related
  - form에 빈값을 허용하려면 blank=True

- form enctype (인코딩)속성 지정
  - `multipart/form-data`
    - 파일/이미지 업로드 시에 반드시 사용, 전송 데이터의 형식 지정
    - `<input type="file">`을 사용할 때 사용
- `<input type="file">` 내에 `accept` 속성 : 파일 선택을 눌렀을 때 허용할 파일 유형 지정. 고유 파일 유형 지정자.



- 이미지 파일은 `request.POST`에 없음, `request.FILES`에 담겨있음

- 같은 이름의 이미지가 들어오면 django가 알아서 이미지 이름 뒤에 난수를 붙여줌.

  



## 이미지 READ

- 업로드된 파일의 경로는 django가 제공하는 `url` 속성을 통해 얻을 수 있음

  - `{{ field.image.url }}` : 이미지 파일 경로

  - `{{ field.image }}` : 이미지 파일 이름

- 서버에 요청하기 위한 url을 settings.py 에 작성 후 그걸 urlpatterns 에 추가하는 방식





## 이미지 UPDATE

- 이미지는 바이너리 데이터이기 때문에 일부 수정이 불가능
- 따라서 새로운 사진으로 덮어 씌우는 방식



### 이미지 크기 변경

- 실제 원본 이미지를 그대로 업로드하는 것은 서버에 부담
- 이미지가 업로드 될 때 resizing
- [django-imagekit](https://github.com/matthewwithanm/django-imagekit) 라이브러리 활용

- 원래 이미지를 변경해서 저장하고자 한다면 mageSpecField로 저장

- `imagekit.processor`
  - Thumbnail : 썸네일. 작은 사진으로 바꾼다.
  - ResizeToFill : 원하는 사이즈와 비율로 자른다.
  - ResizeToFit : 원본 비율로 확대/축소해서 원하는 사이즈에 맞추려고 한다.

