# Database

> SQL 기본, 찍먹

- 데이터베이스(DB)

  - 체계화된 데이터의 모임
  - 파일의 조직적 통합으로 중복을 없애고 구조화해서 기억시켜놓은 자료 집합

- DB 장점

  - 데이터 중복 최소화
  - 무결성
  - 일관성
  - 독립성
  - 표준화
  - 보안

- RDB(관계형 데이터베이스)

  - Relational Database

  - 키와 값들의 간단한 관계를 표 형태로 정리한 데이터베이스

- 용어 정리

  - 스키마(schema) : 자료 구조, 표현방법, 관계 등 전반적인 **명세**
    - 컬럼명, 컬럼 데이터타입
  - 테이블(table) : 열과 행의 모델로 조직된 데이터 요소 집합. 표.
    - 스키마대로 채워진 데이터들

  - 열(Column) : 세로. 각 열에는 고유한 데이터 형식이 지정됨.
  - 행(Row) : 실제 데이터가 저장됨. 레코드.
  - 기본키(Primary Key) :  각 행의 고유 값. 반드시 설정.

- RDBMS

  - 관계형 데이터 관리 시스템, Reltional Database Management System
  - MySQL, SQLite, PostgreSQL, ORACLE, MS SQL 등


## SQL

- SQL (Structured Query Language)

  - RDMBS의 데이터 관리를 위한 프로그래밍 언어
  - 데이터베이스 스키마 생성 및 수정(구조 관리)
  - 자료의 검색 및 관리(CRUD)
  - 데이터베이스 객체 접근 조정 관리

- SQL 분류

  - DDL - 데이터 정의 언어
    - CREATE
    - DROP
    - ALTER
  - DML - 데이터 조작 언어
    - INSERT
    - SELECT
    - UPDATE
    - DELETE
  - DCL - 데이터 제어 언어
    - GRANT
    - REVOKE
    - COMMIT
    - ROLLBACK


- SQLite
  - 파일 형식으로 응용 프로그램에 넣어서 사용하는 가벼운 데이터베이스
  - 구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스
  - 로컬에서 간단한 DB 구성을 할 수 있음.
  - 오픈 소스 프로젝트라 자유로운 사용

### 테이블 생성 및 삭제

- CREATE TABLE
- DROP TABLE

### CRUD

#### CREATE

- `INSERT INTO <TABLE> (<col1>, <col2> ,...) VALUES (value1, value2, ...);`



#### READ

- SELECT
- SELECT clauses
  - LIMIT
    - 쿼리에서 반환되는 행 수 제한
    - OFFSET : 어디서부터 가져올지
  - WHERE

    - 특정 검색 조건 지정
  - SELECT DISTINCT

    - 중복없이 조회

#### DELETE

- DELETE
  - `DELETE FROM <TABLE> WHERE condition;`

#### UPDATE

- UPDATE
  - `UPDATE <TABLE> SET col1=value1, col2=value2, ... WHERE condition;`
  - SET clause로 새로운 값 설정



### SQLite Aggregate Functions

- Aggregate : 골재, 집합, 집합체
- COUNT : 그룹의 항목 수
- AVG : 그룹의 평균
- MAX : 그룹의 최댓값
- MIN : 그룹의 최솟값
- SUM : 그룹의 총합

- LIKE
  - 패턴 일치로 데이터 조회
  - SQLite의 와일드카드
    - % : 0개 이상의 문자 - 여기에 문자열이 있을수도 없을수도
    - _ : 임의의 단일 문자 - 여기에 반드시 한 개의 문자가 있다.

- ORDER BY
  - 정렬
  - ASC : 오름차순 default
  - DESC : 내림차순
  - 정렬 기준이 여러개라면 먼저 쓴 컬럼이 우선

- 주의 순서 중요

  - WHERE < GROUP BY < ORDER BY < LIMIT

- GROUP BY

  - 행 집합에서 요약 행 집합을 만듦
  - 지정된 기준에 따라 행 집합을 그룹으로 엮어 aggregate를 적용
  - WHERE 절 뒤에 작성

  - AS를 활용해 컬럼명을 바꿔 조회 가능