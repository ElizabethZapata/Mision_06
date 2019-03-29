#Autor: Elizabeth Citlalli Zapata Cortes
#Programa para dibujar espirógrafos con el valor del radio de dos círculos.
import random
import pygame
import math

# Dimensiones de la pantalla
ANCHO = 400
ALTO = 400
# Colores
BLANCO = (255, 255, 255)
AZUL = (79,121,201)
MENTA = (34,204,183)


def dibujarEspirografo(r,R,l,r2,R2,l2):

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo


        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras

        #círculo ROJO
        #radio=100
        #for angulo in range (0,360+1,1):
            #a= math.radians(angulo)
            #x= int(radio*math.cos(a))
            #y= int(radio*math.sin(a))
            #pygame.draw.circle(ventana, ROJO, (x+ANCHO//2,ALTO//2-y), 1)

        for grado in range(0, r // math.gcd(r, R) * 360):
            angulo = math.radians(grado)
            k = r / R

            x = int(R * (((l - k) * math.cos(angulo)) + ((l * k)) * math.cos(((l - k) / k) * angulo)))
            y = int(R * (((l - k) * math.sin(angulo)) - ((l * k)) * math.sin(((l - k) / k) * angulo)))

            pygame.draw.circle(ventana, MENTA, (x + ANCHO // 2, ALTO // 2 - y), 1)

        for grado in range(0, r2 // math.gcd(r2, R2) * 360):
            angulo = math.radians(grado)

            k = r2 / R2

            x = int(R2 * (((l2 - k) * math.cos(angulo)) + ((l2 * k)) * math.cos(((l2 - k) / k) * angulo)))
            y = int(R2 * (((l2 - k) * math.sin(angulo)) - ((l2 * k)) * math.sin(((l2 - k) / k) * angulo)))

            pygame.draw.circle(ventana, AZUL, (x + ANCHO // 2, ALTO // 2 - y), 1)



        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    #valores Prueba de la imagen adjuntada
    #r= 42 #radio círculo interno
    #R= 220 #Radio circulo externo
    #l= 0.6
    #Segundo Espirógrafo
    #r2= 72
    #R2= 220
    #l2= 0.6

    print("Primer Trazo")
    r= int(input("Teclear radio círculo interno: "))
    R= int(input("Teclear radio círculo externo: "))
    l= float(input("Teclear valor de l: "))
    print("Segundo trazo")
    r2= int(input("Teclear radio círculo interno: "))
    R2= int(input("Teclear radio círculo externo: "))
    l2= float(input("Teclear valor de l: "))

    dibujarEspirografo(r,R,l,r2,R2,l2)



main()