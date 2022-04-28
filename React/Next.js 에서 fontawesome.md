# Next.js 에서 fontawesome

https://fontawesome.com/v5/docs/web/use-with/react#next-js

Next.js는 CSS를 다른 web 프로젝트랑 다르게 다룸.

그냥 react-fontawesome을 사용했다가는 **엄청 큰** 아이콘을 볼 수 있음 (저도 그랬습니다)

### Font Awesome CSS 작동하게 하기

`pages/_app.js`에 아래 코드 추가

```react
import { config } from '@fortawesome/fontawesome-svg-core'
import '@fortawesome/fontawesome-svg-core/styles.css'
config.autoAddCss = false
```

위 코드 설명

- Next.js 는 `.js`파일에 직접 CSS import 가능
- `config.autoAddCss = false` 는 Font Awesome core SVG 라이브러리가 더이상 페이지 `<head>`에 `<style>` 요소를 추가하지 않음. 추가하려고 해도 Next.js가 막음.



### Pages에서 Icons 사용하기

```react
import Head from 'next/head'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faFaceRelieved } from '@fortawesome/pro-solid-svg-icons'

export default function Home() {
    return (
        <div className="container">
            <main>
                <h1 className="title">
                    <FontAwesomeIcon icon={faFaceRelieved} />
                    Welcome to <a href="https://nextjs.org">Next.js!</a>
                </h1>
            </main>
        </div>
    )
}
```



