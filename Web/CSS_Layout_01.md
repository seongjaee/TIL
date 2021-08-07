# CSS_Layout_01

## Float

- 한 요소가 정상 흐름으로부터 빠져나와 텍스트 및 인라인 요소가 그 주위를 감싸 요소의 좌, 우측을 따라 배치되게 함

- 본래는 이미지를 한쪽으로 띄우고 텍스트가 둘러싸는 레이아웃

- 여기서 더 나아가 이미지가 아닌 요소들에도 적용 -> 웹사이트 전체 레이아웃


### Float 속성

- none: 기본값
- left: 왼쪽으로 띄움
- right: 오른쪽으로 띄움

- Float clear

  - float에 의해 레이아웃이 망가지는 걸 막아줌

  - ```css
    .clearfix::after {
        content: "";
        display: block;
        clear: both;
    }
    ```

  - `::after`  : 가상 요소를 만듦

    -  선택한 요소의 맨 마지막에 가상 요소를 생성
    -  보통 content 속성과 함께 요소에 장식용 콘텐츠 추가
    -  기본값은 inline

  - `clear: both;`

    - 선언으로 float에 영향을 받지 않도록 함
    - clear 속성은 float 및 비 float 요소 모두에 적용됨


### 정리

- flexbox 및 grid 레이아웃 나오기 전에 열 레이아웃을 만드는데 사용
- flexbox 및 grid 레이아웃의 출현으로 원래의 float 이미지를 위한 역할로 돌아감
  - MDN에서는 legacy 레이아웃 기술로 분류
- 웹에 여전히 사용하는 경우도 있음(naver nav 바)