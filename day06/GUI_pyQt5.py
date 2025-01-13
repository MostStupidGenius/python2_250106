# GUI_pyQt5.py
# pyQt5
# 다른 언어에서 이미 잘 쓰이고 있던 qt5 GUI 라이브러리를
# 파이썬에서 쓸 수 있게 바꾼 것으로
# 많은 기능과 세련되고 현대적인 디자인 등 여러가지 제공되는
# 자료들이 많다.
# 하지만 배워야 할 내용이 많아 초보자가 학습하기엔
# 학습곡선이 가파르고
# 소규모 프로젝트보다는 대규모 프로젝트에서 강한 면모를 보인다.
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow,\
QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel,\
QLineEdit, QTextEdit, QMessageBox

# QMainWindow를 상속받아서 이를 수정하는 것으로
# GUI 프로그래밍을 시작한다.
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("첫번째 애플리케이션")
        # self.setGeometry(x좌표, y좌표, 너비, 높이)
        self.setGeometry(300, 300, 300, 200)
        
        # 버튼을 생성
        # parent를 self로 설정
        btn = QPushButton("클릭하세요", self)
        btn.clicked.connect(self.buttonClicked)

        # 윈도우를 띄운다.
        self.show()



    def buttonClicked(self):
        print("버튼이 클릭되었습니다.")


if __name__ == "__main__":
    # 실행단계
    # 시스템에 QApplication 올리는 단계
    app = QApplication(sys.argv)
    # QMainWindow를 상속받은 앱 객체를 만드는 단계
    ex = MyApp()
    # 프로그램 종료시 종료를 알리는 단계
    sys.exit(app.exec_())