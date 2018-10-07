import pygame, time, sys

imagename = sys.argv[1]
delaytime = float(sys.argv[2])

pygame.init()
screen = pygame.display.set_mode((750,400))
pygame.mouse.set_visible(False)
image = pygame.image.load(imagename)
image = pygame.transform.scale(image, (750,400))
screen.blit(image, (0 , 0))
pygame.display.update()
time.sleep(delaytime)
pygame.quit()
