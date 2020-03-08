import pygame
import random

#inicializa los modulos de pygame
pygame.init()

#referencias para los colores
green = (0, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)

#tamanho de la ventana
display_ancho = 800
display_largo = 600

#Crea la ventana
display = pygame.display.set_mode((display_ancho, display_largo))
#Titulo para la ventana
pygame.display.set_caption("Snake")

#timer
clock = pygame.time.Clock()

#el bloque de vibora
snake_block = 10
#velocidad de la vibora
snake_speed = 15

#fuente del texto
font_style = pygame.font.SysFont(None, 50)
score_style = pygame.font.SysFont(None, 35)

def player_score(score):
    """Dibuja en pantalla el score del player"""
    #asigna el valor para luego hacer el blit 
    value = score_style.render("Score:" + str(score), True, red)
    #dibuja en pantalla
    display.blit(value, [ 0, 0 ])

def snake_player(snake_block, snake_list):
    """Dibuja en pantalla la vibora"""
    #recorre la lista de coordenadas del cuerpo de la vibora y lo dibuja
    for x in snake_list:
        pygame.draw.rect(display, green, [ x[ 0 ], x[ 1 ], snake_block, snake_block ])

def mensaje(mensajeArgumento, color, posicionX, posicionY):
    """Funcion para desplegar mensaje en pantalla"""
    #Hace el mensaje
    mensajeDesplegar = font_style.render(mensajeArgumento, True, color)

    #despliega en la ventana
    display.blit(mensajeDesplegar, [ posicionX, posicionY ])

def gameloop():
    """Funcion del juego, practicamente su inicio y su cierre"""

    #bandera para terminar el juego
    game_over = False

    #bandera para cerrar el juego
    game_close = False

    #posicion inicial de la vibora
    x1 = display_ancho / 2
    y1 = display_largo / 2

    #Contendran los movimientos de la vibora
    movimiento_x = 0
    movimiento_y = 0
    
    #Cuerpo de la vibora y su longitud
    snake_list = [ ]
    longitud_snake = 1


    #Posiciones aleatorias para la comida
    comida_x = random.randrange(0, display_ancho - snake_block, 10)
    comida_y = random.randrange(0, display_largo - snake_block, 10)

    #mientras no se pierda en el juego
    while not game_over:

        #mientras se cierre el juego
        while game_close:
            #pantalla en negro
            display.fill(black)
            #Imprime el mensaje para salir o seguir jugando
            mensaje("Game over", red, display_ancho / 3, display_largo / 3)
            mensaje("Presione q para salir o r para repetir", red, 100, 300) 
            #refresca la pantalla
            pygame.display.update()

            #por cada evento en la lista de eventos mapear las teclas para
            #para saber si se ingreso q o r
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    #finaliza el juego
                    pygame.quit()

                    #finaliza el programa
                    quit()
                    return

                if event.type == pygame.KEYDOWN:
                    #si se presiona q sale del juego
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close == False 

                        #finaliza el juego
                        pygame.quit()

                        #finaliza el programa
                        quit()
                        return

                    #si se presiona r se vuelve a llamar al loop del juego
                    if event.key == pygame.K_r:
                        gameloop()

        #por cada evento en lista de eventos
        for event in pygame.event.get():
            #Si el evento es el boton de la esquina superior derecha (la x) se
            #se cambia el estado de la bandera
            if event.type == pygame.QUIT:
                game_over = True

            #Si se presiona una tecla entonces
            if event.type == pygame.KEYDOWN:
                #Se filtra cual tecla es, y se asigna el movimiento respectivo
                if event.key == pygame.K_DOWN:
                    movimiento_x = 0
                    movimiento_y = snake_block
                elif event.key == pygame.K_UP:
                    movimiento_x = 0 
                    movimiento_y = -snake_block
                elif event.key == pygame.K_RIGHT:
                    movimiento_x = snake_block
                    movimiento_y = 0
                elif event.key == pygame.K_LEFT:
                    movimiento_x = -snake_block
                    movimiento_y = 0

        #En el caso de que la vibora choque con los extremos de la ventana
        if x1 >= display_ancho or x1 < 0 or y1 >= display_largo or y1 < 0:
            game_close = True

        #se actualiza para dibujar la vibora en la posicion respectiva
        x1 += movimiento_x
        y1 += movimiento_y

        #Para refrescar el fondo y para que no quede el dibujo de la vibora
        display.fill(black)

        #Dibujar la vibora en los pixeles especificados (x1, y1)
        pygame.draw.rect(display, green, [ comida_x, comida_y, snake_block, snake_block ])

        #Cabeza y cuerpo de la vibora
        snake_Head = [ ]
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)

        #Cada vez elimina la cola porque la cabeza es la que se extiende
        if len(snake_list) > longitud_snake:
            del snake_list[ 0 ]

        #En el caso de que choque contra su cuerpo 
        for x in snake_list[ : -1 ]:
            if x == snake_Head:
                game_close = True

        #Dibuja la vibora y el score
        snake_player(snake_block, snake_list)
        player_score(longitud_snake - 1)

        #Actualiza la pantalla
        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            print("NHOOM")
            #Posiciones aleatorias para la comida
            comida_x = random.randrange(0, display_ancho - snake_block, 10)
            comida_y = random.randrange(0, display_largo - snake_block, 10)
            longitud_snake += 1
            

        #velocidad de refresco
        clock.tick(snake_speed)

    #finaliza el juego
    pygame.quit()

    #finaliza el programa
    quit()

gameloop()
