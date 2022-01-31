# Vue 모드와 환경변수

https://cli.vuejs.org/guide/mode-and-env.html#example-staging-mode

## **3줄 요약**

- Vue CLI에는 모드와 환경 변수가 있음.
- 모드는 development, test, production, 사용자 지정 모드가 있음
- 각 모드마다 사용할 환경 변수를 env파일에 지정하여 사용할 수 있음.

## **1. 모드**

**모드**는 Vue CLI 프로젝트에서 중요한 컨셉. 다음의 세가지 모드가 있음

- `development` : `vue-cli-service serve`에서 사용됨
- `test` : `vue-cli-service test:unit` 에서 사용됨
- `production` : `vue-cli-service build` 와 `vue-cli-service test:e2e` 에서 사용됨

📌 `vue-cli-service`를 실행하면, **환경 변수**들이 모드에 맞춰 환경 변수 파일( `.env`, `.env.local`, `.env.[mode]`, `.env.[mode].local` )에서 로드됩니다.

📌 만약 해당 파일에 `NODE_ENV` 변수가 없으면 모드에 맞춰서 세팅됩니다. 예를 들어 production 모드에서는 `production`  로  development 모드에서는 `development` 로...

📌 `NODE_ENV` 는 앱의 프라이머리 모드를 결정합니다. 결과적으로 어떤 웹팩 구성이 생성될지 결정합니다. `NODE_ENV=development`는 HMR(Hot Module Replacement)이 가능한 webpack configuration을 만듭니다. asset hash나 vendor 번들을 만들지 않아 개발 서버 실행 시 빠른 재빌드를 가능하게 합니다.

📌 `vue-cli-service build`를 실행하는 경우, 배포 준비된 앱을 얻기 위해서는`NODE_ENV`는 production으로 설정되어야 합니다.

📌 `vue-cli-service`를 실행할때, default `NODE_ENV`가 환경에 있는 경우, 이걸 지우거나 명시적으로 NODE_ENV를 세팅해야합니다.

## **2. 환경 변수**

env 파일은 아래 4가지 종류가 있음.

- `.env` : 모든 경우 load됨
- `.env.local` : 모든 경우 load됨. gitignore에 기본으로 등록되어 git 무시됨.
- `.env.[mode]` : 특정 mode에서만 load 됨
- `.env.[mode].local` : 특정 mode에서만 load됨. git 무시됨.

📌 env 파일은 key=value 쌍으로 된 **환경 변수**들로 구성됩니다.

> 주의
>
> priveat API key 같은 걸 app에 저장하지 마세요!
>
> 환경 변수는 build에 embedded되어, 누구든 앱 파일에서 훔쳐볼 수 있습니다!

📌 **환경 변수**는 다음의 세 가지 종류가 있음

- `NODE_ENV`
- `BASE_URL`
- `VUE_APP_`으로 시작하는 사용자 정의 변수

위의 세가지 변수들은 `webpack.DefinePlugin`과 client bundle에 정적으로 임베디드됩니다.

로드된 변수들은 모든 `vue-cli-service` 커맨드, 플러그인, dependencies에서 사용가능해집니다.

📌환경 변수 파일은 반드시 루트 디렉토리에 생성해야함.

### **Client-Side Code에서 환경 변수 사용하기**

- `process.env.변수이름`으로 접근 가능
- `NODE_ENV` 는 `"production"`, `"development"`, `"test"` 셋중 하나로, 앱이 실행 중인 모드에 따라 결정.
- `BASE_URL` : `vue.config.js`에 `publicPath` 옵션, 앱이 배포되는 기본 경로에 따라 결정.

### **Local Only 변수들**

로컬에서만 사용하고 싶은 경우 `.local`로 끝나는 환경 파일에 넣어놓자. `.gitignore`가 기본적으로 무시해준다.