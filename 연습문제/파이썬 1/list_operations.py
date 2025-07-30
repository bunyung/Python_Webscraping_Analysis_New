# list_operations.py

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print(f"리스트1: {list1}")
print(f"리스트2: {list2}")

# 병합 (중복 제거 없이)
merged_list = list1 + list2

# 병합 후 중복 제거 및 정렬
merged_unique_sorted = sorted(set(merged_list))

# 공통 요소 찾기 (교집합)
common_elements = sorted(set(list1).intersection(set(list2)))

print(f"병합된 리스트: {merged_unique_sorted}")
print(f"공통 요소: {common_elements}")
