# 거북이 100마리의 리스트를 생성
# 거북이 들이 화면 중앙에 위치 -> 임의의 위치로 차례로 이동
# 선을 그리면서, 크기, 색상, 모양은 임의의 값으로 설정
# [거북이 모양, x위치, y위치, 거북이 크기, r, g, b]

import turtle
import random

myTurtle, tX, tY, tColor, tSize, tShape = [None] * 6
shapeList = []
playerTurtles = []
wWidth, wHeight = 500, 500 # 윈도우 사이즈

turtle.title("리스트를 활용한 거북이 그리기")
turtle.setup(wWidth, wHeight)
turtle.screensize(wWidth, wHeight)

shapeList = turtle.getshapes()
for i in range (1, 101) :
    random.shuffle(shapeList)
    myTurtle = turtle.Turtle(shapeList[0]) # 거북이 모양 변경
    tX = random.randrange(int(- wWidth / 2), int(wWidth / 2)) # -250 ~ 250
    tY = random.randrange(int(- wHeight / 2), int(wHeight / 2)) # -250 ~ 250
    tSize = random.randrange(1, 5) # 크기
    r = random.random(); g = random.random(); b = random.random() # 색상
    playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b])

print(playerTurtles)

for turtleList in playerTurtles :
    myTurtle = turtleList[0]
    myTurtle.color(turtleList[4], turtleList[5], turtleList[6])
    myTurtle.pencolor(turtleList[4], turtleList[5], turtleList[6])
    myTurtle.turtlesize(turtleList[3])
    myTurtle.goto(turtleList[1], turtleList[2])

turtle.done()