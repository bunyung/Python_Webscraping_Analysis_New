# f_string_example.py
import datetime

name = "김철수"
age = 25
pi = 3.14159
price = 1234
percentage = 0.855
today = datetime.date(2025, 7, 20)

# f-string 방식 (추천)
print(f"이름: {name}, 나이: {age}")
print(f"원주율: {pi:.2f}")  # 소수점 둘째 자리까지
print(f"가격: {price:,}원")  # 천 단위 콤마
print(f"퍼센트: {percentage * 100:.2f}%")  # 85.50%
print(f"날짜: {today:%Y년 %m월 %d일}")
