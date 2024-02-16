# list (리스트) : 타 프로그래밍 언어에서 배열과 같은 구조의 데이터 타입  (가변 배엵)
# 배열의 생성 : 리스트명 = [값1, 값2, 값3, ....., 값n]
list1 = [0, 0, 0, 0]

sum = 0
list1[0] = 45
list1[1] = 33
list1[2] = 55
list1[3] = 100
list1.append(100)
print(list1)
sum = list1[0] + list1[1] + list1[2] + list1[3] + list1[4]
print("list1의 합 : ", sum)
print("list의 최대값, 최대값의 인덱스 : ", max(list1), list1.index(max(list1)))

list2 = [] # 빈 리스트 생성
list2.append(2)
list2.append(3)
print(list2)

list3 = []
for i in range (1, 6) :
    list3.append(i)
print(list3)

aa = [10, 20, 30]
bb = [40, 50, 60]
print(aa + bb) 
print(aa * 3)


cc = []
for i in range (0, 10) :
    cc.append(i)

print(cc)
print(cc[0 : 3])
print(cc[:: 2]) # 앞에서부터 두칸씩 건너 뜀
print(cc[:: -2]) # 뒤에서부터 두칸씩 건너 뜀
print(cc[:: -1]) # 뒤에서부터 추출

# 리스트의 값 변경
cc[1 : 2] = [20, 21]
print(cc)

cc[1 : 4] = [20, 21]
print(cc)

print("=================================================")
#파이썬의 list는 모든 데이터 타입을 다 원소로 가질 수 있다.
list4 = [10, 20, 3.14, '파이썬', False]
print(list4)
# print(list4[5])

list5 = [10, 20, 30, 40, 50]
print(list5[-1])
print(list5[2:4])
print(list5[:3])
print(list5[3:])
print(list5[-2:-4]) # [] 출력 => 음수 index를 붙이면 시작 위치부터 정방향으로 탐색을 하기 때문
print(list5[-3:-1])

# 2차원 배열처럼 사용
list6 = [100, 200]
list6[1] = [20, 30]
print(list6)

#list 조작함수
myList = [30, 20, 10]
print("현재 리스트 : %s" %myList)

print("--- 리스트에 append 로 추가---")
myList.append(40)
print("현재 리스트 : %s" %myList)

print("--- 리스트에 pop()으로 꺼내기 : %s" %myList.pop())
print("현재 리스트 : %s" %myList)

print("--- 리스트에 pop(1)로 꺼내기 : %s" %myList.pop(1))
print("현재 리스트 : %s" %myList)

myList.append(20)
print("현재 리스트 : %s" %myList)

# sorted로 정렬된 배열 복사
print(sorted(myList))
print("현재 리스트 : %s" %myList)

# sort 적용 후
myList.sort()
print("현재 리스트 : %s" %myList)

print("mylist에서 20의 위치 : %d" %myList.index(20))

# reverse 적용 후
myList.reverse()
print("reverse() 후 리스트 : %s" %myList)

# insert 적용 후
myList.insert(2, 200)
print("insert() 후 리스트 : %s" %myList)

# remove 적용 후
myList.remove(20)
print("remove(20) 후 리스트 : %s" %myList)

# extend 적용 후
myList.extend([1000, 2000, 3000])
print("extend([1000, 2000, 3000]) 후 리스트 : %s" %myList)

print("myList의 요소 갯수 : %d" %len(myList))
print("myList에서 10의 갯수 : %d" %myList.count(10))