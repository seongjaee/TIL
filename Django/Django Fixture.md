# Django Fixture

- 협업 간에 DB가 공유되지 않아 불편할 수 있다. 이를 해결하기 위해 고정적으로 필요한 데이터를 미리 만들어둔다.
- Django에서는 `fixtures` 폴더가 이런 데이터를 저장할 경로 기본값으로 설정되어있다.
- loaddata : fixtures의 데이터를 DB에 가져오기
  - `$ python manage.py loaddata <filename> `
- dumpdata : DB에 있는 데이터를 fixtures 폴더에 저장
  - `$ python manage.py dumpdata --indent 4 <app_name>[.ModelName] > <filename>.json`
  - (참고) 터미널에서 `>`는  `>` 앞에 출력될 내용을  `>`뒤에 작성한 파일에 저장