# Git basic



## What

분산 버전 관리 시스템

코드의 history를 관리하는 도구



## Why

버전 관리의 필요성

혹시 과거의 버전(기록)이 필요할 수도 있다.

버전 간의 차이를 알기 쉽게 저장함. 수정 이유도 기록.

버전 간의 차이,  변경사항만을 기록해 저장용량을 줄인다.



## How

### git 기본 명령어

`$ git init` : git 로컬 저장소 생성

`$ git add .` :  촬영 준비

`$ git commit -m "<Message>"` :  촬영~

`$ git log` :  log 확인

`$ git push origin master` : 푸시

`$ git remote add origin <URL>  ` : 리모트 저장소와 연결

`$ git status` : git 현재 상태 확인



### 주의 사항

1. Home 폴더에서 init 해선 안됨.
2. repo 안에 또 repo를 만들면 안됨.(이미 `git init` 한 폴더 안에서 또 `git init` 해선 안됨)
