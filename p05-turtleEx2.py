import turtle
import random

# 마우스 왼쪽 버튼 클릭 시 수행
def screenLeftClick(x, y) :
    global r, g, b # 함수 외부에서 선언한 r, g, b 변수를 내부에서도 사용 하겠다는 의미

    turtle.pencolor(r, g, b)
    turtle.pendown()
    turtle.goto(x, y) # x, y 좌표로 꼬북이를 이동 시킴

# 마우스 오른쪽 버튼 클릭 시 수행
def screenRightClick (x, y) :

    turtle.penup()
    turtle.goto(x, y)


# 마누스 가운데 버튼 클릭 시 수행
def screenMidClick(x, y) :
    global r, g, b, pSize

    r = random.random()
    g = random.random()
    b = random.random()
    
    pSize = random.randrange(1, 10) # 선 굵기 크기를 1 ~ 9 까지 난수로 설정

    turtle.pensize(pSize)

pSize = 7
r, g, b = 0.0, 0.0, 0.0

turtle.title("거북이로 그림 그리기")
turtle.shape("turtle")
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1) # 마우스 왼쪽버튼 클릭 되면 수행할 함수 설정 (1)
turtle.onscreenclick(screenMidClick, 2) # 마우스 가운데 (휠) 버튼 클릭 되면 수행할 함수 설정 (2)
turtle.onscreenclick(screenRightClick, 3) # 마우스 오른쪽 버튼 클릭 되면 수행할 함수 설정 (3)

turtle.done()