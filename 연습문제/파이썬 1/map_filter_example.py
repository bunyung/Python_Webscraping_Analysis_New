# map_filter_example.py

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"원본 숫자: {numbers}")

# map을 사용해 모든 수의 제곱 계산
squared = list(map(lambda x: x ** 2, numbers))
print(f"모든 수의 제곱: {squared}")

# filter를 사용해 5보다 큰 수들 추출
filtered = list(filter(lambda x: x > 5, numbers))
print(f"5보다 큰 수들: {filtered}")

# 5보다 큰 수들의 제곱 (filter 후 map)
filtered_squared = list(map(lambda x: x ** 2, filtered))
print(f"5보다 큰 수들의 제곱: {filtered_squared}")
