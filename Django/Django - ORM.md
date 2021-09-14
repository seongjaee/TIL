# Django ORM

- Django ORM lazy loading
  - 정말로 사용하지 않으면 SQL 쿼리 호출하지 않음



## CRUD

### CREATE

- ```python
  <Model>.objects.create(
  	col1=value1,
  	col2=value2,
      ...
  )
  ```

- 

### READ

- 모든 레코드 조회
  - `<Model>.objects.all()`
- 특정 레코드 조회
  - `<Model>.objects.get(pk=1)`

#### UPDATE

- 특정 레코드 수정

  - ```python
    <instance> = <Model>.objects.get(pk=1)
    <instance>.<col> = <value>
    <instance>.save()
    ```

#### DELETE

- 특정 레코드 삭제
- `<Model>.objects.get(pk=1).delete()`



## more+

- `count()`
  - `<Model>.objects.count()`
- 특정 조건으로 조회
  - `<Model>.objects.filter(age=30).values('name')`
  - 크기 비교
    - `__gt`, `__lt`, `__gte`, `__lte`
  - 조건 AND
    - `.filter(age=30, name='홍길동')`
  - 조건 OR
    - `.filter(Q(age=30) | Q(name='홍길동'))`
  - SQL LIKE
    - `__startswith`, `__endswith`, `__contains`
    - `.filter(name__startswith='홍')`
- 정렬
  - `<Model>.objects.order_by(<col>)`
- Django Aggregation
  - `User.objects.aggegate(Avg('age'))`

- Django Annotate
  - 주석 컬럼을 하나 추가. 원본 테이블이 변경되지 않음.