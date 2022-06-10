# 카카오 로그인 구현하기(FE)

> React + Typescript + NextJS
>
> Next Auth 라이브러리를 발견해서 열심히 공부해서 적용해보려 했는데 너무 어려워서 포기했슴다!
>
> 그냥 원래 방식대로 해봤슴다!

### 1. 카카오 API 키 받아오기

`https://developers.kakao.com/ 에서 받을 수 있음

`내 애플리케이션 > 앱 키` 에서 REST API키가 `Client_ID` 임

`내 애플리케이션 > 플랫폼` 에서 Web에 도메인 추가 : `http://localhost:3000`

바로 밑에 Redirect URI 등록 : `http://localhost:3000/api/auth/callback/kakao`



### 2. 프로젝트 파일에 env 변수 저장하기

`.env` 파일 만들고 저장

```
// .env

KAKAO_CLIENT_ID=내키비밀
KAKAO_REDIRECT_URI=http://localhost:3000/api/auth/callback/kakao
```



`next.config.js`에서 env 등록

```javascript
// next.config.js
module.exports = {
    ...,
    env: {
        KAKAO_CLIENT_ID,
        KAKAO_REDIRECT_URI,
  },
}
```



### 3. 카카오 로그인 버튼 만들기

카카오 로그인 버튼 컴포넌트 만들기

```react
import Link from "next/link";

const kakaoGetAuthCodeURL = `https://kauth.kakao.com/oauth/authorize?client_id=${process.env.KAKAO_CLIENT_ID}&redirect_uri=${process.env.KAKAO_REDIRECT_URI}&response_type=code`;

export default function KakaoLoginButton() {
  console.log(process.env.KAKAO_CLIENT_ID);
  return (
    <div>
      <Link href={kakaoGetAuthCodeURL}>
        <a>Kakao Login</a>
      </Link>
    </div>
  );
}
```

3번째 줄 url 양식은 카카오 dev 문서에 있음!



`/pages` 폴더에 `login.tsx` 만들기

```react
import KakaoLoginButton from "../components/auth/KakaoLoginButton";

export default function loginPage() {
  return (
    <>
      <KakaoLoginButton></KakaoLoginButton>
    </>
  );
}
```

![image-20220425151403598](../AppData/Roaming/Typora/typora-user-images/image-20220425151403598.png)

/login으로 가보면 버튼이 있음(아무튼 버튼)

누르면

 ![image-20220425151439551](../AppData/Roaming/Typora/typora-user-images/image-20220425151439551.png)

나옴.

확인하고 계속하기 누르면

![image-20220425151542139](../AppData/Roaming/Typora/typora-user-images/image-20220425151542139.png)

![image-20220425151526086](../AppData/Roaming/Typora/typora-user-images/image-20220425151526086.png)

다시 localhost:3000으로 Redirect되는데 URL이 위와 같음.

카카오 dev에서 설정한 Redirect URI에 뒤에 `?code=` 이 붙음.

이 코드가 인가코드임.

일단 404가 뜨지 않도록 API 루트 만들기.

### 4. API route만들기

`pages/auth/kakao` 폴더에 `[...params].js` 만듦.

```react
import { useRouter } from "next/router";

export default function KakaoAuth() {
  const router = useRouter();
  const { code } = router.query;
  console.log(code);
  return <div>Login...</div>;
}
```

> 주의 : /api 폴더에 페이지 만들면 안됨... 이것때문에 1시간 검색함...
>
> pages/api 폴더에 들어간건 전부 `/api/*` 로 매핑되고 `page` 대신 API endpoint 취급.

다시 확인하고 계속하기 누르면

![image-20220425155753892](../AppData/Roaming/Typora/typora-user-images/image-20220425155753892.png)

콘솔창에 code 찍힘.



이제 이 code를 우리 백엔드로 보내면 됨.

API 명세서에 따라서 API 요청 코드 작성.

### 5. API 요청 axios 코드 작성

`/api` 폴더 `member.ts`에 작성했음.

API 명세서 보고 작성했습니다.

```react
// /api/member.ts

import { api } from ".";

export const kakaoLogin = async (code: string) => {
  return await api.get(`/api/members/login/kakao?${code}`);
};

```

