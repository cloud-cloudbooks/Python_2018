# 객체 정보는 __str__()로

class Robot:
    '''로봇들을 만드는 클래스'''

    def __init__(self, name, build_year):
        self.maker = 'Kong'
        self.isWalking = True
        self.name = name
        self.build_year = build_year
        self.xpos = 0
        self.ypos = 0

    def move(self):
        if self.isWalking:
            self.xpos += 1
            self.ypos += 1

    def curPosition(self):
        print('현재 좌표: ({}, {})'.format(self.xpos, self.ypos))

    def __str__(self):     # 객체정보
        sentence = '이름:{}, 제조년:{}, 현재위치: ({}, {})' \
            .format(self.name, self.build_year, self.xpos, self.ypos)
        return sentence


hubo = Robot('shane', 2016)
print(hubo)
