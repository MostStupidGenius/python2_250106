# send_gmail.py
# svla rozb qdxk edmd
# gmail을 SMTP(메일 보내기 프로토콜) 라이브러리를 활용하여
# 이메일을 자동으로 전송할 수 있다.
# 필요한 라이브러리 임포트
# smtplib는 기본 내장 라이브러리이기 때문에
# 설치가 필요가 없다.
import smtplib
# 이메일 내용의 텍스트를 추출하기 위한 모듈임포트
from email.mime.text import MIMEText
# 멀티미디어(영상, 사진, 음성 등)를 이메일을 통해 전송하기 위한 모듈
from email.mime.multipart import MIMEMultipart

# 이메일 전송을 위한 기본 함수 정의
def send_email(sender_email: str, sender_password: str, receiver_email, 
               subject: str, body: str):
    """
    sender_email: 보내는 사람의 이메일 주소
    sender_password: 보내는 사람의 구글 계정 앱 비밀번호(16자리)
    receiver_email: 받는 사람의 이메일 주소
    subject: 보내는 이메일 제목
    body: 보내는 이메일 내용
    """
    # MIMEMultipart 객체를 생성하여 이메일 메시지 구성
    message = MIMEMultipart()
    # 발신자 이메일 설정
    message["From"] = sender_email    
    # 수신자 이메일 설정
    message["To"] = receiver_email
    # 이메일 제목 설정
    message["Subject"] = subject

    # 이메일 본문을 일반 텍스트로 추가
    # "plain" 서브타입은 기본 형식을 의미한다.
    # 별다른 특징이 없는 텍스트를 전달한다는 의미이다.
    message.attach(MIMEText(body, "plain",))

    # SMTP 서버에 연결하여 이메일을 보내는 부분
    # 오류 발생 가능성이 있기 때문에 try-except 코드 블록을 사용한다.
    try:
        # Gmail SMTP 서버에 연결 (Gmail 포트: 587 사용)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        # TLS(Transport Layer Security) 보안 연결
        server.starttls()

        # Gmail 계정으로 로그인
        # 보내는 이메일과 앱 비밀번호를 전달하여 계정으로 로그인한다.
        server.login(sender_email, sender_password)

        # 이메일을 문자열로 변환
        text = message.as_string()
        # 변환된 문자열을 이메일로 전송
        server.sendmail(sender_email, receiver_email, text)
        print("이메일 전송 성공")
        return True

    except Exception as e:
        # 오류가 발생하면 어떤 오류인지 출력
        print(f"{e}")
        return False
    
    finally:
        # 서버 연결 종료
        # 전송 여부와 무관하게 실행
        # try 혹은 except 구문에서의 return 이후에 실행
        # 함수 코드 블록을 벗어나기 전에 실행된다.
        server.quit()
        print("연결 종료")

# 예시 코드
if __name__ == "__main__":
    # 보내는 이메일 주소
    sender_email = "miraclelee0613@gmail.com"
    # 보내는 이메일 계정 앱 비밀번호(16자리)
    password = "svla rozb qdxk edmd"
    # 받는 이메일
    receiver_email = "jslee7518@gmail.com"
    # 이메일 제목
    subject = "테스트 이메일 250115 이준상"
    # 이메일 내용
    body = "테스트 이메일 내용"

    # 이메일 전송 함수 실행
    result = send_email(sender_email, password, receiver_email, subject, body)
    print(result)
