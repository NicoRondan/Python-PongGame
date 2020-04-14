import turtle
import winsound

#Establecer ventana
wn = turtle.Screen()
#Setear titulo
wn.title("Pong by @NicoRondan")
#Background de la pantalla
wn.bgcolor("black")
#Tamaño
wn.setup(width=800, height=600)
wn.tracer(0)
wn.delay(40)

#Puntaje
score_a = 0
score_b = 0

# Paleta A
paddle_a = turtle.Turtle()
#Velocidad de animación
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
#Largo y ancho
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
#Posicionamiento de la paleta
paddle_a.goto(-350, 0)

# Paleta B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jugador A: 0  Jugador B: 0", align="center", font=("Courier", 24, "normal"))


# Funciones
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    
# Escuchando al teclado
wn.listen()
#Cuando se presionan las teclas, llamar a las funciones
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#Main game loop
while True:
    wn.update()
    
    #Mover la bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # chequear el borde
    if ball.ycor() > 290:
        ball.sety(290)
        #revertir la dirección
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        #revertir la dirección
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        #Sumar puntaje
        score_a += 1
        pen.clear()
        pen.write("Jugador A: {}  Jugador B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Jugador A: {}  Jugador B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        
    # Paleta y bola colisionan
    if (ball.xcor() > 340 and ball.xcor() < 350 ) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
    if (ball.xcor() < -340 and ball.xcor() > -350 ) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)