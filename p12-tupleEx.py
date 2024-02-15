# tuple 생성 (읽기 전용)
tuple1 = (10, 20, 30, 40, 50)
print(tuple1)
# tuple1.append(50)
# tuple1[0] = 100


# Tuple의 요소에 접근 - 리스트 처럼 Tuple명 [위치]
print(tuple1[0])
print(tuple1[1 : 3])

tuple2 = 1, 2, 3, 4, 5
print(tuple2)

# tuple의 덧셈, 곱셈

tuple3 = tuple1 + tuple2
print(tuple3)
print(tuple1 * 3)

# 항목이 하나인 튜플 생성 : 쉼포를 찍어 주도록 한다.
tuple4 = (10,)
print(tuple4)

tuple4 = 10,
print(tuple4)

# tuple 삭제
# del(tuple1)
# print(tuple1)

myList = list(tuple1) # tuple을 list로 변환
print(myList)

list2 = [100, 200, 300]
myTuple = tuple(list2) # list를 tuple로 바꿔 새로운 tuple 반환
print(myTuple)