# Git merge request close

## 발단

- Remote 저장소에 `$ git push origin master:<branch>` 로 새로운 branch로 push 했다.
- 그리고 remote 저장소 master branch에 merge request까지 올렸다.
- 올리고 보니 수정해선 안되는 파일까지 수정하고 올려버린걸 확인했다.
- 당황하며 Close request 버튼을 눌러 request를 닫았다.

## 삽질

- 이것저것 건드리다가 뇌정지가 와버렸다.
- 구글에 검색해서 나오는 명령어들을 막 써보는데 소용 없었다.
- 정신이 없었다. 내가 뭘 하고 있는지도 몰랐다. 깃과 파일이 머릿속에서 엉키기 시작했다.
- 결국 local 저장소를 모두 지우고 다시 clone을 받았다.
- 그런데 다시 local의 수정사항을 push하려고 하니 에러가 발생했다.
- merge request를 close 하더라도 remote에는 여전히 이전에 commit 한 branch가 남아있는데 다시 그 branch로 push를 하려하니 충돌이 일어난 것 같았다.
- 그래서 `$ git push origin --delete <branch>` 로 remote의 해당 branch를 삭제해버렸다.
- 그리고 다시 push를 하니 제대로 된 것 같다.



## 결론

- 생각을 하고 하자.



