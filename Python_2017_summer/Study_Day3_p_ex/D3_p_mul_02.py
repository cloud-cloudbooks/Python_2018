m = int(input("출력하고 싶은 구구단 단수를 입력하세요 :"))

while m<1 or m>9 :
    m = int(input("출력할 수 없어요. 숫자를 다시 입력하세요 :  "))
for x in range(1, 10):
    print (x, "x", m, "=", x*m )