class 학생:
  def __init__(self, name, korean, math, english, science):
    self.name = name
    self.korean = korean
    self.math = math
    self.english = english
    self.science = science
  def 총점(self):
    return self.korean + self.math +\
    self.english + self.science
  def 평균(self):
    return self.총점() / 4
  def 출력(self):
    print(self.name, self.총점(), self.평균(), sep="\t")
#----------------------------------------------------------------#
# 학생 리스트를 선업합니다.
students = [
    학생("김길동", 87, 98, 88, 95),
    학생("김길순", 92, 98, 96, 98),
    학생("이길동", 76, 96, 94, 90),
    학생("이길순", 98, 92, 96, 92),
    학생("박길동", 95, 98, 98, 98),
    학생("박길순", 64, 88, 92, 92)
]

# 학생을 한 명씩 반복합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
  student.출력()