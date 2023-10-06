import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

rotate_angle = [0, 0, 0]  # Initial rotation angles

def draw_cube():
    glBegin(GL_QUADS)
    # Bottom face
    glNormal3f(0, -1, 0)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)

    # Top face
    glNormal3f(0, 1, 0)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    # Front face
    glNormal3f(0, 0, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    # Back face
    glNormal3f(0, 0, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)

    # Left face
    glNormal3f(-1, 0, 0)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, -1, 1)

    # Right face
    glNormal3f(1, 0, 0)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)

    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_LINE_LOOP)
    # Bottom face edges
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)

    glEnd()

    glBegin(GL_LINE_LOOP)
    # Top face edges
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    glEnd()

    glBegin(GL_LINES)
    # Connecting edges
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)

    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)

    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)

    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)
    glEnd()


def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    # Set up positional light based on the view matrix
    modelview_matrix = glGetDoublev(GL_MODELVIEW_MATRIX)
    light_position = [modelview_matrix[3][0], modelview_matrix[3][1], modelview_matrix[3][2], 1]  # Positional light
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glRotatef(rotate_angle[0], 1, 0, 0)
    glRotatef(rotate_angle[1], 0, 1, 0)
    glRotatef(rotate_angle[2], 0, 0, 1)
    draw_cube()
    glPopMatrix()

    pygame.display.flip()

def handle_events():
    global rotate_angle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                pygame.mouse.get_rel()  # Reset mouse position for smooth rotation
        elif event.type == pygame.MOUSEMOTION and event.buttons[0]:
            # Rotate based on mouse movement
            rotate_angle[0] += event.rel[1]
            rotate_angle[1] += event.rel[0]

pygame.init()
display_size = (800, 600)
pygame.display.set_mode(display_size, DOUBLEBUF | OPENGL)
gluPerspective(45, (display_size[0] / display_size[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

glEnable(GL_DEPTH_TEST)

while True:
    handle_events()
    setup_lighting()  # Call setup_lighting before each display to update light position
    display()
    pygame.time.wait(10)
