# fruit_search.py

# 과일 목록 리스트
fruits = ['사과', '바나나', '오렌지', '포도', '딸기']

# 과일 목록 출력
print(f"과일 목록: {fruits}")

# 사용자로부터 찾을 과일 입력 받기
search_fruit = input("찾을 과일을 입력하세요: ")

# 과일 검색 및 결과 출력
if search_fruit in fruits:
    print(f"'{search_fruit}'가 목록에 있습니다!")
else:
    print(f"'{search_fruit}'가 목록에 없습니다.")
