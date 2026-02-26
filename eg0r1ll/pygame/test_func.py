import pygame
import random


def testFoo(screen, countt=0):
    pygame.draw.rect(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (0, 0, 100, 100))
    print("test")
