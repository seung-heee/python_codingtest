# 시간 복잡도 : O(N)
array = [3, 5, 1, 2, 4]
summary = 0  # 합계를 저장할 변수
for x in array:
    summary += x
print(summary)

# 시간 복잡도 : O(N^2)
array = [3, 5, 1, 2, 4]
for i in array:
    for j in array:
        temp = i *j
        print(temp, end=" ")