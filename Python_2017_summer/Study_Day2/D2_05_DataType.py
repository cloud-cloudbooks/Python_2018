# indexing,
string = "NATURE"

print(string[0])
print(string[1])
print(string[5])

print(string[-1])
print(string[-2])
print(string[-6])


#  slicing
string = "NATURE"
print("-" * 5 + "정방향" + "-" * 5)
print(string[0:5])
print(string[2:4])
print(string[2:])
print(string[:3])

print("-" * 5 + "역방향" + "-" * 5)
print(string[-4:-2])
print(string[-6:])
print(string[:-3])

# 문자열을 위한 메서드

myStr = 'Hello, My little baby'
print(myStr.upper())
print(myStr.lower())
print(myStr.title())

print(myStr.count('b'))
print(myStr.endswith('y'))
print(myStr.startswith('h'))

myStrlist1 = myStr.split()
print(myStrlist1)             # 공백이 기준이 됨
myStrlist2 = myStr.split(',') #,가 기준이 됨
print(myStrlist2)
print()

# 리스트 변경하기

cheeses = ['체다', '모짜렐라', '까망베르', '리코타']
print(cheeses)

cheeses[0] = '크림'
print(cheeses)

all = cheeses + ['블루']
print(all)
print(cheeses)

# 리스트 슬라이싱

bucket = ['세계일주', '악기 하나 배우기', '누군가의 후원자되기',
          '베스트셀러 작가']
print(bucket)

done = bucket[1:3]
print(done)

print(bucket[0:4])

# 리스트 관련 메서드

colors = ['red', 'orange', 'yellow']
print(colors)

print('red의 위치:', colors.index('red')) # 위치 가져오기
print('orange의 위치:', colors.index('orange'))
print()

colors.append('purple')             # 항목 추가하기1
print(colors)

colors.insert(3, 'green')            # 항목 추가하기2
print(colors)

colors.extend(['black', 'white'])   # 항목 추가하기3
print(colors)

# sort, reverse, pop, remove, count

colors = ['red', 'orange', 'yellow', 'green', 'yellow']
print(colors)

colors.sort()                       # 항목 정렬하기
print(colors)

colors.reverse()                    # 역순 정렬하기
print(colors)
print()

print(colors.pop())                 # 항목 가져오기
print(colors)

colors.remove('red')             # 항목 삭제하기
print(colors)

print(colors.count('yellow'))       # 항목 개수 세기

# 튜플 멤버십 테스트
print('yellow' in colors)
print('red' in colors)
print('red' not in colors)

# 형변환
#숫자와 문자열 사이의 형변환 / 리스트와 튜플 사이에 형변환

my_number = int('5')
print(type(my_number))

your_list = ['개', '고양이', '도마뱀']
your_tuple = tuple(your_list)
print(type(your_tuple))