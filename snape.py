from operator import index
import turtle
import time
import random
posponer =0.1
wn =turtle.Screen()
wn.title("Juego de pong")
wn.bgcolor()
wn.setup(width=600,height=600)
wn.tracer(0)
score=0;
high_score=0;
#Funciones
def arriba():
    cabeza.direction="up"
def abajo():
    cabeza.direction="down"
def izquierda():
    cabeza.direction="left"
def derecha():
    cabeza.direction="right"
     
def mov():#movimiento
    y = cabeza.ycor()
    x=cabeza.xcor()
    if cabeza.direction == "up":
        cabeza.sety(y+20)
    if cabeza.direction == "down":
        cabeza.sety(y-20)
    if cabeza.direction == "left":
       cabeza.setx(x-20)
    if cabeza.direction == "right":
           cabeza.setx(x+20)

#cabeza
cabeza=turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()
cabeza.color("blue")
cabeza.goto(0,0)
cabeza.direction = "stop"
#comida

comida=turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)
#Segmentos
seg=[]
#texto
texto=turtle.Turtle()
texto.speed(0)
texto.color("red")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score:0         High Score :0",align="center",font=("Courier",24,"normal"))
#Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, ("Left"))
wn.onkeypress(derecha, "Right")
while True:
    wn.update()
    #colicion con comida
    if cabeza.distance(comida) <20:
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        comida.goto(x,y)
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.penup()
        nuevo_segmento.color("blue")
        seg.append(nuevo_segmento)
        #Aumentar marcador
        score+=10;
        if score >high_score:
            high_score=score
        texto.clear()
        texto.write("Score:{}         High Score :{}".format(score,high_score),align="center",font=("Courier",24,"normal"))
    #mover segmento
    totalSeg=len(seg)
    for index in range (totalSeg-1,0,-1):
        x=seg[index-1].xcor()
        y=seg[index-1].ycor()
        seg[index].goto(x,y)
    if totalSeg>0:
        x=cabeza.xcor()
        y=cabeza.ycor()
        seg[0].goto(x,y)
    if(cabeza.xcor()>280 or cabeza.xcor()<-280 or cabeza.ycor()<-280 or cabeza.ycor()>280):
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction="stop"
        for se in seg:
            se.goto(1000,1000)
        seg.clear()
        #recetear
        score=0;
        
        texto.clear()
        texto.write("Score:{}         High Score :{}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    mov()
    #colisiones con el curpo
    for se in seg:
        if se.distance(cabeza)<20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"
            for se in seg:
                se.goto(1000, 1000)
            seg.clear()
            score=0
            texto.clear()
            texto.write("Score:{}         High Score :{}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    time.sleep(posponer)
    