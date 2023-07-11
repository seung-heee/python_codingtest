# 도전 8 : 튜플에 리스트 문자열을 저장하고 출력
tple = ()  # 튜플 선언
lst = [1, 2, 3, [1, 2, 3], "seunghee"]  # 리스트
print(f"리스트 {lst}")
tple = tuple(lst)  # 리스트 데이터 받아 튜플로 캐스팅
print(f"튜플로 캐스팅! : {tple}")  # 출력
