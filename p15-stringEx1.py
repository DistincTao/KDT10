str = '우리나라 대한민국'
print(str)
print(str[1:3])
print(str + " 최고")
print(str * 3)
print(len(str))

# str[2] = '너'

# 문자열 관련 함수
str1 = "Python is Best programming Language"
print(str1.upper()) # 대문자로 변환
print(str1.lower()) # 소문자로 변환
print(str1.swapcase()) # 대소문자 전환
print(str1.title()) # 첫글자를 대문자

str2 = 'Python is very simple. 정말로? Python이 그래?'
print(str2.count('Python'))

print(str2.find("Python")) # 앞에서부터 찾은 첫 인덱스 번호 indexOf
print(str2.rfind("Python")) # 뒤에서부터 찾은 첫 인덱스 번호 lasrIndexOf
print(str2.index("is")) # 앞에서부터 찾은 첫 인덱스 번호 indexOf

print(str2.find("good")) # 찾는 단어가 없을 경우 -1 반환
# print(str2.index("good")) # 찾는 단어가 없을 경우 Error 발생

print(str2.startswith("Python")) # 해당 단어로 시작하는지 확인후 T/F 반환
print(str2.startswith("very"))

print(str2.endswith("정말")) # 해당 단어로 끝나는지 확인후 T/F 반환

str3 = "     파     이     썬     "
print("[", str3.strip(), "]") # 앞뒤 공백 제거
print("[", str3.rstrip(), "]") # 뒤에 공백 제거
print("[", str3.lstrip(), "]") # 앞에 공백 제거
print("[", str3.replace(" ", ""), "]") # 모든 공백을 변경을 통하여 제거

str4 = "하나:둘:셋:넷"
print(str4) 
print(str4.split(":")) # :로 나누어서 리스트로 반환

before =['2024', '0', '16']
after = list(map(int, before)) # 해당 타입으로 변환하여 리스트로 반환
print(before)
print(after)

print('1234'.isdigit()) # True : 숫자로 이우러진 문자열인지 확인
print('가나다라'.isdigit()) # False
print('가나다라'.isalpha()) # False
print('abcd'.isalpha()) # False
print('abcd'.islower()) # False
print('     '.isspace()) # False
print('a1b2c3'.isalnum()) # False
