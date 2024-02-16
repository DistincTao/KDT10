import operator

# 기차 이름별로 수송량을 합산
# 순위를 결정 (1, 2, 2, 4)

trainTupleList = [('토마스', 5), ('헨리', 8), ('에드워드', 9), ('에밀리', 5), ('토마스', 4),
                ('헨리', 7), ('토마스', 3), ('에밀리', 8), ('퍼시', 5), ('고든', 13)]

trainDic = {}
rank, curRank = 1, 1

for trainTuple in trainTupleList :
    trainName = trainTuple[0] # 기차의 이름
    trainWeight = trainTuple[1] # 기차의 수송량

    if trainName in trainDic : # 기차이름이 딕셔너리에 있다면
        trainDic[trainName] += trainWeight # 수송량 누적
    else : 
        trainDic[trainName] = trainWeight

trainSortedList = sorted(trainDic.items(), key=operator.itemgetter(1), reverse=True)
print(trainSortedList)
print('기차 이름 \t 총 수송량 \t 순위')
print("%5s" % trainSortedList[0][0], '\t', "%8d" %trainSortedList[0][1], '\t', curRank)

for i in range(1, len(trainSortedList)) :
    rank += 1
    if (trainSortedList[i][1] == trainSortedList[i - 1][1]) :
    # i번째 기차의 수송량이 i-1 번째 기차의 수송량과 같다면
        pass
    else :
        curRank = rank
    print("%5s" % trainSortedList[i][0], '\t', "%8d" %trainSortedList[i][1], '\t', curRank)
    