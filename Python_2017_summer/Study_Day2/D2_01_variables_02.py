# (변할 수 있는 정보라고 하는 게 더 적당, 변수는 단지 이름에 불과하다. - 포스트잇)

# 컴퓨터가 프로그램을 만드는데 필요한 숫자를 저장하거나
# 여러가지 연산 결과를 보관했다가 다시 찾아보려면 정보를 보관하는 공간이 필요하다

# 변수는 변할 수 있는 수이므로, 필요에 따라 몇번이라도 저장된 값을 바꿀수 있다.
# =은 할당한다는 말, '같다'가 아님. 오른쪽의 값을 먼저 계산한 후 왼쪽에 할당한다는 의미
# 변수를 사용하지 않는 프로그램은 거의 없다.

# 변수를 선언하지 않으면 어떻게 될까?
# (5를 넣기 위해 a라는 그릇이 필요하다는 뜻..
# a 선언하지 않고 a에 5를 넣으라고 하면 컴퓨터가 일을 할 수 없으므로 오류)

# 변수이름에는 다음의 문자만 사용할 수 있다.
#  소문자(a~z), 대문자(a~z), 숫자(0~9), 언더스코어(_):대소문자 구분,
#  이름은 숫자로 시작할 수 없다. 사이에 공백이 있으면 안된다.
#  변수명은 이름을 보고 짐작할 수 있도록 만든다.
#  사용할 수 있는 유효한 이름 : a, a1, a_b_c__97, _abc, _1a
#  사용할 수 없는 이름 : 1, 1a, 1_
#  그 외에 파이썬의 예약어(reserved word, 파이썬에서 이미 다른 목적으로 사용하는 단어)는 안된다
#  : False, True, finally, is, return, None, continue, lambda, try, class, def,
#    from, while, and, nonlocal, del, global, not, with, as, elif, if, or, yield,
#    assert, else, import, pass, break, except, in, raise
#  위의 예약어를 굳이 변수명으로 사용하면 어떻게 될까?
#   ex)   and = 1
#         SyntaxError : invalid syntax

# 바람직한 변수명 : sum, next_value, maxAge, score 등등

name = "Jane"
print(name)


a = 5
print(a)

b = 3.4 + 2
print(b)

c = a + b
print(c)

d = 6
d = d+1
print(d)

# 기억해두자.. d = d +1 는 d에 저장된 값에  1을 더하여 다시 d에 저장하라는 문장이다.
#즉, d = d + 1은 '변수 d의 값을 1씩 증가시켜주세요'라는 의미














