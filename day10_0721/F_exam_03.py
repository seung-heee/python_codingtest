def tile_fill(N):
    # 크기 N의 dp 리스트 생성 후 초기화 
    dp = [0] * (N + 1)
    dp[1] = 1 # N = 1인 경우는 타일 세로로 하나 놓는 방법 1가지
    dp[2] = 2 # N = 2인 경우는 타일을 세로로 두개 놓는 방법 2가지

    # N = 3부터 N까지 dp 배열을 채운다
    for i in range(3, N + 1):
        # i 크기의 바닥을 채우는 방법은 i-1 크기의 바닥에 세로로 타일을 하나 추가하는 방법
        # + i -2크기의 바닥에 가로로 놓은 타일 두 개를 추가하는 방법의 합과 같음
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[N] 

N = int(input())
result = tile_fill(N)
print(result) 