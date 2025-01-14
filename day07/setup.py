# exe_parctice.py
# pyinstaller를 이용한 독립 실행형 파일 만들기
# 설치
# pip install pyinstaller
# 사용
# pyinstaller --noconsole --onefile GUI_pyQt5_practice.py

# cx_freeze를 이용한 독립 실행형 파일 만들기
# 설치
# pip install cx_freeze
# 사용
# python setup.py build
# setup.py
from cx_Freeze import setup, Executable

setup(
    name="TodoList",
    version="0.1",
    description="my first app",
    executables=[Executable("GUI_pyQt5_practice.py", # 파일로 내보낼 소소파일명/경로
                            base="Win32GUI") # 윈도우 운영체제면 입력
    ]
)

# Nuitka
# 파이썬 코드를 C/C++로 변환하여 컴파일 한다.
# - 높은 성능의 실행 파일 생성
# - 전체 프로그램 최적화
# - 모든 파이썬 버전 지원
# 설치
# pip install nuitka
# 실행
# nuitka --standalone --onefile script.py
# nuitka --standalone --onefile --enable-plugin=pyqt5 .\GUI_pyQt5_practice.py
# 옵션 중 --windows-console-mode='disable' 혹은 'hide'를 사용하여
#       GUI가 포함된 프로그램의 console창을 숨길 수 있다.






