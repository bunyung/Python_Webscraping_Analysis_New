# unpacking_example.py

# 1. 리스트 언패킹 예제
coords = (10, 20)
x, y = coords
print(f"좌표: x={x}, y={y}")

# 2. 리스트 언패킹
values = [1, 2, 3]
a, b, c = values
print(f"리스트 언패킹: a={a}, b={b}, c={c}")

# 3. *args를 사용하는 함수 예제
def sum_all(*args):
    return sum(args)

print(f"가변 인수의 합: {sum_all(10, 20, 30)}")

# 4. **kwargs를 사용하는 함수 예제
def print_info(**kwargs):
    info = ", ".join(f"{key}={value}" for key, value in kwargs.items())
    print(f"키워드 인수들: {info}")

print_info(name="김철수", age=25, city="서울")
