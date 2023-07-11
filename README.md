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
