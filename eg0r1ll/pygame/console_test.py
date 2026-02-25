import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1600, 900), pygame.RESIZABLE)
pygame.display.set_caption("console")


clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)

# ==============================================


# Переменные консоли
console_active = False
console_text = ""
console_log = []


game_status = True
while game_status:
    
    if not console_active: # когда консоль закрыта можно менять экран
        screen.fill("gray")


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game_status = False


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                game_status = False
            
            
            elif event.key == pygame.K_F1: # меняем флаг статуса консоли от нажатой клавиши
                console_active = not console_active
                
                # if not console_active: # перезаливка экрана (если она не заливается по умолчанию в цикле)
                #     screen.fill((0,0,0))

            if console_active:
                # Обработка ввода консоли
                if event.key == pygame.K_RETURN:
                    if console_text == "clear":
                        console_log = []
                    elif console_text == "quit" or console_text == "exit":
                        console_log = []
                        console_text = ""
                        console_active = False
                    else:
                        console_log.append(console_text)
                    console_text = ""

                elif event.key == pygame.K_BACKSPACE:
                    console_text = console_text[:-1]

                else:
                    console_text += event.unicode 


    if console_active:
        # Отрисовка фона консоли
        console_rect = pygame.Rect(0, 0, 800, 200)
        pygame.draw.rect(screen, (50, 50, 50), console_rect)
        
        # Отрисовка лога
        for i, line in enumerate(console_log[-5:]): # Последние 5 строк
            text_surf = font.render(line, True, (255, 255, 255))
            screen.blit(text_surf, (10, 10 + i * 30))
        
        # Отрисовка ввода
        input_surf = font.render("> " + console_text, True, (0, 200, 0))
        screen.blit(input_surf, (10, 160))
        

    pygame.display.update()

    clock.tick(60)  











