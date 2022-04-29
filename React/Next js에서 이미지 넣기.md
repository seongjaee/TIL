# **Next js에서 이미지 넣기**

### 참고 문서

- https://nextjs.org/docs/api-reference/next/image

- https://nextjs.org/docs/basic-features/image-optimization#local-images

- https://birdmee.tistory.com/10



### Usage

로그인 페이지에서의 예시 코드입니다.

```jsx
import Image from "next/image";
import kakaoLoginButtonImage from "../../public/assets/img/login/kakao_login_medium_narrow.png";

import styled from "styled-components";

const ButtonContainer = styled.div`
  position: relative;
`;

const kakaoGetAuthCodeURL = `https://kauth.kakao.com/oauth/authorize?client_id=${process.env.KAKAO_CLIENT_ID}&redirect_uri=${process.env.KAKAO_REDIRECT_URI}&response_type=code`;

export default function KakaoLoginButton() {
  return (
    <>
      <ButtonContainer>
        <Link href={kakaoGetAuthCodeURL}>
          <a>
            <Image
              src={kakaoLoginButtonImage}
              alt="Kakao login button"
              layout="fill"
            />
          </a>
        </Link>
      </ButtonContainer>
    </>
```

## **Image Component**

- `next/image` 에서 `Image` 컴포넌트를 사용합니다.

  ```jsx
  import Image from 'next/image'
  ```



### src

- src 속성은 다음 2가지 중 하나여야합니다.

  1. 정적 임포트된 이미지 파일

  2. 문자열 경로. 외부 절대 경로 URL 이거나, `loader` prop이나 `loader configuration` 에 의존한 내부 경로

  외부 URL 사용하려면 도메인을 `next.config.js` 에 추가해야합니다.

  ```javascript
  module.exports = {
    images: {
      domains: ["aaa.bbb.com"],
    },
  }
  ```

  `https://`  없음에 주의해야합니다.



### **Local Image**

- 이미지 파일을 그대로 import 합니다.

  ```jsx
  import kakaoLoginButtonImage from "../../public/assets/img/login/kakao_login_medium_narrow.png";
  ```

  `await import()` , `require()` 지원이 안된다고 하네요.

  `import` 가 반드시 정적이여야 빌드 시 해석된다고 합니다.

- Next.js에서 자동으로 원본 크기대로 이미지의 너비, 높이를 설정해준다고 합니다.

  - 직접 넣고 싶은 경우 `width={}`, `height={}` 속성 값을 넣을 수 있다고 합니다.

### **Remote Image**

- `src` 속성에 URL 문자열이 들어가는데, 상대 경로도 되고 절대 경로도 된다고 합니다.
- 외부 URL을 사용할 때는 `next.config.js` 에 도메인 설정이 필요합니다.

## **Image Sizing**

- 이미지의 *layout shift* 때문에 애플리케이션 성능을 낮추는 경우가 많다고 합니다. (이미지가 나중에 로드되면서 이미지 주변의 다른 요소들 밀어버림)

  이 성능 문제는 사용자한테 굉장히 짜증나기 때문에 `Culmulative Layout Shift` 라고 불리는 [Core Web Vital](https://web.dev/cls/)이 따로 있다고 합니다.

- 이걸 막기 위해서는 **항상 이미지를 사이징해야한다**고 합니다. 그래야 브라우저에서 이미지 로드 전에 충분히 공간을 마련한다고 합니다.

- `next/image` 는 좋은 성능을 보장하게 설계됐기 때문에 layout shift가 발생하는 방식으로는 사용할 수 없다고 합니다. 그래서 다음 세 가지 방법 중 하나로 사이징해야한다고 합니다.

  1. (자동적인 방법) static import 사용
  2. 명시적으로, `width`, `height` 속성 사용
  3. 암시적으로 `layout="fill"` 사용해서 부모 요소에 맞추기.

- **내 이미지 사이즈 모르면?**

  - `layout="fill"` 쓰기
  - 이미지 정규화하기

## **Styling**

Image 컴포넌트 스타일링하는 법은 그냥 `<img>` 요소 스타일링이랑 딱히 다른 점은 없지만 다음을 명시해야함!

- 올바른 레이아웃 모드 선택
- DOM 구조가 아니라 className으로 image 타겟팅
- `layout="fill"` 쓸 때는 부모 요소가 `position: relative`여야함.
- `layout="responsive"` 쓸 때는 부모 요소가 `display: block`이어야함.