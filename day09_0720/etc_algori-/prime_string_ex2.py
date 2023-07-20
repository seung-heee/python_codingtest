def is_prime(num):  # 소수인지 판별하는 함수
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):  # 2부터 num의 제곱근까지 반복
        if num % i == 0:  # 나누어진다면
            return False  # 소수가 아님
    return True  # 소수임


def find_largest_prime_substring(s):
    max_prime = 0
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = int(s[i:j])
            if is_prime(substring) and substring > max_prime:
                max_prime = substring

    return max_prime


while True:
    num_str = input()
    if num_str == "0":
        break
    else:
        result = find_largest_prime_substring(num_str)
        print(result)
