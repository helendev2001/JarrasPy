from pygame import *
import random
import sys

# Colores
NEGRO   = (0   , 0   , 0  )
ROJO    = (255 , 0   , 0  )
CAFE    = (90  , 50  , 15 )
CELESTE = (76  , 226 , 252)
BLANCO  = (255 , 255 , 255)
AGUA    = (220 , 251 , 249)


# Crea botones
def crearBoton(pantalla, boton, mensaje, color, marcar, fuente):
    if boton.collidepoint(mouse.get_pos()):
        draw.rect(pantalla,  marcar, boton)
    else:
        draw.rect(pantalla, color, boton)
    texto = fuente.render(mensaje, True, BLANCO)
    pantalla.blit(texto, (boton.x+(boton.width-texto.get_width()) / 2, boton.y+(boton.height-texto.get_height())/2))


# Parametros ventana pygame
init()
Letra = font.SysFont("Times New Roman", 20, bold=False, italic=False)
Dimensiones = (800, 500)
Pantalla = display.set_mode(Dimensiones)
display.set_caption("Jarras Puzzle")

# Variables
x = 100
y = 100
ancho = 100
alto = 30
escala = 50
opcion = ""
inicio = 0
estadoJ1 = 0
estadoJ2 = 0
# Jarras
J5 = Rect(x, y, 2*ancho, 5*escala)
J3 = Rect(x+(2.5*y), 2*y, 2*ancho, 3*escala)

# Botones
BLlenar = Rect(Pantalla.get_width()-150, 100, ancho, alto)
BVaciar = Rect(Pantalla.get_width()-150, 200, ancho, alto)
BTraspasar = Rect(Pantalla.get_width()-150, 300, ancho, alto)
incremento = y
Terminar = False
# Se define para poder gestionar cada cuando se ejecuta un fotograma
reloj = time.Clock()
v = 2
while not Terminar:

    Pantalla.fill((255, 255, 255))
    # Pantalla.fill(NEGRO)
    # ---Manejo de eventos
    for Evento in event.get():
        if Evento.type == QUIT:
            Terminar = True
        if Evento.type == MOUSEBUTTONDOWN and Evento.button == 1:
            if J5.collidepoint(mouse.get_pos()):
                opcion = "Jarra5"
                print("Selecciono Jarra de 5L")
            if BLlenar.collidepoint(mouse.get_pos()) and opcion == "Jarra5":
                incremento = 1;
                opcion = "Llenar_Jarra5"
                print("Llenar Jarra de 5L")
            if BVaciar.collidepoint(mouse.get_pos()) and opcion == "Jarra5":
                opcion = "Vaciar_Jarra5"
                print("Vaciar Jarra de 5L")
            if J3.collidepoint(mouse.get_pos()):
                opcion = "Jarra3"
                print("Selecciono Jarra de 3L")
            if BLlenar.collidepoint(mouse.get_pos()) and opcion == "Jarra3":
                incremento = 1;
                opcion = "Llenar_Jarra3"
                print("Llenar Jarra de 3L")
            if BVaciar.collidepoint(mouse.get_pos()) and opcion == "Jarra3":
                opcion = "Vaciar_Jarra3"
                print("Vaciar Jarra de 3L")


    crearBoton(Pantalla, BLlenar, "LLENAR", NEGRO, CELESTE, Letra)
    crearBoton(Pantalla, BVaciar, "VACIAR", NEGRO, CELESTE, Letra)
    crearBoton(Pantalla, BTraspasar, "TRASPASAR", NEGRO, CELESTE, Letra)
    # --Todos los dibujos van después de esta línea
    draw.rect(Pantalla, NEGRO, J5, 3)
    draw.rect(Pantalla, NEGRO, J3, 3)

    if opcion == "Jarra5":
        draw.rect(Pantalla, ROJO, J5, 3)
    elif opcion == "Jarra3":
        draw.rect(Pantalla, ROJO, J3, 3)
     
     
    if (opcion == "Llenar_Jarra5" and not estadoJ2==1):          #print("Llenar Jarra de 5L")
        if (incremento >= inicio and incremento < 5*escala):
            draw.rect(Pantalla, AGUA, (x, y, 2*ancho, incremento))
            draw.rect(Pantalla, NEGRO, J5, 3)
            incremento += v
            # print(incremento)
        if (incremento >= 245):
            draw.rect(Pantalla, AGUA, (x, y, 2*ancho, 5*escala))
            draw.rect(Pantalla, NEGRO, J5, 3)
        estadoJ1 = 1;
    elif  (opcion == "Llenar_Jarra5" and estadoJ2==1):
        if (incremento >= inicio and incremento < 5*escala):
            draw.rect(Pantalla, AGUA, (x, y, 2*ancho, incremento))
            draw.rect(Pantalla, NEGRO, J5, 3)
            incremento += v
            # print(incremento)
        if (incremento >= 245):
            draw.rect(Pantalla, AGUA, (x, y, 2*ancho, 5*escala))
            draw.rect(Pantalla, NEGRO, J5, 3)
            draw.rect(Pantalla, AGUA, (x+(2.5*y), 2*y, 2*ancho, 3*escala))
            draw.rect(Pantalla, NEGRO, J3, 3)

        estadoJ1 = 1;
        estadoJ2 = 1;

    if (opcion == "Llenar_Jarra3" and not estadoJ1==1):
        #print("Llenar Jarra de 5L")
        if (incremento >= inicio and incremento < 3*escala):
            draw.rect(Pantalla, AGUA, (x+(2.5*y), 2*y, 2*ancho, incremento))
            draw.rect(Pantalla, NEGRO, J3, 3)
            incremento += v
            # print(incremento)
        if (incremento >= 145):
            draw.rect(Pantalla, AGUA, (x+(2.5*y), 2*y, 2*ancho, 3*escala))
            draw.rect(Pantalla, NEGRO, J3, 3)
        estadoJ2 = 1;
    elif (opcion == "Llenar_Jarra3" and estadoJ1==1):
        if (incremento >= inicio and incremento < 3*escala):
            draw.rect(Pantalla, AGUA, (x+(2.5*y), 2*y, 2*ancho, incremento))
            draw.rect(Pantalla, NEGRO, J3, 3)
            incremento += v
            # print(incremento)
        if (incremento >= 245):
            draw.rect(Pantalla, AGUA, (x+(2.5*y), 2*y, 2*ancho, 3*escala))
            draw.rect(Pantalla, NEGRO, J3, 3)
            draw.rect(Pantalla, AGUA, (x, y, 2*ancho, 5*escala))
            draw.rect(Pantalla, NEGRO, J5, 3)
        estadoJ1 = 1;
        estadoJ2 = 1;
    # elif opcion==opcion="Llenar Jarra de 5L"
    print(estadoJ1,estadoJ2)
    # --Todos los dibujos van antes de esta línea
    display.flip()
    reloj.tick(60)  # Limitamos a 20 fotogramas por segundo

