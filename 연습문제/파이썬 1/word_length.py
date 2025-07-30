# word_length.py

words = ['cat', 'elephant', 'dog', 'butterfly', 'ant']

print(f"단어 목록: {words}")

# 가장 긴 단어 찾기
longest_word = max(words, key=len)

# 가장 짧은 단어 찾기
shortest_word = min(words, key=len)

print(f"가장 긴 단어: {longest_word} ({len(longest_word)}글자)")
print(f"가장 짧은 단어: {shortest_word} ({len(shortest_word)}글자)")
