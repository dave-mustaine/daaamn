import pygame
from pygame.locals import *
# pip install PyOpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (0, 0, 0),
    (0, 1, 0),
    (0.7, 1, 0),
    (0.7, 0.8, 0),
    (0.2, 0.8, 0),
    (0.2, 0.2, 0),
    (0.7, 0.2, 0),
    (0.7, 0, 0),
    (0, 0, 0.2),
    (0, 1, 0.2),
    (0.7, 1, 0.2),
    (0.7, 0.8, 0.2),
    (0.2, 0.8, 0.2),
    (0.2, 0.2, 0.2),
    (0.7, 0.2, 0.2),
    (0.7, 0, 0.2)
)

edges = ((0, 1), (0, 7), (0, 8), (1, 2), (1, 9), (2, 3), (2, 10), (3, 4), (3, 11), (4, 5), (4, 12), (5, 6), (5, 13),
         (6, 7), (6, 14), (7, 15), (8, 9), (8, 15), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15))


def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    glRotatef(0.5, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    cube()
    pygame.display.flip()
    pygame.time.wait(10)
