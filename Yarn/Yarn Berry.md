# Yarn Berry

> https://toss.tech/article/node-modules-and-yarn-berry

## 개요

> https://github.com/yarnpkg/berry

- Node.js를 위한 패키지 관리 시스템
- 2020년 1월 25일 정식 버전 출시

## Plug 'n' Play

> https://yarnpkg.com/features/pnp

### node_modules의 문제점

- 기존 방식
  -  `yarn install` 시 Node Resolution Algorithm에 따라  node_modules 디렉토리를 만든다.
  - Node는 "패키지"가 무엇인지 모른다.
    - "여기 파일이 있나? 없어? 그럼 부모 node_modules로 가자. 여기 파일이 있나? 없어? ..."
  - 이런 방식은 비효율적
    - node_modules 디렉토리에 엄청난 양의 파일
    - node_modules 생성은 무거운 I/O 작업, 최적화의 여지가 적음
    - package.json에 dependency 하나를 빼먹어서 고장날 수 있음
    - 런타임마다 Node resolution이 `stat`, `readdir` 호출을 해야해서 부팅이 오래 걸림
- 해결
  - Yarn은 이미 dependency tree에 대해 모두 알고 있음!
  - 그러니 Node에게 패키지 위치 찾기를 맡기지 말자. 대신 패키지 매니저가 일하게 하자. 패키지 매니저가 패키지 위치를 인터프리터에게 알려주고, 패키지 간 종속성을 관리하도록 하자.
  - Plug 'n' Play 모드에서는  node_modules 대신 `.pnp.cjs` 파일 하나를 만든다.
  - 이 파일에는 패키지 이름 + 버전과 위치, 종속성 배열이 매핑된다. 이를 이용해 바로 패키지의 위치를 Node에게 전해줄 수 있다.