# list_analysis.py

numbers = [15, 3, 27, 8, 19, 12, 31]

print(f"숫자 목록: {numbers}")

max_value = max(numbers)
min_value = min(numbers)

# 중복 제거 후 내림차순 정렬
unique_numbers = sorted(set(numbers), reverse=True)

# 두 번째로 큰 값 찾기
second_largest = unique_numbers[1] if len(unique_numbers) > 1 else None

print(f"최댓값: {max_value}")
print(f"최솟값: {min_value}")
print(f"두 번째로 큰 값: {second_largest}")
