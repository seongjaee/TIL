# Git - branch

## Commit

Root commit 을 제외한 모든 Commit은 모두 부모 commit을 가진다.

자신의 부모 commit을 이용해 과거의 기록을 따라갈 수 있다.



## Branch

Branch는 특정 commit의 포인터이다.

master branch는 기본으로 제공되는 포인터 이름이다.

HEAD는 "현재 작업하고 있는" commit의 포인터다.

즉, HEAD -> master 는 현재 작업하고 있는 commit은 master가 가리키는 commit이라는 뜻이 된다.

새로운 commit 생성 시 HEAD와 HEAD가 가리키는 branch도 같이 옮겨가게 된다.

새로운 branch 생성 시 현재 작업중인 commit에 새로운 포인터가 생성된다. 즉, 하나의 commit에 두 개의 포인터가 생긴 셈이다.

한 branch에서 작업을 한 후 commit을 하면 branch가 나뉘게 된다. 두 포인터가 다른 commit을 가리키게 된다.



## Merge

서로 다른 branch의 내용을 병합하는 게 merge다.



