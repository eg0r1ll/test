import pygame
import random

pygame.init() # начало игры
screen = pygame.display.set_mode((1920, 1080)) # создание экрана
pygame.display.set_caption("test_game") # создание описание окна

screen.fill((100,100,100)) # заливка экрана

square = pygame.Surface((500, 500)) # создание квадрата
square.fill("red ")



running = True
while running:

    screen.blit(square, (0, 0)) # отрисовка раннее созданного квадрата
    pygame.draw.circle(screen, "blue", (1000, 500), 100) # отрисовка круга
    pygame.draw.line(square, "black", (0,0), (500, 500), 5) # отрисовка линии внутри раннее созданного квадрата 


    pygame.display.update() # обновление экрана


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
        # Отслеживания нажатия клавиш:
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_c: # с - color change
                screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))\
                
            elif event.key == pygame.K_ESCAPE: # esc - quit
                running = False
                pygame.quit()