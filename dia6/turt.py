import turtle             
from time import sleep

tortuga = turtle.Turtle( )
tortuga.shape( "turtle" )
sleep( 1 )
#
#for i in range( 1, 4 ):
#    tortuga.forward( 100 )
#    tortuga.left( 90 )
#tortuga.forward( 100 )
#
#while True:
#    tortuga.forward( 1 )
#    tortuga.left( 1 )
#
from random import randint
ancho = turtle.window_width( )
alto = turtle.window_height( )
tortuga.color( "green" )

while True:
    posicion = tortuga.pos( )
    movimiento = randint( 100, 150 )
    giro = randint( 1, 60 )
    tortuga.forward( movimiento )
    tortuga.left( giro )
    print( posicion )
    if posicion[ 0 ] > ancho / 2 or posicion[ 0 ] < -ancho / 2:
        tortuga.color( "red" )
        sleep( 0.5 )
        tortuga.home( )
        tortuga.color( "green" )
    if posicion[ 1 ] > alto / 2 or posicion[ 1 ] < -alto / 2:
        tortuga.color( "red" )
        sleep( 0.5 )
        tortuga.home( )
        tortuga.color( "green" )

input( )

#
#my_window = turtle.Screen() 
#my_window.bgcolor("blue")       # creates a graphics window
#my_pen = turtle.Turtle()      
#while True:
#
#    my_pen.forward(150)           
#    my_pen.left(90)               
#    my_pen.forward(75)
#my_pen.color("white")
#my_pen.pensize(12)
#input( )
