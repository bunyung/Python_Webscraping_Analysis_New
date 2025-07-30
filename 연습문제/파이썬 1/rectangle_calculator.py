# rectangle_calculator.py

# 사용자로부터 가로와 세로 길이 입력 받기
width = float(input("가로 길이를 입력하세요: "))
height = float(input("세로 길이를 입력하세요: "))

# 넓이와 둘레 계산
area = width * height
perimeter = 2 * (width + height)

# 결과 출력
print(f"직사각형의 넓이: {int(area) if area.is_integer() else area}")
print(f"직사각형의 둘레: {int(perimeter) if perimeter.is_integer() else perimeter}")
