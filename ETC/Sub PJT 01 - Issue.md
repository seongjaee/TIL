# Sub PJT 01 - Issue

- 프로젝트 `npm run serve` 시

  `ERROR: PostCSS received undefined instead of CSS string` 발생

  - 해결

    `npm rebuild node-sass`

    node-sass 버전 문제인듯? 

-  Vue3 Warning `Extraneous non-emits event listeners `

  - 해결

    `login-dialog.vue`에 `emits: ['closeLoginDialog']` 추가.

- Vue3 Warning ` You are running the esm-bundler build of vue-i18n.`

  - 해결

    `import { createI18n } from 'vue-i18n/index'` 로 수정

- Element plus form `validate` 에러

  `validate` 함수는 반드시  `callback`이 한 번 호출되야함!
