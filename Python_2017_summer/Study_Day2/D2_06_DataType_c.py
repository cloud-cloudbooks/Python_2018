# Data Type을 알고싶으면 type(변수 혹은 리터럴값) 사용
# 형변환 : 다른 형태의 자료로 변환하는 것
# int, float, str, list, tuple, set, dict
#
#
# 문자열 연산

print("=" * 40)
print("Python은" + " 훌륭한 프로그래밍 언어이다")

head = "Python은"
tail = " 훌륭한 프로그래밍 언어이다"
string = head + tail
print(string)

str1 = "꿈"
str2 = "과"
str3 = "도"
str4 = "전"
print(str1 + str2 + " " + str3 + str4)

print("=" * 40)

#형식문자열


print('%s, %s'  % ('하나','둘'))
print('%d, %d, %d' % (1, 2, 3))
print()

print('작품번호: %5d, 작품선호도: %6.2f' % (365, 9.228))
print('작품번호: %5d, 작품선호도: %6.2f' % (468, 8.124))
print()

print('체질량지수(BMI)를 계산해 보아요')

weight = int(input('체중을 입력하세요: '))
height = float(input('키를 입력하세요: '))
bmi = weight/(height*height)
comment = 'BMI는 %d/(%.2f * %.2f)이므로 %6.2f이다.'

print(comment % (weight, height, height, bmi))





















