# 모듈 Module

> 파이썬의 모듈 : 파일 단위의 코드 재사용

- 모듈 : 특정 **기능**을 `.py` 파일 단위로 작성한 것
- 패키지 : 특정 기능과 관련된 여러 **모듈들의 집합**

- 라이브러리 : 모듈과 패키지의 집합

## 파이썬 표준 라이브러리 PSL

[Python Standard Library Docs](https://docs.python.org/ko/3/library/)

- 파이썬에 기본적으로 설치된 모듈과 내장 함수



## 파이썬 패키지 관리자 pip

- PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템

- 패키지 설치 명령어
  - `$ pip install <package>`
  - `$ pip install <package>==<version>`
  - `$ pip install <package>>=<version>`

- 패키지 삭제 명령어

  - `$ pip uninstall <package>`

- 패키지 목록 및 정보 명령어

  - `$ pip list`
  - `$ pip show <package>`

- 패키지 관리

  - `$ pip freeze`
  - 설치된 패키지의 목록을 `<package>==<version>` 형식으로 출력
  - 출력된 해당 목록을 requirements.txt 로 만들어 관리하는 게 좋음
    - `$ pip freeze > requirements.txt`

  - `$ pip install -r requirements.txt`로 목록의 패키지를 모두 설치할 수 있음.

## 모듈/패키지 활용

### 패키지 Package

- 패키지는 점(`.`)으로 구분된 모듈 이름을 써서(`package.module`) 모듈을 구조화하는 방법

- 모든 폴더에는 `__init__.py`를 만들어 패키지로 인식

  - Python 3.3 이후부터는 없어도 되기는 하는데, 하위 파이썬이나 프레임 워크를 고려해 넣는게 좋음

- 구조

  my_package/

  ​		`__init__.py`

  ​		package_1/

  ​				`__init__.py`

  ​				`tools.py`

  ​		package_2/

  ​				`__init__.py`

  ​				`tools.py`



- 모듈 사용법

  - 모듈 임포트
    - `import module`
    - `from import var, function, Class`
    - `from module import *`
    - `from package import module`
    - `from package.module import var, function, Class`

  - `dir(<module>)` 로 모듈 내 요소를 확인 할 수 있음.

