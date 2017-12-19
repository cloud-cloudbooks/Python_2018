# 시퀀스형 자료
# string, list, tuple

# slicing (시퀀스에서 일정 부분 가져오는 것)

strdata = 'Time is money!!'
print(strdata[1:5])   # ‘ime’가 출력됨
print(strdata[:7])    # ‘Time is’가 출력됨
print(strdata[9:])    # ‘oney!!’가 출력됨
print(strdata[:-3])   # ‘Time is mone’이 출력됨
print(strdata[-3:])   # ‘y!!’이 출력됨
print(strdata[:])    # ‘Time is money!!’가 출력됨
print(strdata[::2])  # ‘Tm smny!’가 출력됨
print(strdata[::3])

# 문자열, 리스트 데이터 indexing
strdata = 'Time is money!!'
listdata = [1, 2, [1, 2, 3]]
print(strdata[5])     # ‘i'가 출력됨
print(strdata[-2])    # ‘!’가 출력됨
print(listdata[0])     # 1이 출력됨
print(listdata[-1])    # [1, 2, 3]이 출력됨
print(listdata[2][-1])  # 3이 출력됨

