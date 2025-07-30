# word_frequency.py
from collections import Counter
import re

# 예시 텍스트를 파일에 저장 (실제 파일이 있다면 이 부분은 생략하세요)
text = """파이썬은 강력한 프로그래밍 언어입니다.
파이썬 프로그래밍은 배우기 쉽고, 파이썬 언어는 다양한 분야에 사용됩니다."""

with open("sample.txt", "w", encoding="utf-8") as f:
    f.write(text)

# 파일 읽기
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 한글 단어만 추출 (필요시 수정 가능)
words = re.findall(r'\b[가-힣]+\b', content)

# 단어 빈도 계산
word_counts = Counter(words)

print("단어 빈도 분석 결과:")
for word, count in word_counts.most_common():
    print(f"{word}: {count}번")
