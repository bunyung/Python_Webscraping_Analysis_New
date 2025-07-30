# dict_comprehension.py

# 1부터 5까지 숫자와 제곱값 딕셔너리
squares_dict = {i: i ** 2 for i in range(1, 6)}
print(f"1부터 5까지의 제곱 딕셔너리: {squares_dict}")

# 짝수만의 제곱 딕셔너리 (2,4,6,8,10)
even_squares_dict = {i: i ** 2 for i in range(2, 11, 2)}
print(f"짝수만의 제곱 딕셔너리: {even_squares_dict}")
