# multiple_sum.py

# 1부터 100까지 3의 배수 리스트 생성
multiples_of_3 = [num for num in range(1, 101) if num % 3 == 0]

# 합계와 개수 계산
total_sum = sum(multiples_of_3)
count = len(multiples_of_3)

# 결과 출력
print(f"1부터 100까지 3의 배수: {multiples_of_3}")
print(f"3의 배수의 합: {total_sum}")
print(f"3의 배수의 개수: {count}개")
