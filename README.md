# python_codingtest

2023 방학특강\_코딩테스트

코딩테스트를 위한 파이썬 저장소~

###### 한글깨짐 수정

Settings -> Code-runner: Excutor Map -> code-runner.executorMap -> "python": "set PYTHONIOENCODING=utf8 && python -u" 수정

#### Day01(230710):

- 주요 실습 사항 파이썬 환경설정 실행 및 git 연동
- 입/출력 split() : 데이터입력/분리, join() : 데이터 병합, 문자열 포맷팅
- 변환/연산자 : ord(), chr(), round(), upper(), lower(), 출력 포맷: %x, %d, %o
- 조건문/반복문 : if, for, range, while, break, range(순회)

#### Day02(230711):

- 자료형

  - 문자열, 리스트
    .len() : 길이
    .min() : 최솟값
    .max() : 최댓값
    .find("d") : 문자열 내 d의 위치(인덱스)
    .replace('원래문자', '변경문자') : 문자 변경
    .append() : 요소 추가
    .count() : 요소 개수
    .insert(index, 값) : index위치에 값 삽입
    .remove() : 제거
    .sort() : 정렬(기본은 오름차순)
    .reverse() : 거꾸로 뒤집기
    .pop() : 마지막 요소 제거

  - 튜플 : 정적 데이터 삽입, 서로 다른 데이터 묶어서 관리, 최단 경로 알고리즘 or 해싱의 키로 자주 활용됨(값x)

#### Day03(230712):

- 알고리즘 복잡도
  - 시간 복잡도 : 특정한 크기의 입력에 대하여 알고리즘의 수행 시간 분석
  - 공간 복잡도 : 특정한 크기의 입력에 대하여 알고리즘의 메모리 사용량 분석
- 빅오표기법 :
  - O(N)-입력 데이터의 크기에 비례해 처리 시간이 증가하는 알고리즘 ex 1차원 for문
  - O(n²)-데이터가 많아질수록 처리시간이 급수적으로 늘어나는 알고리즘 ex 이중루프
- 성능 : O(1) < O(log n) < O(nlog n) < O(n²) < O(2ⁿ)
- 그리디 : 탐욕법, 욕심쟁이!

#### Day06(230717):

- 스택 : 선입후출 DFS

  - 추가 append()
  - 삭제 pop()
  - 재귀, DFS, 역추적 작업(괄호 검사, 후위 연산법, 문자열 역순 등)

- 큐 : 선입선출 BFS
- 데큐 : 양방향 큐 BFS

  - 추가 append()
  - 삭제 popleft()
  - 역순 reverse()
  - 프로세스, 순차 데이터 처리

- 재귀함수 : 자기 자신 다시 호출하는 함수 DFS
  - 반드시 종료 조건 지정
  - 팩터리얼(factorial 함수) – 콜 스택 저장(메모리 사용)
  - 유클리드 호제법 - 최대공약수, 피보나치
