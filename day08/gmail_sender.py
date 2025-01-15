# gmail_sender.py
# send_gmail.py의 함수를 활용한 GUI 툴을 만들어보자.
# tkinter GUI 라이브러리를 활용하여
# 간단한 UI로 이메일과 앱 비밀번호를 입력받아
# 체크박스: 아이디, 비밀번호 저장 -> json파일로 저장하고(email_config.json)
# 이후 json파일에서 내용 가져오기
# 프로그램 설정 파일을 만들고 이를 읽어오는 기능 추가

# 로그인 후(SMTP 서버 접속 확인)
# 이메일 제목과 이메일 내용 칸
# 내용을 채워넣고 "보내기" 버튼을 클릭하면 -> "보내시겠습니까?" 메시지 띄우기
# "예" 누르면 전송, "전송중", "전송완료" 메시지 띄우기

# 필요한 라이브러리
# 필수: os
import os
# GUI: tkinter
import tkinter as tk
# File: json
import json
# from send_email import send_email
from send_gmail import send_email
# SMTP:
import smtplib

# 기타
from tkinter import messagebox

# 이메일을 전송 GUI 클래스 생성
class GmailSenderGUI:
    def __init__(self):
        # GUI를 사용하기 위한 메인 윈도우
        self.window = tk.Tk()
        self.window.title("Gmail 전송 프로그램")
        self.window.geometry("400x600")

        # 설정 파일 이름
        self.config_file_name = "email_config.json"
        # 설정 파일이 위치할 폴더 경로
        self.config_folder_path = os.path.abspath("C://email_sender")
        # 만약 해당 폴더가 없다면
        if not os.path.exists(self.config_folder_path):
            # 폴더를 만든다.
            os.mkdir(self.config_folder_path)
        # os.path.join()은 전달된 문자열들을 하나의 폴더나 파일 경로로
        # 병합해주는 함수이다.
        self.config_file_path = os.path.join(self.config_folder_path, self.config_file_name)

        # 설정 파일 읽어오기(파일 유무에 따라 동작 다름)
        self.config = self.load_config()

        # 화면 구성하기
        self.create_widget_login()

    def create_widget_login(self):
        """
        1. 로그인 정보 입력 화면
        이메일 입력칸
        비밀번호 입력칸: 입력했을 때 *로 표시되어 그 값이 가려지게 설정
        아이디/비밀번호 저장여부 체크 박스
        로그인 버튼
        """
        self.login_widgets: list[tk.Widget] = list()
        # 이메일 입력 안내 라벨
        self.label_sender_email = tk.Label(self.window, text="보내는 사람 이메일: ")
        # 라벨을 pack 방식으로 배치
        self.label_sender_email.pack(pady=5)
        self.login_widgets.append(self.label_sender_email)

        # 이메일 입력칸 추가
        self.entry_sender_email = tk.Entry(self.window, width=40)
        # 입력칸을 pack 방식으로 배치
        self.entry_sender_email.pack()
        self.login_widgets.append(self.entry_sender_email)

        # 앱 비밀번호 입력 안내
        self.label_password = tk.Label(self.window, text="비밀번호")
        self.label_password.pack()
        self.login_widgets.append(self.label_password)
        # 앱 비밀번호 입력 칸
        # show=옵션에 전달하는 문자열내용으로 입력한 값이 표시된다.
        self.entry_password = tk.Entry(self.window, width=40, show="*")
        self.entry_password.pack()
        self.login_widgets.append(self.entry_password)

        # 저장여부를 담을 tk에 소속된 객체
        self.save_var = tk.BooleanVar()
        # 저장여부 체크 박스
        self.save_checkbox = tk.Checkbutton(
            self.window,
            text="이메일/비밀번호 저장",
            variable=self.save_var # 체크 여부에 따라 해당 변수의 값이 변화한다.
        )
        self.save_checkbox.pack(pady=10)
        self.login_widgets.append(self.save_checkbox)

        # SMTP 서버에 접속하는 트리거가 될 로그인 버튼 만들기
        self.button_login = tk.Button(self.window, text="로그인", command=self.SMTP_login)
        self.button_login.pack(pady=4)
        self.login_widgets.append(self.button_login)
        # 저장된 설정이 있다면 불러오기
        if self.config["sender_email"] or self.config["password"]:
            self.sender_email = self.config.get("sender_email", '')
            self.sender_password = self.config.get("password", '')
            self.isKeep = self.config.get("isKeep", False)
            self.save_var.set(self.isKeep)
            self.entry_sender_email.insert(0, self.sender_email)
            self.entry_password.insert(0, self.sender_password)

    def SMTP_login(self):
        # 입력한 이메일과 비밀번호를 임시로 담을 변수
        sender_email = self.entry_sender_email.get()
        sender_password = self.entry_password.get()
        # 로그인 성공 여부를 담을 변수
        result: bool = False

        # SMTP 로그인 시도
        try:
            # Gmail SMTP 서버에 연결 (Gmail 포트: 587 사용)
            server = smtplib.SMTP("smtp.gmail.com", 587)
            # TLS(Transport Layer Security) 보안 연결
            server.starttls()

            # Gmail 계정으로 로그인
            # 보내는 이메일과 앱 비밀번호를 전달하여 계정으로 로그인한다.
            server.login(sender_email, sender_password)
            messagebox.showinfo("로그인 성공", "로그인을 성공했습니다.")
            # 로그인에 성공했으므로 result의 값을 True로 바꿔준다.
            result = True
        except Exception as e:
            print(e)
        finally:
            # 이메일을 보낼 때 서버에 또다시 로그인할 것이므로
            # 여기서는 로그인 테스트만 진행한다.
            server.quit()

        # 로그인 성공 여부에 따라 코드 흐름을 다르게 한다.
        if result:
            # 성공했다면 해당 이메일과 비밀번호는 유효한 것이므로
            # 해당 정보를 self의 변수에 담아 공식적으로 사용한다.
            self.sender_email = sender_email
            self.sender_password = sender_password

            # 1. 로그인 화면에서 이메일 화면으로 넘어갈 때
            # 해야 하는 조치사항
            # 만약 아이디/비밀번호 저장 체크 박스를 체크했다면
            if self.save_var.get():
                config = {
                    "sender_email": self.sender_email, # 보내는 이메일
                    "password": self.sender_password, # 보내는 이메일 계정 앱 비밀번호
                    "isKeep": True # 이메일과 비밀번호를 파일을 통해 불러올지 여부
                }
                # 현재 설정 저장
                self.save_config(config)
            # 로그인 성공시, 이메일 화면으로 이동
            self.create_widget_sender()
            return
        else:
            # 로그인 실패시, 로그인 실패 메시지 띄우기
            messagebox.showerror("실패", "로그인 실패. 정보를 확인해주세요.")
            return

    # 로그인 페이지에서 로그인 버튼을 누르면 실행될 코드
    # + 아이디/비밀번호 저장여부에 따라 설정파일을 새로 저장
    # 기존의 위젯을 모두 지우거나 숨기고
    # 새로운 위젯을 배치
    def create_widget_sender(self):
        """
        2. 이메일 전송 화면
        - 이메일 제목칸
        - 이메일 내용칸
        - + 이미지, 영상 등 첨부파일을 추가하는 기능
        """
        # 1. 로그인 위젯 전부 제거
        if self.login_widgets:
            for widget in self.login_widgets:
                # 로그인 화면의 모든 위젯을 제거
                # .destroy()
                widget.destroy()
        
        # 2. 이메일 위젯 생성
        # 받는 이메일 주소 안내 라벨
        self.label_receiver_email = tk.Label(self.window, text="받는 사람 이메일: ")
        self.label_receiver_email.pack(pady=5)
        # 받는 이메일 주소 입력칸
        self.entry_receiver_email = tk.Entry(self.window, width=40)
        self.entry_receiver_email.pack()

        # 이메일 제목 안내 라벨
        self.label_email_subject = tk.Label(self.window, text="이메일 제목: ")
        self.label_email_subject.pack(pady=5)
        # 이메일 제목 입력칸
        self.entry_email_subject = tk.Entry(self.window, width=40)
        self.entry_email_subject.pack()

        # 이메일 내용 안내 라벨
        self.label_email_body = tk.Label(self.window, text="이메일 내용")
        self.label_email_body.pack(pady=5)
        # 이메일 내용 입력칸
        self.text_email_body = tk.Text(self.window, width=40, height=10)
        self.text_email_body.pack()

        # + 첨부파일 추가칸

        # 이메일 전송 버튼
        self.button_send = tk.Button(
            self.window,
            text="이메일 전송",
            command=self.send_email_process
        )
        self.button_send.pack()

    # 외부의 함수인 send_email을 이용하여 이메일을 보내는 로직
    def send_email_process(self):
        self.receiver_email = self.entry_receiver_email.get()
        self.email_subject = self.entry_email_subject.get()
        self.email_body = self.text_email_body.get("1.0",tk.END)
        if self.receiver_email and self.entry_email_subject and self.email_body:
            result = "성공" if send_email(
                self.sender_email,
                self.sender_password,
                self.receiver_email,
                self.email_subject,
                self.email_body
                ) else "실패"
            # 성공 여부에 따라 내용 송출
            messagebox.showinfo(f"전송 {result}", f"이메일 전송에 {result}했습니다.")
        else:
            messagebox.showwarning("경고", "필요한 정보가 입력되지 않았습니다.")

    def load_config(self) -> dict[str, str]:
        config:dict[str, str] = None
        # 설정 파일이 경로에 존재하면
        if  os.path.exists(self.config_file_path):
            with open(self.config_file_path, "r") as file:
                config = dict(json.load(file))
        # 설정 파일이 존재하지 않으면
        else:
            # 키값만 있고 vaule값은 모두 빈 문자열인 기본 설정파일 내보내기
            config = {
                "sender_email": "", # 보내는 이메일
                "password": "", # 보내는 이메일 계정 앱 비밀번호
                "isKeep": False # 이메일과 비밀번호를 파일을 통해 불러올지 여부
            }
            # with open(self.config_file_path, "w", encoding="utf-8") as file:
            #     json.dump(config, file, ensure_ascii=False, indent=4)
            self.save_config(config)
        return config
    
    # config를 전달받아 config_file_path에 그 정보를 저장하는 메서드
    def save_config(self, data: dict) -> None:
        # 그대로 저장하는 것이 아니라 
        # 암호화를 통해 파일을 여는 것만으로는 다른 사람이 볼 수 없도록
        # 보안 조치를 취해야 한다.
        # + 추가 기능 암호화
        with open(self.config_file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    gui = GmailSenderGUI()
    gui.run()
















