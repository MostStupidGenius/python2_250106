# GUI_pyQt5_practice.py
# pyQt5를 활용한 어플리케이션 만들기
# 기획:
# 최상단엔 텍스트 라인과 "입력" 버튼 배치
# 하단에는 입력한 할일 목록이 띄워지도록 리스트 위젯 사용
# 할일 목록 아래에 삭제/완료 버튼 -> 선택할 할일을 없앨 수 있게
# 필요한 라이브러리 임포트
import sys
from PyQt5.QtWidgets import * # PyQt5의 모든 위젯 임포트
from PyQt5.QtCore import Qt   # Qt 코어 기능 임포트

# TodoList 클래스 정의
# QMainWindow를 상속받음
class TodoList(QMainWindow):
    def __int__(self):
        print("line 16")
        # super().__init__()  # 부모 클래스 초기화
        print("asd1")
        self.initUI()       # UI 초기화 메서드
        print("asd2")
    
    def initUI(self):
        # 중앙 위젯 생성
        self.central_widget = QWidget()
        # 설정
        self.setCentralWidget(self.central_widget)

        # 메인 수직 레이아웃 구성
        self.main_layout = QVBoxLayout(self.central_widget)

        # 입력 부분을 위한 수평 레이아웃 구성
        self.input_layout = QHBoxLayout()

        # 할일 입력을 위한 텍스트 입력창 구성
        self.task_input = QLineEdit()
        # 텍스트 입력창에 플레이스 폴더 적용
        # place holder란 어떤 값을 입력해야 하는지
        # 값을 입력하지 않았을 때 반투명한 글자로 보여주는 것으로
        # 입력을 시작하면 사라진다.
        self.task_input.setPlaceholderText("할일을 입력하세요")

        # 할일을 추가하는 "추가"버튼 생성
        self.add_button = QPushButton(text="추가")
        # "추가" 버튼에 대한 이벤트 연결
        # 버튼 클릭시 add_task 메서드 호출
        self.add_button.clicked.connect(self.add_task)

        # 버튼을 레이아웃에 추가
        self.input_layout.addWidget(self.task_input)
        self.input_layout.addWidget(self.add_button)

        # 할일 목록을 표시할 리스트 위젯 생성
        self.task_list = QListWidget()

        # 삭제 버튼 생성
        self.delete_button = QPushButton("체크된 항목 삭제")
        # 클릭시 이벤트 연결
        self.delete_button.clicked.connect(self.delete_task)

        # 모든 요소를 레이아웃에 추가
        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addWidget(self.task_list)
        self.main_layout.addWidget(self.delete_button)

        # 메인 윈도우 설정
        self.setWindowTitle("Todo List")
        self.setGeometry(300, 300, 400, 500)

        # self.
    # 삭제 버튼 클릭시 실행할 메서드
    def delete_task(self):
        # 삭제할 항목들을 저장할 리스트 선언
        items_to_remove = []
        # 모든 항목을 순회하면서 체크된 항목 찾기
        for i in range(self.task_list.count()):
            # i번째 값을 가져온다.
            item = self.task_list.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                items_to_remove.append(item)

        for item in items_to_remove:
            self.task_list.takeItem(self.task_list.row(item))

    # 추가 버튼 클릭시 실행할 메서드
    def add_task(self):
        # 입력창에서 텍스트 가져오기
        task = self.task_input.text()
        # 텍스트가 비어있지 않다면
        if task:
            # 새로운 할일 항목 생성
            item = QListWidgetItem(task)
        # + 체크박스
        item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        # 초기 상태 체크 해제
        item.setCheckState(Qt.CheckState.Unchecked)

        # 리스트에 항목 추가
        self.task_list.addItem(item)
        # 입력창 비우기
        self.task_input.clear()


# 메인 실행 부분
if __name__ == "__main__":
    app = QApplication(sys.argv)
    print("Line92")
    todo_list = TodoList()
    # todo_list.
    todo_list.show() # 윈도우 표시
    sys.exit(app.exec_()) # 이벤트 루프 시작
