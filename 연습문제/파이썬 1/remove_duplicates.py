# remove_duplicates.py

original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

print(f"원본 리스트: {original_list}")

# 중복 제거 후 정렬
unique_sorted_list = sorted(set(original_list))

print(f"중복 제거 후: {unique_sorted_list}")
