# PWA

Progressive Web Application

https://developer.mozilla.org/ko/docs/Web/Progressive_web_apps/Introduction

## PWA가 뭐야?

PWA는 웹과 네이티브 앱의 기능 모두의 이점을 갖도로 개발된 웹 앱.

2015년 용어 등장. 2016년 Google I/O 에서 미래의 웹 기술로 공식적으로 소개.



### 웹 앱 vs. 네이티브 앱

#### 웹 앱

HTML, CSS, JS 등으로 만든 앱. 모바일 웹과 네이티브 앱을 결합. 모바일 웹의 특징과 함께 네이티브 앱의 장점.

**장점**

- 접근이 쉬움. URL만 있으면 접근이 가능, 
- 별도의 설치 필요 없음
- 링크로 공유 가능.
- 홈 화면에 바로 가기 추가해서 네이티브 앱 처럼 사용 가능

**단점**

- 온라인에서만 동작
- 하드웨어 사용 불가
- 플랫폼 API 사용 불가

#### 네이티브 앱

모바일 기기에 최적화된 언어(Java, Kotiln, Swift, Object C)로 개발된 앱.

**장점**

- 운영 체제와 더 잘 통합되어 부드러운 UX 제공, 안정적.
- 오프라인에서도 동작
- 카메라 같은 장치와도 상호작용 가능.

**단점**

- 플랫폼에 한정적이라는 단점.
- 플랫폼마다 맞는 앱을 제작해야하는 비용 문제.



**PWA는 웹 앱의 높은 접근성, 네이티브 앱의 높은 기능성을 모두 포함.**

> "That app looks like native, I hope it behaves like it."
>
> 네이티브 앱처럼 보이니, 실제로 그렇게 행동하길 바람.



### PWA

PWA는 특정한 기술이 아님. 일부 특정 패턴, API, 기능들을 포함하는 웹 앱 구축에 대한 새로운 철학임.

PWA인가 아닌가를 구분하는 기능들

- 오프라인에서 동작
- 설치 가능
- 쉬운 동기화
- 푸시 알림 등

#### PWA 가치

비교적 적은 노력으로 PWA 기능들을 구현 가능하지만, 이점이 상당함.

- Service Workers를 사용한 캐싱으로 대역폭, 시간 절약 => 앱 설치 후 로딩 시간 단축. 

- 앱 업데이트 시 변경된 컨텐츠만 업데이트.
- 네이티브 플랫폼에 통합된 외관과 느낌.
- 알림 및 푸시 메시지 => 재참여율 증가



## PWA의 조건

**PWA 점수**

