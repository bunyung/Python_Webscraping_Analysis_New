# factorial_functions.py

# 재귀 함수로 팩토리얼 계산
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# 반복문으로 팩토리얼 계산
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 테스트
print(f"5! (재귀) = {factorial_recursive(5)}")
print(f"5! (반복) = {factorial_iterative(5)}")
print(f"7! (재귀) = {factorial_recursive(7)}")
print(f"7! (반복) = {factorial_iterative(7)}")
