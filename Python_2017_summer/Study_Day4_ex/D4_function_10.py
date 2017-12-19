x# 전역변수 지역변수
global_variables = '전역변수' #프로그램 전체에서 사용가능한 변수, 블록 밖에서 만들어야.

def scope():
    local_variables = '지역변수'#한정된 영역에서만 사용, 함수블록 내에서 클래스 블록 내에서 만듬
    print(global_variables)
    print(local_variables)


scope()  # scope() 함수 실행

print()
print(global_variables)
# print(local_variables)




