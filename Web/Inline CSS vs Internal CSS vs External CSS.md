# Inline CSS vs Internal CSS vs External CSS

https://www.hostinger.com/tutorials/difference-between-inline-external-and-internal-css

## Inline CSS

```html
<p style="font-size: 20px; color: blue">
    Inline CSS
</p>
```

- HTML 태그에 직접 CSS 스타일을 선언한다.
- `style`은 모든 HTML에서 공통으로 사용할 수 있는 전역 특성이다.

- https://developer.mozilla.org/ko/docs/Web/HTML/Global_attributes/style
- 주로 테스트 등 빠른 스타일링을 위한 목적으로 사용된다.
- 장점
  - 테스트, 변경에 대한 미리보기 등 빠르게 확인할 수 있다.
  - 별도의 문서로 외부 스타일을 만들 필요가 없다는 장점이 있다.
- 단점
  - https://stackoverflow.com/questions/2612483/whats-so-bad-about-in-line-css
  - CSS 룰을 모든 HTML에 하나하나 추가하려면 시간 낭비, 유지 보수가 좋지 않다.
  - HTML 구조가 복잡해진다.
  - 웹페이지 사이즈와 다운로드 시간에 영향을 미친다.

## Internal CSS

```html
<style type="text/css">
    h1 {
        color: green;
        margin: 32px;
    }
</style>
```

- `<head>` 내에 `<style>`에 스타일을 지정한다.
- 장점
  - 싱글 페이지 내의 스타일을 적용하는데 효과적이다.
  - 클래스 선택자, ID 선택자를 사용할 수 있다.
  - HTML 파일에 코드만 추가하면 된다. 다른 추가적인 파일을 업로드할 필요 없다.
- 단점
  - 여러 페이지에 같은 스타일을 적용하려면 모든 페이지에 CSS 룰을 추가해야하기 때문에 시간 낭비.
  - HTML 파일의 사이즈가 커지므로 로딩 시간에 영향을 미친다.

## External CSS 

```css
/* style.css 파일 */
.container {
    display: flex;
    width: 320px;
    background-color: tomato;
}
```

```html
<!-- HTML head 태그 안에 -->
<link rel="stylesheet" type="text/css" href="style.css">
```

- 외부에 .css 파일을 만들어 HTML 파일에 link로 연결한다.

- 장점
  - 큰 웹사이트를 스타일링하는 데 적합하다.
  - 하나의 .css 파일을 수정하는 것만으로도 사이트 전체를 한 번에 수정 가능하다.
  - CSS의 분리로, HTML 파일이 간결한 구조를 갖게 되고 HTML 파일 사이즈가 작아진다.
- 단점
  - external css가 로드되기 전까지는 페이지가 정확히 렌더링되지 않을 수 있다.
  - 여러 CSS 파일을 업로드하거나 link하면 사이트 다운로드 시간이 길어질 수 있다.

