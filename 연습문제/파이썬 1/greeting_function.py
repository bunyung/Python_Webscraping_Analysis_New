# greeting_function.py

def greet(name, greeting="안녕하세요", suffix="님!"):
    print(f"{greeting}, {name}{suffix}")

# 출력 예제
greet("김철수")  # 기본값 사용
greet("John", greeting="Hello")  # 영어 인사
greet("이영희", suffix="님! 좋은 하루 되세요!")  # 기본값이 아닌 suffix 사용
