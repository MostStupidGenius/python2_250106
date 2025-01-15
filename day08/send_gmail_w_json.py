# send_gmail_w_json.py
# send_gmail.py에 작성된 메일 보내기 함수를 json에 담긴 값을 활용하여
# 미리 설정된 형태로 이메일 전송하기
from send_gmail import send_email
import json

if __name__ == "__main__":
    # json 파일 읽어오기
    with open("day08/gmail_info.json", 'r') as file:
        data = json.load(file)
    # json에 담긴 데이터는 dict 자료구조와 동일하기 때문에
    # 파이썬에서 다루기 위해 dict 자료구조로 변환한다.
    data = dict(data)
    print(data["sender_email"])
    print(data["password"])
    # 받는 이메일을 저장할 변수 선언
    receiver_email = None
    # 제대로된 입력을 받기 위한 반복문
    while(not receiver_email):
        # 빈문자열을 입력한 경우 입력을 다시 받는다.
        receiver_email = input("받을 이메일을 입력해주세요: ")
        # + 입력받은 이메일의 형식을 검사하여
        # 유효한 이메일이 아니면 재입력받기
    
    subject = input("이메일 제목: ")
    body = input("이메일 내용: ")

    # 전송 시작 안내 메시지
    print("이메일 전송을 시작합니다.")
    send_email(data["sender_email"], data["password"],
               receiver_email, subject, body)
