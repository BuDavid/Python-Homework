from typing import Union

class StudentList:
    LOWEST_SCORE = 0
    HIGHEST_SCORE = 100

    def __init__(self):
        self.dic = {}

    def add_student(self, name: str, score: Union[int, None] = None) -> None:
        if name not in self.dic:
            self.dic[name] = score if self.is_valid(score) else None

    def change_score(self, name: str, score: int) -> None:
        if name in self.dic:
            self.dic[name] = score if self.is_valid(score) else None

    def reset_score(self, name: str) -> None:
        if name in self.dic:
            self.dic[name] = None

    def remove_student(self, name: str) -> None:
        if name in self.dic:
            del self.dic[name]

    def print_list(self) -> None:
        for key, value in self.dic.items():
            print(f"{key}: {value}")

    def clear(self) -> None:
        self.dic.clear()

    def __len__(self) -> int:
        return len(self.dic)

    def is_valid(self, score: Union[int, None]) -> bool:
        if score is None or score < self.LOWEST_SCORE or score > self.HIGHEST_SCORE:
            return False
        return True

