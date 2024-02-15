a = 99

if a < 100 :
    print("100보다 작다.")
else : 
    print("100보다 작지 않다.")

if a < 100 :
    print("100보다 작다.")
elif a == 100 :
    print("100과 같다.")
else :
    print("100보다 크다.")

# 리스트와 함께 사용하는 if 문
favoriteFruit = ['수박', '귤', '참외', '포도', '딸기']

if '딸기' in favoriteFruit :
    print("딸기가 있습니다.")

if '샤인머스켓' not in favoriteFruit :
    print("샤인머스켓이 없습니다.")
