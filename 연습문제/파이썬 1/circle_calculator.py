# circle_calculator.py

# π 값을 상수로 정의
PI = 3.14159

# 사용자로부터 반지름 입력 받기
radius = float(input("원의 반지름을 입력하세요: "))

# 넓이와 둘레 계산
area = PI * radius ** 2
circumference = 2 * PI * radius

# 결과 출력 (소수점 둘째자리까지 반올림)
print(f"반지름이 {radius}인 원의 넓이: {area:.2f}")
print(f"반지름이 {radius}인 원의 둘레: {circumference:.2f}")
