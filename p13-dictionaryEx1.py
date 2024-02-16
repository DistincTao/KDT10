import operator


# 딕셔너리 생성
dict1 = {1:'a', 2:'b', 3:'c'}
print(dict1)

student1 = {'학번' : 240001, '이름' : '피터', '나이' :  20}
print(student1)

# 생성된 딕셔너리에 키와 값을 추가
student1['연락처'] = '010-1234-5678'
print(student1)

#키로 값을 찾는 방법
print(student1['학번'])
print(student1.get('이름'))
# print(student1['주소']) # 존재하지 않는 키에 대하여 KeyError 발생

# student1 딕셔너리가 가지고 있는 모든 key 값을 가져오기
print(student1.keys())

# 키를 리스트로 전환
print(list(student1.keys()))
keys = list(student1.keys())
print(keys)

# student1 딕셔너리가 가지고 있는 모든 value 값을 가져오기
print(student1.values())
values = list(student1.values())
print(values)

# student1 딕셔너리의 모든 값을 tuple 형태로 반환
print(student1.items())
items = list(student1.items())
print(items)

# dictionary에 해당 Key가 있는지 여부 검사
print('이름' in student1) # True
print('주소' in student1) # False

if '주소' in student1 :
    print(student1['주소'])
else :
    print("주소가 없습니다.")


# student1에 있는 모든 Key와 value를 출력
for i in student1.keys() :
    print('%s : %s' %(i, student1[i]))

# 
trainDic = {'Thomas' : '토마스', 'Edward' : '에드워드', 'Henry' : '헨리', 'Gothen' : '고든', 'James' : '제임스'}

print(trainDic.values())
print(sorted(trainDic.values()))

print(trainDic.items())
sortedTrainList = sorted(trainDic.items(), key=operator.itemgetter(0)) # key 값으로 오름차순 정렬
print(sortedTrainList)

sortedTrainList = sorted(trainDic.items(), key=operator.itemgetter(1)) # value 값으로 오름차순 정렬
print(sortedTrainList)

sortedTrainList = sorted(trainDic.items(), key=operator.itemgetter(1), reverse=True) # value 값으로 내림차순 정렬
print(sortedTrainList)