# conditional_expression.py

score = 85
result = "합격" if score >= 80 else "불합격"
print(f"점수: {score}, 결과: {result}")

age = 17
status = "성년자" if age >= 18 else "미성년자"
print(f"나이: {age}, 상태: {status}")

numbers = [5, 12, 42, 8, 23]
max_num = max(numbers)
positive_numbers = [num for num in numbers if num > 0]

print(f"숫자들의 최대값: {max_num}")
print(f"양수들: {positive_numbers}")
