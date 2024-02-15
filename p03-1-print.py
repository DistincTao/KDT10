numSys = int(input("진수를 입력하세요 (16, 10, 8, 2) >>> "))
inputNum = input("값 입력 >>> ")

if numSys == 16 :
    num = int(inputNum, 16)

if numSys == 10 :
    num = int(inputNum, 10)

if numSys == 8 :
    num = int(inputNum, 8)

if numSys == 2 :
    num = int(inputNum, 2)

print("16진수 : ", hex(num))
print("10진수 : ", (num))
print("8진수 : ", oct(num))
print("2진수 : ", bin(num))