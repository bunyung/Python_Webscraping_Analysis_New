# module_usage.py
import datetime
import random

# 현재 날짜와 시간 출력
now = datetime.datetime(2025, 7, 20, 14, 30, 25)  # 문제 예시와 동일한 시간 지정
print(f"현재 날짜와 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 포맷된 날짜 (요일 포함)
formatted_date = now.strftime("%Y년 %m월 %d일 %A")
print(f"포맷된 날짜: {formatted_date}")

# 임의의 정수 (1~10)
rand_int = random.randint(1, 10)
print(f"임의의 숫자: {rand_int}")

# 임의의 실수 (예: 1.0~5.0)
rand_float = round(random.uniform(1.0, 5.0), 2)
print(f"임의의 실수: {rand_float}")

# 리스트 요소 랜덤 선택 및 섞기
fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
rand_choice = random.choice(fruits)
print(f"임의의 리스트 요소: {rand_choice}")

random.shuffle(fruits)
print(f"섞인 리스트: {fruits}")
