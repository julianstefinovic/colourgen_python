import pygame
import random
import time

pygame.init()

dim = 500

win = pygame.display.set_mode((dim, dim))

pygame.display.set_caption("Snake")

r1 = 0
r2 = 0

rc1 = 0
rc2 = 0
rc3 = 0 

dim1 = 0
dim2 = 0

i = 0

time.sleep(10)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  

    #for i in range(5):

    dim1 = random.randint(10, 10)
    dim2 = random.randint(10, 10)

    r1 = random.randint(0, dim-20)
    r1 = (r1*20)%1000
    r2 = random.randint(0, dim-20)
    r2 = (r2*20)%1000

    rc1 = random.randint(0, 255)
    rc2 = random.randint(0, 255)
    rc3 = random.randint(0, 255)

    if i > 20000:
        rc1 = 0
        rc2 = 0
        rc3 = 0

    if i < 100000:
        pygame.draw.rect(win, (rc1, rc2, rc3), (r1, r2, dim1, dim2))

        pygame.display.update()
    i +=1

pygame.quit()