# statistics_function.py
import math

def statistics(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    maximum = max(numbers)
    minimum = min(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_dev = math.sqrt(variance)
    return mean, maximum, minimum, std_dev

# 테스트
numbers = [10, 20, 30, 40, 50]
mean, maximum, minimum, std_dev = statistics(numbers)

print(f"숫자들: {numbers}")
print(f"평균: {mean:.1f}")
print(f"최댓값: {maximum}")
print(f"최솟값: {minimum}")
print(f"표준편차: {std_dev:.2f}")
