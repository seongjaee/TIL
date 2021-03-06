# 가상환경

> 독립된 개발 환경

- 파이썬 표준 라이브러리가 아닌 외부 패키지나 모듈은 모두 pip로 설치해야함
- 여러 프로젝트를 진행 중이면 버전이 상이할 가능성이 있어서 오류가 날 가능성
- 이럴 때 가상환경으로 프로젝트별 독립적인 패키지 관리가 가능



## venv

- 가상환경을 만들고 관리하는데 사용되는 모듈
- 특정 디렉토리에 가상 환경을 만들고, 독립적인 파이썬 패키지 집합을 만들 수 있음
  - 특정 폴데어 가상 환경이 있음
  - 실행 환경에서 가상환경을 활성화
  - 해당 폴더에 있는 패키지를 관리/사용



- 가상환경 생성
  - `$ python -m venv <folder>`

- 가상환경 활성화/비활성화

  - 윈도우 기준  bash `$ source <folder>/Scripts/activate`
  - cmd `C:> <folder>\Scripts\activate.bat`

  - 비활성화 `$ deactivate`



## 패키지 관리

- `$ pip freeze`
- 설치된 패키지의 목록을 `<package>==<version>` 형식으로 출력
- 출력된 해당 목록을 requirements.txt 로 만들어 관리하는 게 좋음
  - `$ pip freeze > requirements.txt`

- `$ pip install -r requirements.txt`로 목록의 패키지를 모두 설치할 수 있음.