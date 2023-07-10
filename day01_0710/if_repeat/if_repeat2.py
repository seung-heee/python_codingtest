a, b, c = map(int, input("정수 3개 중 짝수 출력 : ").split())
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)

s = map(int, input("정수 여러 개 입력 ㄱㄱ").split())
print(s)  # 정수 여러개 들어있는 리스트 s 반환
for i in s:  # 리스트 순회
    if i % 2 == 0:  # 짝수면
        print(i)  # 출력
