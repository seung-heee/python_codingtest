def find_infected_wards(num_wards, num_connections, connections):
    # 병동들 간의 연결 상태를 그래프로 표현하기 위해 인접 리스트를 사용
    graph = [[] for _ in range(num_wards + 1)]

    # 연결된 병동들을 그래프에 추가
    for connection in connections:
        ward1, ward2 = connection
        graph[ward1].append(ward2)
        graph[ward2].append(ward1)

    # 감염 여부를 체크하는 리스트를 초기화
    is_infected = [False] * (num_wards + 1)

    def dfs(ward):
        # 병동을 방문하고 감염 상태로 표시
        is_infected[ward] = True
        # 현재 병동과 연결된 다른 병동들을 확인하면서 감염되지 않은 경우 재귀적으로 탐색
        for neighbor in graph[ward]:
            if not is_infected[neighbor]:
                dfs(neighbor)

    # 첫 번째 병동(A씨가 위치한 병동)부터 DFS로 탐색을 시작
    dfs(1)

    # 감염된 병동의 개수를 세어 반환
    num_infected_wards = sum(is_infected) - 1  # A씨가 위치한 병동은 제외
    return num_infected_wards

# 입력 예시와 동일한 데이터로 함수를 호출하여 결과를 출력
num_wards = 7
num_connections = 6
connections = [(1, 2), (2, 3), (1, 5), (5, 2), (5, 6), (4, 7)]
result = find_infected_wards(num_wards, num_connections, connections)
print("감염됨 병동은 {}개입니다.".format(result))