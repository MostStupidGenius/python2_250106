# pickling.py
# 피클링이란 파이썬의 객체를 직렬화하여
# 파일로 내보낸 뒤 다른 환경, 코드에서
# 언피클링하여 파이썬 객체로 바로 사용할 수 있게 하는
# 객체 전달 방법이다.
# 주로 AI모델을 다른 코드나 환경에 전달할 때 쓰이며
# 그 외에도 커다란 데이터를 매번 읽어오는 작업의 경우
# 그 데이터의 변경이 없다면 피클링하여
# 언피클링으로 쉽고 빠르게 가져올 수 있다.
import pickle
import os

# 피클링하는 방법
def pickling(data: any, file_path: str) -> str|None:
    parent_folder_path = os.path.dirname(file_path)
    is_exist_parent_folder = os.path.exists(parent_folder_path)
    # 만약 해당 파일 경로에 이미 파일이 있다면
    if os.path.exists(file_path):
        print("이미 파일이 존재합니다. 덮어쓰기로 파일을 쓰시겠습니까?")
        answer = input("Y/N").lower() # 소문자로 바꾼다.
        # 만약 답변이 n이라면 아무 행동 없이 파일 경로 반환
        # if answer == "n": return file_path
        # -> 만약 y로 시작하지 않는 답변인 경우
        if not answer.startswith("y"): return file_path
    elif not is_exist_parent_folder:
        # os.mkdir()에 폴더 경로를 전달하면 해당 폴더를 생성한다.
        os.mkdir(parent_folder_path) # 부모 폴더를 생성
    # 오류 발생 가능성 고려
    try:
        # with open()을 통해서 만들 피클링 파일을 wb 방식으로 쓴다.
        with open(file_path, 'wb') as file:
            # 데이터를 파일에 써 내보낸다.
            pickle.dump(data, file)
    except Exception as e:
        print(e)
        return None
    finally:
        pass
    return file_path

def unpickling(file_path: str) -> any:
    data = None
    try:
        # with open을 통해서 rb 모드로 파일을 읽어온다.
        with open(file_path, 'rb') as file:
            # .load()메서드에 file객체를 전달하면
            data = pickle.load(file)
            # 데이터를 받을 수 있다.
    except Exception as e:
        print(e)
        return None
    finally:
        pass
    return data

if __name__ == "__main__":
    data = {
        "name" : "홍길동",
        "age" : 30,
        "gender": "M"
    }
    file_path = pickling(data, "./g/test.pkl")
    # data = unpickling(file_path)
    # print(data)