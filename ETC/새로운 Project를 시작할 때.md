# 새로운 Project를 시작할 때

## 1. 환경 구축

- 해당 프로젝트를 위한 환경을 구축해야한다.
- 프로젝트를 위한 가상환경을 만든다.
  - 파이썬의 경우 `$ python -m venv venv`
  - 가상 환경 실행은 `$ source venv/Script/activate` (윈도우)
- `git` 저장소를 새로 만든다.  `$ git init`
- `git`이 관리하지 않아야할 목록을 `.gitignore`에 작성한다.

## 2. 어떤 framework

- 프로젝트를 위한 어떤 framework를 사용할 것인지 결정됐다면 가상환경에 설치한다.

- `pip install <package>` 

  

## 3. 프로젝트 작업 환경 기록

- 원격 저장소에 올리거나 다른 작업 환경 또는 협업 개발자들을 위해 작업 환경을 기록해야한다.

- `pip freeze > requirements.txt` 로 현재 가상환경에 설치된 파이썬 패키지를 기록한다.