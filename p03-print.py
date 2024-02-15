print("100") # 문자열 출력

# %d : 10진수
# %x : 16진수
# %o : 8진수

print("%d" % (100 + 1))
print("요자리%d에 찍게 하고독 하는 것이" % 1000)
print("%d %d" %(500, 1000))

# %f : 실수 (소수점 6자리)
# %c : 한자리 문자
# %s : 문자열

print("%f" % 3.14)
print("%5.2f" % 3.14) # 소수점 포함한 총 출력 수 + 소수점 이하 출력 수
print("%3.2f" % 3.14)
print("%4.2f" % 3.14)
print("%20.17f" % 3.14)

print("%10d" % 100)
print("%010d" % 100)  # 빈자리가 0으로 채워짐
print("%2d" % 12345)

print("%06d" % 123) # 빈자리가 0으로 채워짐
print("%s" % "python")
print("%8s" % "python")

print("%d %5d %05d" % (123, 123, 123))
print("{0:d} {1:5d} {2:05d}".format(123, 123, 123))
print("%d%5d%05d" % (123, 123, 123))

# print() 문은 내용을 출력한 후 줄바꿈을 한다.
# 강제로 줄바꿈을 하고 싶은 경우 \n 사용
print("요렇게 하면 콘솔창에서 \\n 은 \n 줄바꿈")
print("\\t는 탭 \t 을 누른 효과")
print("글자가 \"큰따옴표\" 되는 효과")
print("글자가 \'작은따옴표\' 되는 효과")

print("\\\\\\ 역슬러시 세개 출력")

print(r"\n \t \" \\를 그대로 출력")