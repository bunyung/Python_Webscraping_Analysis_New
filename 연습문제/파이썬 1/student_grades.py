# student_grades.py

# 학생 성적 딕셔너리
grades = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 78,
    "최수진": 95
}

# 학생 성적 출력
print("학생 성적:")
for name, score in grades.items():
    print(f"{name}: {score}점")

# 평균 점수 계산
average = sum(grades.values()) / len(grades)

# 평균 점수 출력
print(f"평균 점수: {average:.1f}점")
