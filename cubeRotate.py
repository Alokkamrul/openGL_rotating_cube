"""

Name : Kamrul Islam
Reg : 2017331081

"""



import pygame 
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from graphics import * 

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )



def gl_lines(start, end):
   #Bressenham Line Drawing Algo
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
 
    is_steep = abs(dy) > abs(dx)
 
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
 
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
 
    dx = x2 - x1
    dy = y2 - y1
 
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1
 
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx
 
    if swapped: # Reverse the list if the coordinates were swapped
        points.reverse()
    return points


def isValid(input, m, n, x, y, prev_color, new_color):
    if (x < 0 or x >= m) or (y < 0 or y >= n) or (input[x][y] != prev_color) or (input[x][y] == new_color):
        return False
    return True


def floodfill(screen,   m, n, x,   y, prevC, newC):
    queue = []

    queue.append([x, y])
    screen[x][y] = newC
    while queue:

        currPixel = queue.pop()

        posX = currPixel[0]
        posY = currPixel[1]

        if isValid(screen, m, n,
                   posX + 1, posY,
                   prevC, newC):

            screen[posX + 1][posY] = newC
            queue.append([posX + 1, posY])

        if isValid(screen, m, n,
                   posX-1, posY,
                   prevC, newC):
            screen[posX-1][posY] = newC
            queue.append([posX-1, posY])

        if isValid(screen, m, n,
                   posX, posY + 1,
                   prevC, newC):
            screen[posX][posY + 1] = newC
            queue.append([posX, posY + 1])

        if isValid(screen, m, n,
                   posX, posY-1,
                   prevC, newC):
            screen[posX][posY-1] = newC
            queue.append([posX, posY-1])


surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)



colors = (
    (0,1,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (0,0,1),
    (0,0,1),
    (1,0,0),
    (0,1,0),
    (1,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1)
)

def Cube():

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


    glBegin(GL_QUADS)
    x =0
    for surface in surfaces:
        x+=1
        glColor3fv(colors[x])
        for vertex in surface:
            glVertex3fv(verticies[vertex])
            glColor3fv(colors[x])
            
    glEnd()

    

def main():
    pygame.init()
    display = (1200,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(75, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                glTranslatef(-.1,0,0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                glTranslatef(.1,0,0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                glTranslatef(0,-.1,0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                glTranslatef(0,.1,0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                glTranslatef(0,0,0.1)
            if event.button == 5:
                glTranslatef(0,0,-0.1)


        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()