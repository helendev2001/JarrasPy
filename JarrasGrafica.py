from pygame import *
import random
import sys

NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
CAFE = (90, 50, 15)
CELESTE = (76, 226, 252)
BLANCO = (255, 255, 255)

def crearBoton(pantalla, boton, mensaje, color, marcar,fuente):
    if boton.collidepoint(mouse.get_pos()):
        draw.rect(pantalla,  marcar, boton)
    else:
        draw.rect(pantalla, color, boton)
    texto = fuente.render(mensaje, True, NEGRO)
    pantalla.blit(texto, (boton.x+(boton.width-texto.get_width())/2, boton.y+(boton.height-texto.get_height())/2))

init()
Letra = font.SysFont("Calibri", 20, bold=False, italic=False)
Dimensiones = (800, 500)
Pantalla = display.set_mode(Dimensiones)
display.set_caption("JARRAS")

x=150
y=360
ancho=75
alto=30
dist=25
J5 = Rect(x, 100, 200, 250)
J3 = Rect(y+dist, 200, 200, 150)
BLlenar5 = Rect(x, y, ancho, alto)
BVaciar5 = Rect(x+ancho+dist, y, ancho, alto)
BLlenar3 = Rect(x+ancho+(7*dist), y, ancho, alto)
BVaciar3 = Rect(x+ancho+(12*dist), y, ancho, alto)
aux = 0
clic = 0
Terminar = False
# Se define para poder gestionar cada cuando se ejecuta un fotograma
reloj = time.Clock()

while not Terminar:

    Pantalla.fill((255, 255, 255))
    #Pantalla.fill(NEGRO)
    # ---Manejo de eventos
    for Evento in event.get():
        if Evento.type == QUIT:
            Terminar = True
        if Evento.type == MOUSEBUTTONDOWN and Evento.button == 1:
            if BLlenar5.collidepoint(mouse.get_pos()):
                print("Llenar5")
                aux = 1
                clic = clic + 1
            if BVaciar5.collidepoint(mouse.get_pos()):
                print("Vaciar5")
                aux = 2
            if BLlenar3.collidepoint(mouse.get_pos()):
                print("Llenar3")
                aux = 3
                clic = clic + 1
                print(clic)
            if BVaciar3.collidepoint(mouse.get_pos()):
                print("Vaciar3")
                aux = 4
            if J5.collidepoint(mouse.get_pos()):
                print("Jarra de 5")
            if J3.collidepoint(mouse.get_pos()):
                print("Jarra de 3")

    if BLlenar5.collidepoint(mouse.get_pos()):
        crearBoton(Pantalla,BLlenar5,"LLENAR",BLANCO,CELESTE,Letra)
    else:
        crearBoton(Pantalla, BLlenar5, "LLENAR", BLANCO, CELESTE, Letra)

    if BLlenar3.collidepoint(mouse.get_pos()):
        crearBoton(Pantalla, BLlenar3, "LLENAR", BLANCO, CELESTE, Letra)
    else:
        crearBoton(Pantalla, BLlenar3, "LLENAR", BLANCO, CELESTE, Letra)

    if BVaciar5.collidepoint(mouse.get_pos()):
        crearBoton(Pantalla, BVaciar5, "VACIAR", BLANCO, CELESTE, Letra)
    else:
        crearBoton(Pantalla, BVaciar5, "VACIAR", BLANCO, CELESTE, Letra)

    if BVaciar3.collidepoint(mouse.get_pos()):
        crearBoton(Pantalla, BVaciar3, "VACIAR", BLANCO, CELESTE, Letra)
    else:
        crearBoton(Pantalla, BVaciar3, "VACIAR", BLANCO, CELESTE, Letra)

    # --Todos los dibujos van después de esta línea
    draw.rect(Pantalla, ROJO, J5, 3)
    draw.rect(Pantalla, ROJO, J3, 3)

   # for row in range(297, 100, -50):
        #draw.line(Pantalla, NEGRO, (120, row), (130, row), 3)
    #for row2 in range(297, 200, -50):
        #draw.line(Pantalla, NEGRO, (400, row2), (410, row2), 3)

    if aux == 1:
        draw.rect(Pantalla, CELESTE, J5, 0)
        draw.rect(Pantalla, ROJO, J5, 3)
    elif aux == 2:
        draw.rect(Pantalla, NEGRO, J5, 0)
        draw.rect(Pantalla, ROJO, J5, 3)
    elif aux == 3:
        draw.rect(Pantalla, CELESTE, J3, 0)
        draw.rect(Pantalla, ROJO, J3, 3)
    elif aux == 4:
        draw.rect(Pantalla, NEGRO, J3, 0)
        draw.rect(Pantalla, ROJO, J3, 3)
    elif (clic%2)==0:
        draw.rect(Pantalla, CELESTE, J5, 0)
        draw.rect(Pantalla, ROJO, J5, 3)
        draw.rect(Pantalla, CELESTE, J3, 0)
        draw.rect(Pantalla, ROJO, J3, 3)

    # --Todos los dibujos van antes de esta línea
    display.flip()
    reloj.tick(20)  # Limitamos a 20 fotogramas por segundo
pygame.qu