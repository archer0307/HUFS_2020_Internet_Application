import turtle

turtle.setup(width=1920,height=1061)
turtle.speed(2)
#turtle.hideturtle()
turtle.pensize(3) #색은 RGB 16진수 코드로 찾았으나, 두께를 구하지 못함.
turtle.pencolor("#FF69B4")
turtle.fillcolor("#FF69B4")
turtle.bgcolor("#90EE90")

def draw_a_star():
    
    for i in range (5):
        turtle.fd(100)
        turtle.rt(144)
        
def move_forward():
    
    turtle.pu()
    turtle.fd(350)
    turtle.pd()

def turn_right():
    
    turtle.rt(144)
    

for i in range(5):
    draw_a_star()
    move_forward()
    turn_right()

