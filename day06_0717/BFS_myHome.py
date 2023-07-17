from collections import deque # 데큐 연동

n = int(input('단지의 크기 N를 입력 : ')) # 단지 크기 입력
arr = [list(map(int,input('단지 지도 세부 정보를 입력 : '))) for _ in range(n)] # 단지 세부 정보 입력
cnt=0 # 단지안에 속하는 집의 수 
cnt_arr=list() # 큐가 끝날때 최종 cnt를 담아줄 배열값

dx = [-1, 0, 1, 0] # 4가지방향 정의
dy = [0, 1, 0, -1]

q = deque() # 큐 선언

