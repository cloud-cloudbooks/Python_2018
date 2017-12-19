# Data Structure

# 4. 리스트 자료 (list) - [ ] 안에 순서 있게 나열한 자료형, 콤마(,)로 요소 구분
list_data = ["재인", "철수", "준표", "재용", "도널드 트럼프"]
#              0        1       2        3        4
list_data2 = ["재인", 25, [1, 2, 3, 4], ['재인', '철수']]

print(list_data)
print(list_data[0])
print(list_data[1])
print(list_data[2])
print(list_data[3])
print(list_data[4][2]) #리스트[4]번째의 [2]번째 위치
print(list_data[1:3])
print(list_data[:3])


# 리스트 변경하기
list_data[2] = "우성"
print(list_data)


print(list_data2[:1])
print(list_data2[2])

#데이터 삭제
a = [1,2,3,4]
# a.remove(2)
# a.remove(a[3])
# print(a)
del a[0]
print(a)

# 5. 튜플 자료 (tuple) - 리스트와 비슷하지만 요소 값을 변경할 수 없다는 것이 차이점.
#    ( )안에 자료가 하나이면 문자열이지 튜플이 아님
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b','c')
tuple3 = (1, 'a', 'abc', [5, 6, 7, 8])
print(tuple1[3])

# 튜플 사용

myTuple = ()
myTuple = (1, 2, 3)
myTuple = (1, "python", 3.14)
myTuple = ("문자열도 넣고", (1,2,3), [4,5,6])

myTuple = 1, 2, "number"
print(myTuple)
a, b, c = myTuple
print(a, b, c)
print()

# 튜플 선언시 한 가지 유의점
myTuple = ("hello")
print(type(myTuple))  # myTuple는 문자열 변수
myTuple = ("hello", )
print(type(myTuple))  # myTuple는 튜플 변수

myTuple = (1, 2, 3)
# myTuple[0] = 10   # 오류 발생 튜플값 변경하려하면 오류 발생

# 6. 집합(set) : 중복이 없고, 순서가 없다. {}로 선언
my_set = {1, 2, 3, 3, 5, 7, 7}
print(my_set)
# print(my_set[0])  # 집합에는 순서가 없으므로 인덱싱도 안되고 슬라이싱도 안됨. 오류가 남
# set는 빈 집합을 만들려면  set={}로 하면 안된다. 그러면 dict이 만들어짐.set()로 만들어야
#section_038.py

s_nature = {'sky', 'sea'}
print(s_nature)
print()

# 항목 추가하기
s_nature.add('earth')
print(s_nature)
s_nature.update({1, 2}, [2, 3])
print(s_nature)
print()

# 항목 가져오기
print(s_nature.pop())
print(s_nature)
print(s_nature.pop())

# 항목 삭제  discard(삭제하려는 항목이 집합에 없어도 아무일 없다), remove(그러면 오류),
#           clear(집합을 깨끗하게 비우는 기능)

s_planet = {'수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성'}
print(s_planet)
print()

# 항목 삭제하기
s_planet.discard('금성')
print(s_planet)
s_planet.remove('천왕성')
print(s_planet)
#s_planet.remove('명왕성')  # 오류 발생
print()

# 항목 비우기
s_planet.clear()
print(s_planet)



# 7. 사전 (dictionary) - 키와 값이 한 쌍인, 순서가 없는 자료형, 각 요소는 콤마로 구분
#           사전자료는 순서가 없으므로 인덱스로 값을 접근할 수 없고, 키를 이용해 대응되는 값을 접근
#           dict도 { }로 선언한다. 키는 중복되면 안되고 값은 중복 가능

dict1 = {'이름':'트럼프', '나이': '70', '주소':'워싱턴'}
print(dict1)
print(type(dict1))
print(dict1['이름'])
print(dict1.get('나이'))
dict1['주소'] = '뉴욕'
print(dict1['주소'])

dict1['가족'] = '이방카'
print(dict1)

del dict1['나이']
print(dict1)

dict1.clear()  #clear와 del의 차이.. clear는 안의 것만 비운다. del은 dict1 자체 삭제
