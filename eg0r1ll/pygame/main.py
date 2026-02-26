import pygame
import threading

from test_func import testFoo
from tkinter_console_test import console



pygame.init()

FPS = 60
screen = pygame.display.set_mode((800, 450), pygame.RESIZABLE)
pygame.display.set_caption("main")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)



game_status = True
while game_status:

    pygame.display.update()

    for event in pygame.event.get():
        # exit:
        if event.type == pygame.QUIT:
            pygame.quit()
            game_status = False

        # keys:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                game_status = False

            elif event.key == pygame.K_f:
                testFoo(screen)

            elif event.key == pygame.K_F1:
                # threading
                console()


    clock.tick(FPS)