# split_join_example.py

text = "Python is awesome programming language"

print(f"원본 문자열: {text}")

# split()으로 단어별 분리
words = text.split()
print(f"분리된 단어들: {words}")

# join()으로 하이픈(-) 연결
hyphen_joined = "-".join(words)
print(f"하이픈으로 연결: {hyphen_joined}")

# 대문자로 변환 후 공백으로 연결
upper_joined = " ".join(word.upper() for word in words)
print(f"대문자로 변환 후 공백으로 연결: {upper_joined}")
