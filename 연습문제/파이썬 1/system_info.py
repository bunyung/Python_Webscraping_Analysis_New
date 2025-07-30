# system_info.py
import os
import sys

# 현재 작업 디렉토리
current_dir = os.getcwd()
print(f"현재 작업 디렉토리: {current_dir}")

# Python 버전 정보
python_version = sys.version.split("\n")[0]
print(f"Python 버전: {python_version}")

# 운영체제 정보
os_name = os.name
print(f"운영체제: {os_name}")

# 환경 변수 PATH 일부 출력 (앞 4개 디렉토리만 예시)
path_env = os.environ.get("PATH", "")
print(f"환경 변수 PATH 일부: {':'.join(path_env.split(':')[:4])}")

# 파일 경로 다루기
file_path = "/Users/username/documents/report.txt"

directory = os.path.dirname(file_path)
filename = os.path.basename(file_path)
extension = os.path.splitext(filename)[1]

print("파일 경로 정보:")
print(f"- 디렉토리: {directory}")
print(f"- 파일명: {filename}")
print(f"- 확장자: {extension}")

# 파일 존재 여부
exists = os.path.exists(file_path)
print(f"파일 존재 여부: {exists}")
