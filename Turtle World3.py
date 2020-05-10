import turtle

turtle.shape("turtle")
turtle.pencolor("#0000FF")
turtle.fillcolor("#0000FF")
turtle.bgcolor("#90EE90")
turtle.pensize(3)

def clock():
    turtle.pu()
    turtle.fd(100)
    turtle.pd()
    turtle.fd(10)
    turtle.pu()
    turtle.fd(20)
    turtle.stamp()


turtle.stamp()

for i in range(12):
    clock()
    turtle.setpos(0,0)
    turtle.rt(30)

