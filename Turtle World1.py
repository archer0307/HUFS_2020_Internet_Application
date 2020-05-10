import turtle

turtle.setup(width=1920,height=1061)
turtle.speed(2)
turtle.hideturtle()
turtle.pensize(3) #색은 RGB 16진수 코드로 찾았으나, 두께를 구하지 못함.

def draw_a_star():
    
    for i in range (5):
        turtle.fd(100)
        turtle.rt(144)
        
draw_a_star()

