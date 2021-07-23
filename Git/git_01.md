# Git_01



## 3개의 공간

- 작업 공간
  - 작업(수정, 삭제, 생성 등)을 하는 공간
  - `$ git add <filename>`로 스테이지에 기록을 올림

- 스테이지
  - 기록될 파일들의 변경사항들이 올려지는 공간
  - `git commit`으로 저장소에 기록을 올림

- 저장소(Repository)
  - 스테이지 위의 변경사항들을 저장소에 저장





## Local Repo

내 컴퓨터 안에 있는 저장소

`git init`으로 새로운 Repository를 만들 수 있다.



### Add

- `$ git add <filename>`으로 스테이지에 올림
- `$ git add .` 으로 현재 디렉토리 내 모든 파일을 올릴 수도 있음.



### Commit

모든 Commit에는 작성자의 서명이 새겨짐.

- `$ git config --global user.name`
- `$ git config --global user.email`

로 서명을 할 수 있음



`$ git commit -m "<Message>"` 로 커밋마다 수정 사항에 대한 메시지를 남김.

좋은 커밋 메시지를 작성하기 위해 노력해야함



### 모니터링

`git status` 로 작업공간, 스테이지, 저장소의 상태를 확인 가능

`git log`로 저장소 내부에 `commit`에 대한 기록을 확인 가능



## Remote Repo

**원격 저장소**

로컬 저장소에 문제가 생길 경우를 대비해 원격 저장소에 git을 저장해둠

1. Local repo 생성
2. Remote repo 생성
3. Local repo와 Remote repo 연결
4. 커밋 업로드

과정으로 이용



### Remote repo 생성

github, gitlab 등의 사이트를 이용



### Remote repo와 Local repo 연결

`$ git remote add <name> <URL>`



### Remote repo로 업로드

Local -> Remote

`$ git push <name> <branch>`



### Local repo로 다운로드

Remote -> Local

`$ git pull <name> <branch>`



`$ git clone <URL>` 으로 새로운 local repo로 복제 가능

