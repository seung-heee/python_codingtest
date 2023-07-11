# 도전7 : 리스트에 문자열을 저장하고 출력
arr = []  # 리스트 선언

while True:
    a = input()
    arr.append(a)  # 입력받은 값 a를 리스트에 추가
    if a == " ":
        break
print(arr)  # 입력받은 값들로 리스트 생성됨

for i in arr:  # for문으로 arr 리스트 출력
    print(i, end=" ")  # 띄어쓰기로 구분
