# 그리디 _ 숫자게임
# 특정 숫자 s에서 x개를 제거하여 가장 큰 숫자를 출력하는 프로그램

s, x = input('특정 숫자s, 제거 숫자 개수 X 입력 :').split() # 값 입력받기
s_lst = [int(i) for i in s] # s를 정수로 변경해서 리스트에 넣기

s_lst.sort(reverse=True) # 내림차순 정렬
print(s_lst)

for i in range(int(x)): # x번 반복
    s_lst.pop() # 맨 뒤 요소부터 삭제 (맨 뒤에는 제일 작은 값이 있음)
print(s_lst)

result = int(''.join(map(str, s_lst))) # 리스트 값들 결합, 정수로 변환
print(result) # 값 출력

