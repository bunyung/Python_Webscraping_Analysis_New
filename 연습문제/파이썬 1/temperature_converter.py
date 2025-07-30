# temperature_converter.py

# 사용자로부터 섭씨 온도 입력 받기
celsius = float(input("섭씨 온도를 입력하세요: "))

# 화씨로 변환
fahrenheit = celsius * 9 / 5 + 32

# 결과 출력
print(f"섭씨 {celsius}도는 화씨 {fahrenheit:.1f}도입니다.")
