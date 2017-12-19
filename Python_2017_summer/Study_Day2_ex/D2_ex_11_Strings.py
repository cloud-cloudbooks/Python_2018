# 문자열 포맷팅
#값이 변하는 문자열을  %기호 사용
# %s는 문자열, %d는 숫자,

txt1 = '영어';txt2='파이썬'
num1= 5; num2=10
print('나는 %s보다 %s에 더 익숙합니다.' %(txt1, txt2))
print('%s은 %s보다 %d배 더 쉽습니다.' %(txt2, txt1, num1))
print('%d + %d = %d' %(num1, num2, num1+num2))
print('작년 세계 경제 성장률은 전년에 비해 %d%% 포인트 증가했다.' %num1)
