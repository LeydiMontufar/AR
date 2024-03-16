import cv2
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Variables globales para la posición del modelo
x_pos = 0
y_pos = 0

def setup_pygame_window(width=640, height=480):
    pygame.init()
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Nissan GTR ArUco')
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (width / height), 0.1, 50.0)
    # Ajustar la posición inicial de la cámara
    glTranslatef(0.0, 0.0, -5)

def load_model(obj_path):
    vertices = []
    faces = []

    with open(obj_path, 'r') as file:
        for line in file:
            if line.startswith('v '):  # Vértice
                parts = line.split()
                vertices.append((float(parts[1]), float(parts[2]), float(parts[3])))
            elif line.startswith('f '):  # Cara
                parts = line.split()
                face = []
                for part in parts[1:]:
                    # Se asume un formato simple de cara 'f v1 v2 v3 ...'
                    # Esto podría necesitar ser ajustado para manejar otros formatos de cara
                    face.append(int(part.split('/')[0]))
                faces.append(tuple(face))

    return vertices, faces  # Asegúrese de devolver ambos valores

def create_display_list(vertices, faces):
    display_list = glGenLists(1)  # Solicita un identificador de lista de visualización
    if display_list != 0:  # Verifica que se haya generado un identificador válido
        glNewList(display_list, GL_COMPILE)
        # Su código para compilar la lista aquí...
        glEndList()
    return display_list


def main():
    global x_pos, y_pos

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    setup_pygame_window(640, 480)

    vertices, faces = load_model('3D/NISSAN-GTR.obj')
    display_list = create_display_list(vertices, faces)
    clock = pygame.time.Clock()
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    x_pos -= 0.1  # Mover hacia la izquierda
                elif event.key == K_RIGHT:
                    x_pos += 0.1  # Mover hacia la derecha
                elif event.key == K_UP:
                    y_pos += 0.1  # Mover hacia arriba
                elif event.key == K_DOWN:
                    y_pos -= 0.1  # Mover hacia abajo

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()  # Guardar el estado actual de la matriz
        glScalef(0.05, 0.05, 0.05)  # Redimensionar el modelo
        
        # Rotar el modelo
        # Angulo, eje X, eje Y, eje Z (Ejemplo: rotar 90 grados alrededor del eje Y)
        glRotatef(90, 0, 1, 0)

        glCallList(display_list)  # Renderizar el modelo
        glPopMatrix()  # Restaurar el estado previo de la matriz

        pygame.display.flip()
        clock.tick(30)

        

if __name__ == '__main__':
    main()
