# Model relationship 2

## M:N 관계

## 1:N 모델의 한계

- 서점의 예시
  - "책" 테이블에는 책의 정보가 담겨있다.
  - "서점" 테이블에는 서점의 정보가 담겨있다.
  - 어떤 책이 어떤 서점에 재고로 있는지 데이터를 저장하고 싶다면?
  - 이상해진다. 1:N 관계에서는 한쪽 테이블에 데이터의 중복이 많이 발생한다. "책" 테이블에 서점에 대한 정보가 포함된다.
  - 새로운 책이 서점에 들어온다면?
  - ACID : (원자성, 일관성, 고립성, 지속성) - DB 트랜잭션 안전 수행을 보장하기 위한 성질
- 이를 위한 중개 모델

## 중개 모델

- 두 테이블과 각각 1:N 관계를 맺는 중개 모델을 만들면 해결할 수 있다!
- 중개 모델은 두 테이블의 기본키값을 외래키로 갖는다.



## ManyToManyField

- 다대다 (M:N) 관계 설정 시 모델 필드
- 하나의 필수 위치인자(모델 클래스) 필요
- 두 모델 중 한쪽에만 만들어주면 됨
- Book 모델 클래스에 `stores = models.ManyToManyField(Store)`
- 위의 경우 중개모델의 테이블 이름은 `<app_name>_book_stores`
- `book1.stores.<query>`로 사용가능. 필드이름이 매니저이름으로 됨.
- 반대의 경우는 `store1.book_set.<query>` 역참조이므로 _set 매니저 사용.
- 이 역시 `related_name` 으로 역참조 매니저 이름 설정 가능
  - target model이 source model을 참조할 때 사용할 manager 이름 설정
- query는 `add`, `remove` 등이 있음
- `add` 
  - 지정된 객체를 관련 객체 집합에 추가
  - 이미 존재하는 관계의 경우 복제되지 않음
  - 모델 인스턴스, pk 값 인자 허용
- `remove`
  - 관련 객체 집합에서 지정된 객체 제거
  - 내부적으로 QuerySet.delete()로 관계가 삭제됨
  - 모델 인스턴스, pk 값 인자 허용



### 중개 모델을 직접 작성하려는 경우

- 중개 모델을 직접 작성 후, `through` 옵션을 사용해 수동으로 중개 테이블을 지정.

- 중개 테이블에 추가 데이터를 사용하려는 경우 사용 가능

  extra data with a many-to-many relationship

### ManyToManyField Arguments

- `related_name`
  - 역참조 시 사용할 manager 이름 설정

- `through`
  - 중개 모델을 직접 작성 후, `through` 옵션을 사용해 수동으로 중개 테이블을 지정.
  - `through_defaults`
    - 중개 테이블에 관계를 추가할 때, 추가 데이터를 저장하기 위해 사용
    - `through_defaults={<field>:<value>}`

- `symmetrical`

  - ManyToManyField 가 동일한 모델을 가리키는 정의에서만 사용

    `models.ManyToManyField('self', symmetrial=False)`

  - True가 기본값으로, 이 경우 django는 _set 매니저를 추가하지 않음.

  - source 모델 인스턴스가 target 모델 인스턴스를 참조하면, 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 참조.

  - 즉, A 가 B를 팔로우하면 자동으로 B도 A를 팔로우

- 



