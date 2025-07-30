# basic_calculator.py

# 사용자로부터 두 개의 정수를 입력받음
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

# 사칙연산 결과 출력
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

# 나눗셈은 0으로 나누는 경우를 예외 처리하고, 소수 둘째 자리까지 표시
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2:.2f}")
else:
    print("0으로 나눌 수 없습니다.")