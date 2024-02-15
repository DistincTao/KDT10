
# 단순 for 문
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print("%d" % i)

for i in range(1, 6) :
    print("%d" % i, end=" ")

print()

# 1부터 10까지 합
sum = 0

for i in range(1, 11) :
    sum += i
print("1부터 10까지의 합 : %d" % sum)

# 1부터 10사이의 홀수의 합
oddSum = 0
for i in range(1, 11, 2) :
    oddSum += i
print ("1부터 10사이의 홀수의 합 : %d" % oddSum)


# 501부터 1000사이의 홀수의 합

oddSum1 = 0

for i in range(501, 1001, 2) :
    oddSum1 += i
print ("501부터 1000사이의 홀수의 합 : %d" % oddSum1)

# 중첩 for문
for i in range (2, 10) :
    for j in range (1, 10) :
        print ("%d X %d = %2d \t" % (i, j, (i * j)), end = " ")
    print()

for i in range (1, 10) :
    output = ""
    for j in range (2, 10) :
        output += str("%d X %d = %2d \t" % (j, i, (i * j)))
    print(output)
print()

# while
i = 0
while i < 3 :
    print("%d : python while statement " % i)
    i += 1

j = 0
while True :
    print("Hello %d" % j)
    j = j + 1
    if (j == 4) :
        break

#


# 1에서 100까지 합계를 구하되, 3의 배수는 제외

sum3 = 0
for i in range(1, 101) :
    if i % 3 == 0 :
        continue
    sum3 += i

print("1에서 100까지 합계 (3의 배수는 제외) : %d" % sum3)