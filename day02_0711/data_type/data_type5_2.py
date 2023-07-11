b = (2, "bakery", "coffee", 3.13, [5, 4, 3, 2, 1])  # 서로 다른 데이터/자료구조 입력
print(b)
b = b + (1.3, "name", 5)  # b가 변경된 것이 아닌, 새로 생성된 것
print(b)

t_length = len(b)
print(t_length)

lst = list(b)  # 리스트로 변환 내용 수전
print(lst)  # 튜플 b -> 리스트 lst로 변환됨!

c = tuple(lst)  # 리스트 -> 튜플로 변환
print(c)

del c  # del 키워드로 튜플 삭제

if "coffee" in b:  # 리스트 안 특정 데이터 존재 확인
    print("커피가 존재합니다.")
if "3.333" not in b:
    print("3.333은 존재하지 않습니다.")

d = (3, 4444, (55, 55), 6)  # 튜플 내 튜플 가능.
print(d)  # 중첩 튜플
