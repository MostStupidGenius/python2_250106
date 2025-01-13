# GUI_tkinter.py
# tkinter
# 기초적인 GUI 프로그래밍 라이브러리
# GUI 라이브러리를 다루기 위한 기초 지식 습득
# 설치가 필요없는 기본 내장 GUI 라이브러리이다.

import tkinter as tk
from tkinter import messagebox

# 메인 윈도우  생성
root = tk.Tk()
# tkinter는 root를 기반으로 위젯이나 여러 GUI 객체를
# 추가하는 방식으로 동작한다.
# 메인 윈도우 제목 설정
root.title("Tkinter 예제")
# 윈도우 크기 설정
width, height = 300, 200
# root.geometry(f"300x200") # 가로x세로 (px)
root.geometry(f"{width}x{height}") # 가로x세로 (px)

# 라벨 위젯 생성
label = tk.Label(root, text="Hello world") # "root에 라벨을 추가한다"

# 라벨 위젯 패킹
# 어떤 방식으로 대상을 배치할 것인지
label.pack(pady=10) # 다른 요소와 위아래로 얼마나 사이 공간을 둘 것인가

# 엔트리 위젯 생성
# 엔트리 위젯: 입력을 받기 위한 텍스트 박스
entry = tk.Entry(root, width=20)
entry.pack(pady=5)

# 버튼 클릭 시 동작할 행동 정의
def button_click():
    name = entry.get()
    if name:
        messagebox.showinfo("환영", f"{name}님, 환영합니다.")
    else:
        messagebox.showwarning("경고", "이름을 입력해주세요")

# 버튼 위젯 생성
button = tk.Button(root, 
                text="클릭하세요",
                command=button_click, bg="lightblue",
                fg="navy"
                )
button.pack(pady=5)

# 메인 루프 실행
# 프로그램이 동작하는 건 종료하기 전까지이므로
# 종료 전까지 프로그램은 무한 루프로 동작되어야 한다.
root.mainloop()