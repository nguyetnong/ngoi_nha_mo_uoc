import turtle 
#vẽ ngôi nhà
turtle.bgcolor('#EDF0F4')
turtle.pensize(2)
turtle.color("blue")
turtle.begin_fill()

cnt=0
while(cnt<2):
    
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    cnt=cnt+1
turtle.end_fill()

turtle.penup()
turtle.goto(83,-150)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
cnt=0
while(cnt<2):
    
    turtle.forward(84)
    turtle.left(90)
    turtle.forward(95)
    turtle.left(90)
    cnt=cnt+1
turtle.end_fill()

turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.goto(125,83)
turtle.goto(250,0)
turtle.end_fill()
turtle.color("pink")
turtle.begin_fill()
turtle.goto(500,40)
turtle.goto(500,-110)
turtle.goto(250,-150)
turtle.end_fill()

turtle.penup()
turtle.goto(333,-78)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.goto(416,-58)
turtle.goto(416,-38)
turtle.goto(333,-58)
turtle.end_fill()


turtle.penup()
turtle.goto(250,0)
turtle.pendown()
turtle.color("orange")
turtle.begin_fill()
turtle.goto(125,83)
turtle.goto(375,123)
turtle.goto(500,40)
turtle.end_fill()

#vẽ mặt trời
turtle.penup()
turtle.goto(510,250)
turtle.pendown()

cnt=0
while (cnt<4):
    turtle.forward(50)
    turtle.goto(510,250)
    turtle.right(45)
    turtle.forward(80)
    turtle.goto(510,250)
    turtle.right(45)
    cnt=cnt+1
    
turtle.color("yellow")
turtle.begin_fill() 
turtle.goto(510,220)
turtle.circle(30)
turtle.end_fill()

turtle.penup()
turtle.goto(-150,-150)
turtle.pendown()
turtle.color("brown")
turtle.begin_fill()
cnt=0
while (cnt<2):
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(130)
    turtle.left(90)
    cnt=cnt+1
turtle.end_fill()

turtle.color("green")
turtle.begin_fill()
turtle.penup()
turtle.goto(-135,85)
turtle.pendown() 
turtle.circle(-70,steps=3)
turtle.end_fill()

turtle.penup()
turtle.goto(-135,160)
turtle.pendown()
turtle.begin_fill()
turtle.circle(-50,steps=3)
turtle.end_fill()

turtle.penup()
turtle.goto(-135,205)
turtle.pendown()
turtle.begin_fill()
turtle.circle(-30,steps=3)
turtle.end_fill()


turtle.done()
