# word_counter.py

# 사용자로부터 문장 입력 받기
sentence = input("문장을 입력하세요: ")

# 문자열 양쪽 공백 제거 및 중간 공백을 하나로 축소
cleaned_sentence = ' '.join(sentence.split())

# 단어 개수 세기
word_count = len(cleaned_sentence.split()) if cleaned_sentence else 0

# 결과 출력
print(f"공백 제거: {cleaned_sentence}")
print(f"단어 개수: {word_count}개")
