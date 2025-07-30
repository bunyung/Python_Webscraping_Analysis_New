# log_processor.py
from datetime import datetime

# 로그 데이터를 리스트에 저장 (실제 로그 파일을 새로 생성하는 예)
logs = [
    "2025-07-20 09:15:00 - WARNING - 메모리 사용량이 높습니다",
    "2025-07-20 10:30:00 - ERROR - 데이터베이스 연결 실패",
    "2025-07-20 11:45:00 - ERROR - 파일을 찾을 수 없음",
    "2025-07-20 12:00:00 - WARNING - 디스크 공간 부족",
    "2025-07-20 13:00:00 - INFO - 시스템 정상 작동 중"
]

log_filename = "app.log"

# 로그 파일 생성
with open(log_filename, "w", encoding="utf-8") as f:
    for log in logs:
        f.write(log + "\n")

print("로그 파일이 생성되었습니다.\n")

# 로그 파일에서 특정 레벨 필터링 함수
def filter_logs(filename, level):
    filtered = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if f" - {level} - " in line:
                filtered.append(line.strip())
    return filtered

# ERROR 레벨 로그 출력
error_logs = filter_logs(log_filename, "ERROR")
print("ERROR 레벨 로그들:")
for log in error_logs:
    print(log)

print("\nWARNING 레벨 로그들:")
warning_logs = filter_logs(log_filename, "WARNING")
for log in warning_logs:
    print(log)
