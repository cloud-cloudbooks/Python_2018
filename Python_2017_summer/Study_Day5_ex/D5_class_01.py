class Robot:
    '''가장 단순한 형태의 클래스'''
    pass

robot1 = Robot()
robot1.name = 'Hubo 1'
robot1.weight = '45 Kg'

robot2 = Robot()
robot2.name = 'Hubo 2 '
robot2.build_year = '2011년'

print(robot1.name, '-', robot1.weight)
print(robot2.name, '-', robot2.build_year)
