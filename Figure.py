
from Vector import Vector
from abc import ABC, abstractmethod
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import math
import numpy as np
class Figure:
    def __init__(self, points, coordinates):

        self.coordinates = coordinates
        self.points = points
        for i in self.points:
            for j in range(len(i.coordinates)):
                i.coordinates[j] += self.coordinates[j]
        self.dxd=[0.5,0.5,0,1]
        self.pass1 = None
        self.edgez = []


    def proecite(self):
        for i in (self.points):
            if self.dxd[3] != 0:
                i.trim_cord = [i.coordinates[0]-i.coordinates[3]*self.dxd[0]/self.dxd[3],i.coordinates[1]-i.coordinates[3]*self.dxd[1]/self.dxd[3], i.coordinates[2]-i.coordinates[3]*self.dxd[2]/self.dxd[3] ]
            else:
                i.trim_cord = [i.coordinates[0], i.coordinates[1], i.coordinates[2]]
    def draw(self):

        self.proecite()

        glBegin(GL_LINES)
        for edge in self.edgez:
            for vertex in edge:
                glVertex3fv(self.points[vertex].trim_cord)
        glEnd()

    def rotate_figure(self,angle, plosk):
        if plosk == 0:
            mat_povorota = np.array([[1, 0,0,0],
                                     [0,1,0,0 ],
                                     [0,0,math.cos(angle),-math.sin(angle)],
                                     [0,0,math.sin(angle),math.cos(angle)]])

            for i in self.points:
                mat_tochki = np.array([i.coordinates[0],
                                        i.coordinates[1],
                                        i.coordinates[2],
                                        i.coordinates[3]])
                mat_itog = mat_povorota.dot(mat_tochki)
                i.coordinates = [mat_itog[0], mat_itog[1],mat_itog[2],mat_itog[3]]
        elif plosk == 1:
            mat_povorota = np.array([[math.cos(angle), 0, 0, -math.sin(angle)],
                                     [0, 1, 0, 0],
                                     [0, 0, 1, 0],
                                     [math.sin(angle), 0, 0, math.cos(angle)]])

            for i in self.points:
                mat_tochki = np.array([i.coordinates[0],
                                       i.coordinates[1],
                                       i.coordinates[2],
                                       i.coordinates[3]])
                mat_itog = mat_povorota.dot(mat_tochki)
                i.coordinates = [mat_itog[0], mat_itog[1], mat_itog[2], mat_itog[3]]

    def rasprint(self):
        for i in self.points:
            print(i.coordinates)
        print('--------------------')
class Cube(Figure):
    def __init__(self,points,coordinates):
        super().__init__(points,coordinates)
        self.edgez = (
            (0, 1),
            (0, 3),
            (0, 4),
            (2, 1),
            (2, 3),
            (2, 7),
            (6, 3),
            (6, 4),
            (6, 7),
            (5, 1),
            (5, 4),
            (5, 7),

            (0,8),
            (1,9),
            (2,10),
            (3,11),
            (4,12),
            (5,13),
            (6,14),
            (7,15),

            (0+8, 1+8),
            (0+8, 3+8),
            (0+8, 4+8),
            (2+8, 1+8),
            (2+8, 3+8),
            (2+8, 7+8),
            (6+8, 3+8),
            (6+8, 4+8),
            (6+8, 7+8),
            (5+8, 1+8),
            (5+8, 4+8),
            (5+8, 7+8)
        )
