# Git 헷갈리는 상황 정리

**상황 1.**

- `브랜치 A`에서 작업을 하고 `remote 브랜치 A`로 push. pull request까지 올려둠.

- 곧바로 `로컬 브랜치 A`에서 `브랜치 B`를 따고 새로운 작업.
  브랜치 A에서 작업한 내용 수정.
- `브랜치 B`에서 `remote 브랜치 B`로 push, pull request까지 올려둠.

2개의 pull request를 순서대로 승인해도 충돌이 없을까?

- 충돌 없음.
- `리모트 브랜치 B` 로 push 하더라도 A와 B가 아예 별개 브랜치가 되는건 아님. 브랜치는 단순히 포인터일 뿐임.

![image](https://user-images.githubusercontent.com/81851585/159276067-e0789c05-3791-40e6-95a0-cc12b5a01652.png)
