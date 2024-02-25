import sys
import pygame
from pygame.locals import *
import time

pygame.init()

# variable declaration
display_width = 600
display_height = 800

background = (231,225,247)
block_lv1 = (186,186,237)
block_lv2 = (134,220,123)
block_lv3 = (220,188,123)
paddle = (150,123,220)
paddle_outline = (50,50,50)
text = (78, 81, 139)


fps = 30
font = pygame.font.Font("./온글잎 밑미.ttf", 30)

left_time = 120
score = 0

# set
pygame.display.set_caption("breakout")
FramePerSec = pygame.time.Clock()
display = pygame.display.set_mode((display_width,display_height))

while True:
    left_time -= 0.03
    score += 99
    display.fill(background)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    time = font.render(f"남은시간 {round(left_time)}초",True, text)
    score_display = font.render(f"점수 {score}점",True, text)
    score_display_x = len(str(score))*9
    display.blit(time, [10, 10])
    display.blit(score_display, [500-score_display_x, 10])
    pygame.display.update()
    FramePerSec.tick(fps)