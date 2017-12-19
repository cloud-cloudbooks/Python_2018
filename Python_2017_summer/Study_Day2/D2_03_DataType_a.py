# Data Type

# Data Type이란? 파이썬에서 자주 다루는 자료 형태 7가지

# 1. 숫자 자료 (원래 컴퓨터는 숫자를 계산하기 위해 만들어짐)
#         정수형(int), 실수형(float), 복소수형(complex)

# 2. 문자열 자료 (string) - 한 글자 이상의 문자나 숫자, 기호,
#         문자열 자료 선언 방법은 2가지 : " "나 ' '
#         여러줄 문자처리 : '''과 ''', """과 """
#         문자열 안에서 다시 " " 하고 싶다면?  '' 안에 " ", 반대도 가능

# 3. 부울(bool) 참과 거짓 판단하기 위한 자료형. True/False 2개의 값만 존재한다.
#           파이썬에서 숫자 0은 False, 나머지 숫자는 True

# 4. 리스트 자료 (list) - [ ] 안에 순서 있게 나열한 자료형, 콤마(,)로 요소 구분
#          list_data = ["재인", "철수", "준표", "재용"]

# 5. 튜플 자료 (tuple) - 리스트와 비슷하지만 요소 값을 변경할 수 없다는 것이 차이점.
#
# 6. 사전 자료 (dictionary) - 키 값으로 한 쌍인, 순서가 없는 자료형, 각 요소는 콤마로 구분
#           사전자료는 순서가 없으므로 인덱스로 값을 접근할 수 없고, 키를 이용해 대응되는 값을 접근
# 7. 세트




# 1. 숫자형
int_data = 9
float_data = 3.14
complex_data = 3+7j
print(int_data)
print(float_data)
print(complex_data)

# 2. 문자열 자료 (string) - 한 글자 이상의 문자나 숫자, 기호,
#         문자열 자료 선언 방법은 2가지 : " "나 ' '

string_data = "안녕하세요" # "Hello, Python", '010-1234-5678'
print(string_data)


# 3.부울(bool) 참과 거짓 판단하기 위한 자료형. True/False 2개의 값만 존재한다.
#           A == B  같으면 참
#           A != B  다르면 참
#           A <= B A가 B보다 작거나 같으면 참
#           파이썬에서 숫자 0은 False, 나머지 숫자는 True
#

# *** Data Type을 알고싶으면 type(변수 혹은 리터럴값) 사용
# *** 형변환


