"""
문제 : 마을에 모험가 N명을 대상으로 공포도를 측정했다. 
공포도가 높으면 던전 입장이 어렵다. 
공포도가 X인 모험가는 반드시 X명 이상으로 모험가 그룹에 참여해야 던전 입장이 가능하다. 
최대 몇 개의 모험가 그룹을 만들 수 있는지 출력하라.
참고 : 모험가 인원 N을 입력 후, N개의 공포도를 입력 받음
"""
n = int(input("모험가 인원: "))
data = list(map(int, input("각 모험가 공포도 개수만큼 입력: ").split()))
data.sort()
result = 0
count = 0

for i in data:
    count += 1
    if i <= count:  # 최소 인원 충족되면
        result += 1  # 그룹 추가
        count = 0

print("총 그룹 수: ", result)
