class Robot:
    name = '휴보'
    weight = 45

    def speak(self):
        print('안녕하세요. 휴보입니다.')

    def move(self):
        print('휴보가 움직인다.')

    def dance(self):
        print("휴보가 춤을 춥니다")

    def sing(self):
        print("휴보가 노래를 합니다.")

robot1 = Robot()    # robot1은 Robot의 객체, Robot 클래스의 인스턴스
robot2 = Robot()
robot3 = Robot()

# print(type(robot1))
robot2.speak()
robot3.move()
robot1.sing()
robot3.dance()
