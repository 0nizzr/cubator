import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


# Define vertices, edges, surfaces, and colors of the cube
vertices = (    # Define the vertices of the cube as a tuple
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
    (5, 7)
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

colors = (

    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 1),
    (0, 0, 0)
)

# Define a function to draw the cube


def Cube():
    glBegin(GL_QUADS)   # Begin drawing the cube surfaces as quadrilaterals
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()            # End drawing the cube surfaces as quadrilaterals

    glBegin(GL_LINES)   # Begin drawing the cube edges as lines
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():        # Define the main function to display the cube
    pygame.init()   # Initialize pygame
    display = (800, 600)    # Define the display size
    # Set the display size
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    # Set the perspective
    gluPerspective(45, (display[0]/display[1]),
                   0.1, 50.0)

    # Translate the cube to the center of the screen
    glTranslatef(0.0, 0.0, -5)

    glRotatef(0, 0, 0, 0)   # Rotate the cube

    while True:    # Loop to keep the cube displayed
        for event in pygame.event.get():    # Loop to check for events
            if event.type == pygame.QUIT:   # Check for quit event
                pygame.quit()   # Quit pygame
                quit()        # Quit python

        glRotatef(1, 3, 1, 1)   # Rotate the cube
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen
        Cube()  # Draw the cube
        pygame.display.flip()   # Update the display
        # Wait 10 milliseconds before looping again to keep the cube rotating
        pygame.time.wait(10)


main()
