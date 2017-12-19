# 리턴값은 없을 수도 있고 2개 이상일 수도 있다.

def turnValue(number):
    x = number * 10
    return x

def turnSet(number):
    x = {number, number+1, number+2}
    return x

def turnTuple(number):
    return number, number-1, number-2



print(turnValue(10))
print(turnSet(10))
print(turnTuple(10))
