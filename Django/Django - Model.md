# Django - Model

## Model

- 단일한 데이터에 대한 정보
- 저장된 DB의 구조
- 일반적으로 각각의 model은 하나의 DB table에 매핑
- 웹 애플리케이션의 데이터를 관리

<br/>

## Database

### Database 구조

- **스키마, shema**

  - 자료의 구조, 표현방법, 관계 등을 정의한 구조
  - 데이터베이스 전반적인 명세

- **테이블, table**

  - 컬럼 : 필드 또는 속성, 각 열에는 데이터 속성이 지정
  - 행 : 레코드 또는 튜플, 테이블의 데이터가 행에 저장

  - 열과 행로 조직된 데이터 요소들의 집합

- **기본키, Primary Key**

  - 각 행의 고유값, 반드시 설정해야함
  - 데이터베이스 관리 및 관계 설정 시 주요하게 활용

<br/>

## ORM

- ORM, Object-Relational-Mapping
- **객체 지향** 프로그래밍 언어를 사용해서, 서로 호환되지 않는 시스템 간에(cf, Django-SQL) 데이터를 **변환**하는 프로그래밍 기술
- OOP 프로그래밍에서 RDBMS을 연동할 때, DB와 OOP 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법
- Django에서는 내장 Django ORM



### ORM의 장단점

- 장점
  - SQL 몰라도 DB 조작 가능
  - 객체 지향적 접근으로 높은 생산성
- 단점
  - 완전한 서비스 구현 어려움
- 하지만 현대 웹 프레임워크의 요점은 **개발 속도와 생산성**의 증가임.

<br/>

## models.py

- ```python
  # articles/models.py
  
  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

- DB 컬럼과 어떤 타입으로 정의할건지에 대해 `django.db` 모듈의 `models` 상속

  - 각 모델은 `django.db.models.Model` 클래스의 서브 클래스로

- `title` 과 `content` 는 모델의 필드

  - 각 필드는 클래스 속성으로 지정. 각 속성은 DB의 컬럼에 매칭

- `CharField(max_length=None, **options)`

  - 길이의 제한이 있는 문자열

  - max_length는 유효성 검사에서 활용

  - `choices` 옵션을 통해서 form에서 선택하는 드롭박스 만들 수 있음.

    `instance.get_<field>_display` 로 접근 가능

- `TextField(**option)`

  - 글자의 수가 많을 때 사용
  - max_length 옵션 작성 시 textarea 위젯에는 반영되지만 모델과 DB 수준에는 적용되지 않음

- DateField option

  - `auto_now_add`
    - 최초 생성 일자
    - django ORM이 최초 insert 시에만 현재 날짜와 시간으로 갱신
  - `auto_now`
    - 최종 수정 일자
    - django ORM이 저장할 때마다 현재 날짜와 시간으로 갱신

<br/>

## Migrations

- Migrate : 이주하다. 거주지를 옮기다.

- django가 model에 생긴 변화를 DB에 반영하는 방법
- Migration 실행 및 DB 스키마를 다루기 위한 명령어
  - `makemigrations`
    - **model 변경점에 기반한 새로운 마이그레이션**을 만들 때 사용
    - migrations 폴더 안에 새로운 .py 파일을 만들어줌
    - 이 새로운 .py 파일이 ORM에 의해 SQL로 변환되어 DB로 전달
  - `migrate`
    - 마이그레이션을 **실제 DB에 반영**할 때 사용
    - 모델에서의 변경 사항들과 DB의 스키마가 동기화
    - django_migrations table에 migrate 기록이 저장되어있음
  - `sqlmigrate`
    - 마이그레이션에 대한 SQL 구문을 볼 때 사용
    - 마이그레이션이 SQL 문을 어떻게 해석될지 미리 볼 수 있음
    - `$ python manage.py sqlmigrate <app_name> <number>`
  - `showmigrations`
    - DB에 반영된 마이그레이션 확인할 때 사용
- **migration 3단계**
  1. models.py
     - model 변경사항 발생 시
  2. `$ python manage.py makemigrations`
     - migrations 파일 생성
  3. `$ python manage.py migrate`
     - DB에 반영

<br/>

## Database API

- DB를 조작하기 위한 도구

### DB API 구문

- Making Queries
- `< Class name >.< Manager >.< QuerySet API >`
  - ex) `Article.objects.all()`
- Manger
  - django 모델에 DB query 작업이 제공되는 인터페이스
  - 기본적으로 모든 django 모델 클래스에 objects라는 Manager 추가
- QuerySet
  - DB로부터 전달받은 객체 목록
  - DB로부터 조회, 필터, 정렬 등 수행할 수 있음

- [https://docs.djangoproject.com/en/3.2/ref/models/querysets/](https://docs.djangoproject.com/en/3.2/ref/models/querysets/)

<br/>

## CRUD

- 소프트웨어의 기본적인 데이터 처리기능

- Create 생성 
- Read 읽기
- Update 갱신
- Delete 삭제

### Create

- 인스턴스 생성 후 인스턴스 변수 설정
- 초기값과 함께 인스턴스 생성
- QuerySet API - `create()` 사용
- `save()` : 객체를 DB에 저장
  - save() 전까지는 객체의 ID값 알 수 없음
  - save() 하기 전까지는 DB에 영향을 미치지 않음

### READ

- QuerySet API method를 사용해 다양한 조회를 하는 것이 중요
- QuerySet API method는 크게 2가지
  - querysets을 리턴하는 것
  - querysets을 리턴하지 않는 것
- `all()` 
  - 현재 QuerySet의 복사본 반환
- `get()`
  - 주어진 lookup 매개변수와 **일치**하는 객체를 반환
  - 없으면 DoesNotExiset 예외 발생, 둘 이상이면 MultipleObjectReturned 예외 발생
  - 따라서 pk 등 고유성이 보장되는 조회에서 사용
- `filter()`
  - 주어진 lookup 매개변수와 일치하는 객체를 포함하는 새 QuerySet 반환

### Update

- READ를 통해 갱신하고 싶은 데이터에 접근 후 수정



### Delete

- READ를 통해 갱신하고 싶은 데이터에 접근 후 삭제
- `<instance>.delete()` 로 삭제

- `.delete()` 
  - 모든 행에 대해 SQL 삭제 쿼리 수행
  - 삭제된 객체 수와 객체 유형당 삭제 수가 포함된 딕셔너리 반환

<br/>

## HTTP method

### GET

- 특정 리소스를 가져오도록 요청할 때 사용
- 반드시 데이터를 가져올 때만 사용
- DB에 변화를 주지 않음
- CRUD 중 R

### POST

- 서버로 데이터를 전송할 때 사용
- 리소스 생성/변경을 위해 데이터를 HTTP body에 담아 전송
- 서버에 변경사항
- CRUD 중 C/U/D

### CSRF (Cross-site request forgery)

- 사이트 간 요청 위조
- 웹 애플리케이션 취약점 중 하나로 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 한다거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법
- django는 CSRF에 대항하여 middleware와 template tag를 제공

### CSRF 공격 방어

- Security Token 사용 방식
  - 사용자의 데이터에 임의의 난수값을 부여해, 매 요청마다 해당 난수 값을 포함시켜 전송하도록 함
  - 이후 서버에 요청을 받을 때마다 전달된 token값이 유효한지 검증
- DB를 변경하는 POST, PATCH, DELETE Method 등에 적용

