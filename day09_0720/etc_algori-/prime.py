def prime(x):
    for i in range(x + 1):
        if i % 2 == 0:
            print(f"{i}는 짝수")
        else:
            print(f"{i}는 홀수")


prime(100)
