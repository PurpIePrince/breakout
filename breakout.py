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
text_color = (80, 80, 140)

# setting
fps = 30
score = 0
left_time = 120
cols = 10
row = 12
game = False
game_over=0
font = pygame.font.Font("./온글잎 밑미.ttf", 30)

pygame.display.set_caption("breakout")
FramePerSec = pygame.time.Clock()
display = pygame.display.set_mode((display_width,display_height))


def draw_text(text, x, y):
    img = font.render(text,True, text_color)
    display.blit(img, (x, y))

while True:
    left_time -= 0.03
    score += 99
    score_display_x = len(str(score))*9
    display.fill(background)

    draw_text(f"남은시간 {round(left_time)}초", 10, 10)
    draw_text(str(f"점수: {score}점"), 500 - score_display_x, 10)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    FramePerSec.tick(fps)