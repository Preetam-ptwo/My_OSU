import math
import random
import pygame
from sys import exit

pygame.init()

width,height = 1280, 720
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

pygame.display.set_caption("My OSU")
pygame.display.set_icon(pygame.image.load("images\icon.png"))

font = pygame.font.Font("resources\lato.ttf", 42)
score_value = 0

bg_music = pygame.mixer.Sound("resources\gbgm.wav")
bg_music.play(loops = -1)

sound = pygame.mixer.Sound('resources\impact.wav')
sound.set_volume(0.5)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, "Purple")
    screen.blit(score, (x, y))


# circle
Mouse_y=0
Mouse_x=0
circleImg = []
circleX = []
circleY = []
num_of_enemies = 4

for i in range(num_of_enemies):
    circleImg.append(pygame.image.load('images\circles_3.png'))
    circleX.append(random.randint(100, 1180))
    circleY.append(random.randint(100, 620))


def circle(x, y, i):
    screen.blit(circleImg[i], (x, y))

def isCollision(circleX, circleY, bulletX, bulletY):
    distance = math.sqrt(math.pow(circleX - bulletX, 2) + (math.pow(circleY - bulletY, 2)))
    if distance < 50:
        return True
    else:
        return False

while True:
    
    screen.blit(pygame.image.load("images\BG.png"),(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Mouse_x, Mouse_y = pygame.mouse.get_pos()

    for i in range(num_of_enemies):

         # Collision
        collision = isCollision(circleX[i]+90, circleY[i]+90, Mouse_x, Mouse_y)
        if collision:
            sound.play()
            score_value += 1
            circleX[i] = random.randint(100, 1180)
            circleY[i] = random.randint(100, 620)

        circle(circleX[i], circleY[i], i)

    show_score(10,10)
    pygame.display.update()
    clock.tick(60)