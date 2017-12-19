#입력이 있고 출력도 있는 함수

def abs(number):
    # number는 매개변수, -5를 number에 전달하면 number가 대신 함수안에서 일한다.
    if number < 0:
        number = -number
    return number    # return은 값 반환, 종료

print('-3의 절대값 구하기:', abs(-3))
print('10의 절대값 구하기:', abs(10))
print()
temp = abs(-9)/3 * abs(20) + 3 + abs(-19)
print('계산 결과:', temp)


