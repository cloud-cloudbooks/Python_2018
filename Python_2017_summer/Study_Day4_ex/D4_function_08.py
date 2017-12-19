# 함수에 필요한 값들이 가변적이면 가변인수를 쓴다.

def select_even(*arg):
    result = []
    for num in arg:
        if num%2 == 1:
            continue
        result.append(num)
    return result

print(select_even(1, 2, 3, 4, 5, 6))

print(select_even(-16, 3, 26, 89, 36, 120))





