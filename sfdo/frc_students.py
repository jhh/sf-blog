import csv
from dataclasses import dataclass, field
from pathlib import Path

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Student:
    first_name: str
    last_initial: str
    school: str
    grade: int
    team: str
    quote: str
    name: str = field(init=False)

    def __post_init__(self):
        self.name = f"{self.first_name} {self.last_initial}"

    @staticmethod
    def from_row(row: list[str]):
        return Student(row[5], row[8], row[24], int(row[25]), row[26], row[27])


class FrcStudents:
    def __init__(self):
        self.csv_file = Path("/Users/jeff/Desktop/frc.csv")

    def render(self):
        students: list[Student] = []
        with open(self.csv_file, newline="") as csv_file:
            student_reader = csv.reader(csv_file)
            for row in student_reader:
                students.append(Student.from_row(row))
        print(Student.schema().dumps(students, many=True, indent="  "))


def main() -> None:
    app = FrcStudents()
    app.render()


if __name__ == "__main__":
    main()
