# NodeJS address already in use 에러

`Error: listen EADDRINUSE: address already in use :::3000`

이미 포트가 사용중인 프로세스가 있어서 에러가 발생했다.

- cmd에서 `netstat -ano` 명령어로 모든 포트의 PID를 표시

- 3000번 포트를 사용중인 PID를 찾는다.
- 작업관리자 또는 `$ kill` 명령어로 해당 프로스세를 종료시킨다.

