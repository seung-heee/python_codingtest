n = 4
m = 3
# n행 X m열 크기의 2차원 리스트 생성
array = [[0] * m for _ in range(n)]
print(array)
print(type(array))  # 자료구조 타입 확인 list

array[2][1] = 5  # 2행 1열 값 변경
print(array)

a = [1, 4, 3]
print("기본 리스트 : ", a)
a.append(2)  # 리스트에 원소 삽입
print("삽입 : ", a)

a.sort()  # 오름차순 정렬
print("오름차순 정렬 : ", a)

a.sort(reverse=True)  # 내림차순 정렬
print("내림차순 정렬 : ", a)

a.insert(2, 6)  # 2번 인덱스에 숫자 6 추가
print("인덱스 2에 6추가 : ", a)

print("값이 3인 데이터 개수 : ", a.count(3))  # 3의 개수 세기

a.remove(1)  # 특정 값 데이터 삭제
print("값이 1인 데이터 삭제:", a)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}  # 집합 자료형 활용, 특정 원소 제거하기 위해서

# 리스트 a를 반복해서 result에 넣음, 단 remove_set에 없는 값이어야 함
result = [i for i in a if i not in remove_set]
print(result)  # 3, 5를 제외한 값만 들어간다.

# 문자열 리스트
arr_str = ["seung", "hee", "okay"]
print(arr_str)
arr_str.append("yeah~")  # 요소 추가
print(arr_str)
arr_str.insert(1, "hungry")  # 인덱스 1번에 요소 삽입
print(arr_str)
arr_str.pop()  # 마지막 요소 삭제
print(arr_str)
arr_str.sort()
print("정렬됨", arr_str)  # 정렬 z~a 순으로

# 복합 리스트
arr_both = [1, 2, 3, "seung", "hee"]
print(arr_both)
arr_both.append("hahaha")
print(arr_both)
arr_both.insert(4, "배고파요")
print(arr_both)
