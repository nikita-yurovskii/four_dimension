from Point import Point
from Vector import Vector
from OpenGL.GL import *
import glfw
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Figure import Cube
def main():
    rotation = 0
    pl = 0

    a = Cube((
        Point(1, -1, -1,-1), #-1
        Point(1, 1, -1,-1), #1
        Point(-1, 1, -1,-1), #2
        Point(-1, -1, -1,-1),#3
        Point(1, -1, 1,-1),#4
        Point(1, 1, 1,-1),#5
        Point(-1, -1, 1,-1),#6
        Point(-1, 1, 1,-1), #7

        Point(1, -1, -1,1),#8
        Point(1, 1, -1,1),#9
        Point(-1, 1, -1,1),#1-1
        Point(-1, -1, -1,1),#11
        Point(1, -1, 1,1),#12
        Point(1, 1, 1,1),#13
        Point(-1, -1, 1,1),#14
        Point(-1, 1, 1,1)#15
    ), [0,0,0,0])

    pygame.init()
    display = (1280, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(50, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type ==  pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rotation = -0.01
                    pl = 0
                elif event.key == pygame.K_RIGHT:
                    rotation = 0.01
                    pl = 0
                elif event.key == pygame.K_UP:
                    rotation = -0.01
                    pl = 1
                elif event.key == pygame.K_DOWN:
                    rotation = 0.01
                    pl = 1

            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT,
                             pygame.K_RIGHT,pygame.K_UP,
                             pygame.K_DOWN]:
                    rotation = 0

        a.rasprint()
        a.rotate_figure(rotation, pl)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        a.draw()
        pygame.display.flip()
        pygame.time.wait(15)

main()