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

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()