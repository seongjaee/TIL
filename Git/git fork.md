# git fork

- 원격 저장소에 repository에서 fork 버튼을 누르면 해당 repository를 fork해올 수 있다.
- 기본적으로 `my-username/origin-git-name` 식으로 이름이 지어진다.
- 총 3개의 repository가 있다고 생각할 수 있다.
  - 원본
  - 나의 remote
  - 나의 local

## fork해온 repository update

- 내가 fork한 repository, 즉 원본 repository에 변경사항이 생겼다고 하자.
- 그러면 나의 remote, local repository에는 해당 변경사항이 적용되지 않았다.
- 이럴때
  1. `git remote add upstream <origin-git-repository>` 로 upstream이라는 이름으로 원본 저장소를 remote 저장소로 등록한다.
  2. `git fetch upstream`으로 upstream으로부터 변경사항을 받아온다.
  3. `git merge upstream/master` 로 master에 merge한다.
  4. 나의 remote 저장소도 업데이트하기위해 `git push origin master`로 push한다.