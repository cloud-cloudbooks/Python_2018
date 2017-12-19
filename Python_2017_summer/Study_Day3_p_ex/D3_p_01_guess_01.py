# 숫자를 추측해서 맞추는 프로그램


n = 5

while True:                   # 영원히 반복
    x = input("10이하의 숫자에서 맞혀보세요")
    g = int(x)               # 입력받은 값을 비교할 수 있도록 정수로
    if g == n:               # 사용자가 추측한 값과 임의의 수가 같으면 정답.
        print("정답")
        break                # 정답을 맞추면 break로 while 반복 블록을 빠져나감
    if g < n:
        print("너무 작아요.")
    if g > n:
        print("너무 커요.")