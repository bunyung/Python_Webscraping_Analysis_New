# character_counter.py

# 문자열 입력 받기
text = input("문자열을 입력하세요: ")

# 찾을 문자 입력 받기
char = input("찾을 문자를 입력하세요: ")

# 문자 개수 세기
count = text.count(char)

# 결과 출력
print(f"문자 '{char}'이 {count}번 나타납니다.")