- Lighthouse
- [PWABuilder](https://www.pwabuilder.com/)

### 핵심 3가지 요건

#### 1. HTTPS

PWA는 신뢰할 수 있는 사이트에서만 동작. 웹 페이지가 HTTP 도메인에서 제공되어야함.

#### 2. 서비스 워커(Service Worker)

https://developer.mozilla.org/ko/docs/Web/API/Service_Worker_API

백그라운드에서 실행되는 JS 파일 형태의 스크립트. 웹 앱, 브라우저, 네트워크 사이의 프록시 서버 역할.

네트워크 가로채서 적절한 행동을 취함. 여기서는 오프라인 환경에서도 웹이 작동할 수 있도록 네트워크 요청을 가로채서 네트워크 불량 상태 등 접속성이 안좋은 상황 커버함.

네트워크 요청 중간에서 가로챈다는 점 때문에 중간자 공격에 취약. => HTTPS에서만 동작.

#### 3. Manifest(매니페스트)

PWA에 대해 브라우저에 알려주고 사용자의 기기에 설치할 때 어떻게 작동해야하는지 알려주는 JSON 파일.

웹페이지의 url과 앱 이름, 화면 표시 방식 등 기능과 표시 방법에 대한 정보들 포함.



### 원칙들

#### web.dev 핵심 PWA 체크리스트

https://web.dev/i18n/ko/pwa-checklist/

1. 빠르게 시작하고 빠르게 유지(Starts fast, stays fast)
2. 모든 브라우저에서 작동(Works in any browser)
3. 모든 화면 크기에 대응(Responsive to any screen size)
4. 맞춤형 오프라인 페이지 제공(Provides a custom offline page)
5. 설치 가능(Is installable)

#### web.dev 최적 PWA 체크리스트

1. 오프라인 경험 제공(Provides an offline experience)
2. 완전 접근 가능(Is fully accessible)
3. 검색으로 찾을 수 있음(Can be discovered through search)
4. 모든 입력 유형에 작동(Works with any input type)
5. 권한 요청에 대한 컨텍스트 제공(Provides context for permission requests)
6. 건전한 코드를 위한 모범 사례 따름(Follows best practices for healthy code)

#### **MDN PWA 핵심 원칙**

1. Discoverable(발견 가능) : 검색 엔진으로 찾을 수 있어야 함.
2. Installable(설치 가능) : 디바이스 홈 화면이나 앱 런처에서 사용 가능해야함.
3. Linkable(연결 가능) : URL로 공유 가능해야함.
4. Network independent(네트워크 독립적) : 오프라인이나 불안정한 네트워크 연결에서도 동작해야함.
5. Progressively enhanced(점진적) : 최신 브라우저는 안되더라도, 예전 기본 브라우저의 기능은 사용할 수 있어야 함.
6. Re-engageable(재참여 가능) : 새 컨텐츠가 이용 가능해지면 알림을 보낼 수 있어야 함.
7. Secure(안전) : 사용자, 앱, 서버 간의 연결이 민감한 데이터에 접근하려는 모든 서드파티에서 안전해야함. 



## Service Worker

https://developer.mozilla.org/ko/docs/Web/API/Service_Worker_API

웹 앱, 브라우저, 네트워크 사이의 프록시 서버 역할.

네트워크를 가로채서 적절한 행동을 취함.



## Creat-react-app에서 PWA 만들기

https://create-react-app.dev/docs/making-a-progressive-web-app/



## Next.js 에서 PWA 만들기

### **next-pwa**

https://www.npmjs.com/package/next-pwa

```
npm i next-pwa
```

### 기본 사용법

#### Step1 : withPWA

최상단에 `next.config.js` 파일에

```javascript
// next.config.js

const withPWA = require('next-pwa')

module.exports = withPWA({
  pwa: {
    dest: 'public'
  }
})
```

#### Step2: Manifest File 추가

`public` 폴더에 `manifest.json` 파일 생성. 

(예시)

```json
// manifest.json

{
  "name": "PWA App",
  "short_name": "App",
  "icons": [
    {
      "src": "/icons/android-chrome-192x192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "/icons/android-chrome-384x384.png",
      "sizes": "384x384",
      "type": "image/png"
    },
    {
      "src": "/icons/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "theme_color": "#FFFFFF",
  "background_color": "#FFFFFF",
  "start_url": "/",
  "display": "standalone",
  "orientation": "portrait"
}
```

#### Step 3: Head Meta 추가(예시)

`_document.jsx` , 또는 `_app.tsx` 의 `<Head>` 안에 다음 추가.(예시)

```tsx
<meta name='application-name' content='PWA App' />
<meta name='apple-mobile-web-app-capable' content='yes' />
<meta name='apple-mobile-web-app-status-bar-style' content='default' />
<meta name='apple-mobile-web-app-title' content='PWA App' />
<meta name='description' content='Best PWA App in the world' />
<meta name='format-detection' content='telephone=no' />
<meta name='mobile-web-app-capable' content='yes' />
<meta name='msapplication-config' content='/icons/browserconfig.xml' />
<meta name='msapplication-TileColor' content='#2B5797' />
<meta name='msapplication-tap-highlight' content='no' />
<meta name='theme-color' content='#000000' />

<link rel='apple-touch-icon' href='/icons/touch-icon-iphone.png' />
<link rel='apple-touch-icon' sizes='152x152' href='/icons/touch-icon-ipad.png' />
<link rel='apple-touch-icon' sizes='180x180' href='/icons/touch-icon-iphone-retina.png' />
<link rel='apple-touch-icon' sizes='167x167' href='/icons/touch-icon-ipad-retina.png' />

<link rel='icon' type='image/png' sizes='32x32' href='/icons/favicon-32x32.png' />
<link rel='icon' type='image/png' sizes='16x16' href='/icons/favicon-16x16.png' />
<link rel='manifest' href='/manifest.json' />
<link rel='mask-icon' href='/icons/safari-pinned-tab.svg' color='#5bbad5' />
<link rel='shortcut icon' href='/favicon.ico' />
<link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Roboto:300,400,500' />
     
<meta name='twitter:card' content='summary' />
<meta name='twitter:url' content='https://yourdomain.com' />
<meta name='twitter:title' content='PWA App' />
<meta name='twitter:description' content='Best PWA App in the world' />
<meta name='twitter:image' content='https://yourdomain.com/icons/android-chrome-192x192.png' />
<meta name='twitter:creator' content='@DavidWShadow' />
<meta property='og:type' content='website' />
<meta property='og:title' content='PWA App' />
<meta property='og:description' content='Best PWA App in the world' />
<meta property='og:site_name' content='PWA App' />
<meta property='og:url' content='https://yourdomain.com' />
<meta property='og:image' content='https://yourdomain.com/icons/apple-touch-icon.png' />

<!-- apple splash screen images -->
<!--
<link rel='apple-touch-startup-image' href='/images/apple_splash_2048.png' sizes='2048x2732' />
<link rel='apple-touch-startup-image' href='/images/apple_splash_1668.png' sizes='1668x2224' />
<link rel='apple-touch-startup-image' href='/images/apple_splash_1536.png' sizes='1536x2048' />
<link rel='apple-touch-startup-image' href='/images/apple_splash_1125.png' sizes='1125x2436' />
<link rel='apple-touch-startup-image' href='/images/apple_splash_1242.png' sizes='1242x2208' />
<link rel='apple-touch-startup-image' href='/images/apple_splash_750.png' sizes='750x1334' />
<link rel='apple-touch-startup-image' href='/images/apple_splash_640.png' sizes='640x1136' />
-->
```





### **Next.js PWA Example**

https://github.com/vercel/next.js/tree/canary/examples/progressive-web-app

![image-20220417225036036](../AppData/Roaming/Typora/typora-user-images/image-20220417225036036.png)

다운로드 버튼이 생긴다.



`next.config.js` 

```javascript
// next.config.js

/** @type {import('next').NextConfig} */
const withPWA = require('next-pwa')
const runtimeCaching = require('next-pwa/cache')

module.exports = withPWA({
  pwa: {
    dest: 'public',
    runtimeCaching,
  },
})
```



`/pages/_app.tsx`

```tsx
// _app.tsx

import Head from 'next/head'
import '../styles/globals.css'
import { AppProps } from 'next/app'

export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <meta charSet="utf-8" />
        <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
        <meta
          name="viewport"
          content="width=device-width,initial-scale=1,minimum-scale=1,maximum-scale=1,user-scalable=no"
        />
        <meta name="description" content="Description" />
        <meta name="keywords" content="Keywords" />
        <title>Next.js PWA Example</title>

        <link rel="manifest" href="/manifest.json" />
        <link
          href="/icons/favicon-16x16.png"
          rel="icon"
          type="image/png"
          sizes="16x16"
        />
        <link
          href="/icons/favicon-32x32.png"
          rel="icon"
          type="image/png"
          sizes="32x32"
        />
        <link rel="apple-touch-icon" href="/apple-icon.png"></link>
        <meta name="theme-color" content="#317EFB" />
      </Head>
      <Component {...pageProps} />
    </>
  )
}
```



`/public/manifest.json`

```json
{
  "name": "Next.JS Progressive Web App",
  "short_name": "Next PWA",
  "theme_color": "#ffffff",
  "background_color": "#004740",
  "display": "fullscreen",
  "orientation": "portrait",
  "scope": "/",
  "start_url": "/",
  "icons": [
    {
      "src": "icons/icon-72x72.png",
      "sizes": "72x72",
      "type": "image/png"
    },
    {
      "src": "icons/icon-96x96.png",
      "sizes": "96x96",
      "type": "image/png"
    },
    {
      "src": "icons/icon-128x128.png",
      "sizes": "128x128",
      "type": "image/png"
    },
    {
      "src": "icons/icon-144x144.png",
      "sizes": "144x144",
      "type": "image/png"
    },
    {
      "src": "icons/icon-152x152.png",
      "sizes": "152x152",
      "type": "image/png"
    },
    {
      "src": "icons/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "icons/icon-384x384.png",
      "sizes": "384x384",
      "type": "image/png"
    },
    {
      "src": "icons/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "splash_pages": null
}

```

