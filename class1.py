class Test:
  def __init__(self, name):
      self.name = name
      print("{}-생성되었습니다".format(self.name))
  def __del__(self):
      print("{}-소멸되었습니다".format(self.name))

a = Test("A")
b = Test("B")
c = Test("C")

print("프로그램이 종료되는 시점")