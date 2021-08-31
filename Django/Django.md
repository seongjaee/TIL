# Django

## Web Framework

- Framework
  - 정해진 틀 안에서 일을 하도록 함.
  - 재사용할 수 있는 수많은 코드를 통합. 개발자가 표준 코드를 다시 작성하지 않아도 사용할 수 있도록 도움
- Web Framework
  - 웹 페이지 개발을 쉽고 빠르게 도와줌.
- Django 
  - Python Web framework. 무료 오픈 소스
  - Spotify,  Instagram, Dropbox, Delivery Hero 등이 Django로 만들어짐
  - 빠르게 개발할 수 있다는 장점. (애자일 방법론)
- Static web page (정적 웹 페이지)
  - 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지
  - 서버의 추가적인 처리 과정 없이 클라이언트에게 응답
  - 모든 상황에서 모든 사용자에게 동일한 정보 표시
  - 일반적으로 HTML, CSS, JavaScript로 작성됨
- Dynamic web page (동적 웹 페이지)
  - 서버가 추가적인 처리 과정 이후 클라이언트에게 응답을 보냄
  - 방문자와 상호작용하기 때문에 페이지 내용이 그때그때 다름
  - 서버 사이드 프로그래밍 언어(python, java, c++)가 사용됨, 파일 처리와 DB와의 상호작용
- Framwork Architecture
  - MVC Design Pattern (model-view-controller)
  - 사용자 인터페이스로부터 프로그램 로직을 분리하여 애플리케이션의 시각적 요소나 이면에서 실행되는 부분을 서로 영향 없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있음
  - Django는 MTV Pattern이라고 함
- MTV Pattern
  - Model --DB
    - 응용프로그램 데이터 구조 정의 데이터베이스 기록 관리
  - Template --HTML
    - 파일의 구조나 레이아웃 정의
    - 실제 내용 보여주는데 사용
  - View --중간관리자
    - HTTP 요청 수신, HTTP 응답 반환
    - Model을 통해 요충을 충족시키는데 필요한 데이터 접근
    - template에게 응답 서식 설정 맡김



## Django 시작하기

### Project 만들기

- `$ django-admin startproject <project_name>` 으로 프로젝트 생성

- 프로젝트 생성 시 파일 경로들

  ```
  <project>   -> 프로젝트 폴더
  	|
  	|- manage.py     -> 커맨드라인 유틸리티
  	|
  	|- <project>     -> master app
  		|
  		|- __init__.py  -> 패키지로 다루도록 함
  		|- asgi.py      -> 비동기식 웹 서버와 연결 도움
  		|- wsgi.py      -> 웹서버와 연결 도움
  		|- settings.py  -> 애플리케이션 설정
  		|- urls.py      -> 사이트의 url와 views 연결
  ```

- 프로젝트 폴더에서 `$ python manage.py runserver` 로 서버 열기

- ```python
  # <project>.urls.py
  
  urlpatterns = [
      path('admin/', admin.site.urls),
  ]
  
  # url 경로에 admin이 붙으면 admin.site.urls 함수가 실행됨
  ```

- `views.py`를 만들어 모듈화

  ```python
  # <project>.views.py
  
  from django.http.response import HttpResponse
  
  def hello(request):
      html = '<h1>Hello!</h1>'
      return HttpResponse(html)
  ```

  ```python
  # <project>.urls.py
  
  from django.contrib import admin
  from django.urls import path
  
  from . import views
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('hello/', views.hello)
  ]
  ```

- URL 요청 -> urls.py에서 정해진 (view)함수 호출 -> views.py에서 함수 실행 -> templates에서 html 불러옴



### Application 만들기

- master_app은 총괄적인 일 담당.
- 역할별 app들을 만들어서 동작하도록 함.

```python
PJT 
	|-master app
    |- app A	-> 각 app들은 독립적이어야함
    |- app B
    |- app C
    |- app D
```

- `$ python manage.py startapp <app_name> `로 app 생성

- app 생성 시 디렉토리

  ```
  <app_name>   -> 프로젝트 폴더
  	|
  	|- __init__.py
  	|- admin.py      -> 관리자용 페이지 설정
  	|- apps.py       -> 앱의 정보
  	|- models.py     -> 앱에서 사용하는 Model 정의
  	|- tests.py      -> 프로젝트 테스트 코드 작성
  	|- views.py      -> view 함수 정의
  	|
  	|- migrations
  		|
  		|- __init__.py
  ```

- Project
  - Application의 집합
- Application
  - 실제 요청을 처리하는 역할
  - 하나의 역할 및 기능 단위로 작성 
- 새로운 app 생성 후 settings.py 의 INSTALLED_APPS에 추가해야함
  - 생성 전에 작성하면 안됨!

## 요청과 응답

- 서버는 요청을 url로 받아 html로 응답함

- urls.py

  - ```python
    from django.urls import path, includes
    
    urlpatterns = [
        path('index/', views.index)
    ]
    ```

  - HTTP 요청을 알맞은 view로 전달

- views.py

  - ```python
    from django.shortcuts import render
    
    def index(request):
        return render(request, 'index.html')
    ```

  - 

  - HTTP 요청을 수신해서 응답을 반환하는 함수 작성

  - Model을 통해 요청에 맞는 필요 데이터에 접근

  - Template에게 응답 서식을 맡김

- Templates

  - 실제 대용을 보여주는 파일, HTML



## Template

- DTL, Django Template Language

  - Variable  `{{ variable }}`
    - `.`으로 변수 속성에 접근
    - `render()`의 세번째 인자에 {'key': value}의 딕셔너리 형태로 넘겨지면, key가 template에서 사용가능한 변수명
  - Filters `{{ variable|filter }}`
    - `upper` : 대문자로
    - `lenght` : 문자열 길이
  - Tags `{% tag %}`
    - 반복 또는 논리
  - Comments `{# #}`

- Django 서버를 시작하면 모든 INSTALLED_APPS의 app에 대해, 순회하면서 templates 폴더를 병합함.

  서로 다른 app의 같은 이름의 template이 있으면 하나가 무시됨(먼저 있는 app이 우선)
  - 해결방법
    - `templates/<app_name>/<template_name>.html`으로 templates 폴더 안에 저장할 때 app_name 폴더 안에 template을 넣어서 구분되도록 함.

- 템플릿 상속
  - 템플릿을 재사용하기 위함
  - 사이트의 공통 요소를 포함하는 기본 베이스 템플릿을 만들고, 하위 템플릿이 override하도록 함.
  - `{% extends '<base>.html' %}` : 하위 템플릿의 최상단에 적는다.
  - `{% block content %} {% endblock %}` : 하위 템플릿이 override할 수 있는 블록.
- Django template system
  - "표현과 로직을 분리"
  - "중복을 배제"





- SSR : Server Side Rendering

- Vue, React : CSR Client Side Rendering

- variable routing : 패턴 정의

