# return 없이 매개변수만 있는 함수

def signGood(when):
    if when == 1:
        print('Good Morning')
    elif when == 2:
        print('Good Afternoon')
    elif when == 3:
        print('Good Evening')
    else:
        print('Good Night')

signGood(1)
signGood(3)
signGood(10)
