# string_operations.py

# 사용자로부터 문자열 입력 받기
text = input("문자열을 입력하세요: ")

# 대문자, 소문자 변환 및 길이 계산
upper_text = text.upper()
lower_text = text.lower()
length = len(text)

# 결과 출력
print(f"대문자: {upper_text}")
print(f"소문자: {lower_text}")
print(f"문자열 길이: {length}")
