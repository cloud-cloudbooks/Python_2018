# Constructor(생성자) __init__

class Robot:
    '''로봇들을 만드는 클래스'''

    def __init__(self):      # 객체를 만들때마다 맨 처음 자동으로 실행되는 메소드
        self.name = 'pybot'
        self.weight = '45kg'

hubo1 = Robot()
hubo2 = Robot()
print(hubo1.name, hubo1.weight)
print(hubo2.name, hubo2.weight)

print()
hubo1.name = 'minibot'
hubo2.weight = '60kg'
print(hubo1.name, hubo1.weight)
print(hubo2.name, hubo2.weight)
