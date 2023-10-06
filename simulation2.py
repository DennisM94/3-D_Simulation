import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

cube_angle = 0

def draw_cube():
    glBegin(GL_QUADS)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)

    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)

    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, -1, 1)

    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)

    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)

    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)

    glVertex3f(-1, 1, -1)
    glVertex3f(-1, -1, -1)

    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)

    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)

    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    glVertex3f(-1, 1, 1)
    glVertex3f(-1, -1, 1)

    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)

    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)

    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)

    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glEnd()

def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, (-1, 1, 1, 0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

def display():
    global cube_angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glRotatef(cube_angle, 1, 1, 0)
    draw_cube()
    glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(10)

    cube_angle += 1

pygame.init()
display_size = (800, 600)
pygame.display.set_mode(display_size, DOUBLEBUF | OPENGL)
gluPerspective(45, (display_size[0] / display_size[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

glEnable(GL_DEPTH_TEST)
setup_lighting()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    display()
