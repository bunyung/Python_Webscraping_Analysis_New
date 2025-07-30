# email_parser.py

# 사용자로부터 이메일 주소 입력 받기
email = input("이메일 주소를 입력하세요: ")

# '@' 기호를 기준으로 분리
if '@' in email:
    username, domain = email.split('@', 1)
    print(f"사용자명: {username}")
    print(f"도메인: {domain}")
else:
    print("유효한 이메일 주소가 아닙니다.")
