def find_subarray_sum_count(arr, target_sum):
    n = len(arr)
    prefix_sum = [0] * (n + 1)

    # 누적 합 배열(prefix_sum)을 구합니다.
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    count = 0

    # 모든 i, j 쌍에 대해 합이 target_sum인 경우를 구합니다.
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            subarray_sum = prefix_sum[j] - prefix_sum[i - 1]
            if subarray_sum == target_sum:
                count += 1

    return count


# 입력 수열과 합 M을 받습니다.
N = int(input())
A = list(map(int, input().split()))
M = int(input())

result = find_subarray_sum_count(A, M)
print(result)
