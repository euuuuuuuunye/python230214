# class1.py
#1)클래스 정의
class Person:
    #클래스 멤버변수
    num_person = 0
    #초기화 메서드
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 생성
p1 = Person()
p2 = Person()
print("인스턴스 객수:{0}".format(Person.num_person))

