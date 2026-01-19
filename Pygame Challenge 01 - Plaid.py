# -----------------------------------------------------------------------------
# COLOUR LAB - PLAID
# 
# Use your new knowledge of drawing and colours with Pygame to make this a full screen of a plaid pattern.
# 
# Lab Requirements:
# LEVEL 3
# The plaid must have 2 different colours
# LEVEL 4
# Everything listed in level 3 
# The plaid has 2 different strokeWeights
# LEVEL 4+
# Everything listed in level 4
# The plaid uses alpha colour
# 
# Recommended Lessons:
# Github
# Thonny
# Pygame Intro
# Pygame Window
# Pygame Game Loop
# Pygame Drawing
# Pygame Colours
# 
# Challenge Difficulty:**
# 
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
# 
# Upload your code to github when finished
# 
# Good luck!
#-----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# IMAGE LAB - IMAGE COLLAGE
# 
# Use your new knowledge of drawing and colours with Pygame to make this a full screen of a plaid pattern.
# 
# Lab Requirements:
# LEVEL 3
# Use at least 3 different images to create a collage
# You can repeat the same images must use other commands to change the look (example, tint)

# LEVEL 4
# Everything listed in level 3 
# Create a scene with images

# LEVEL 4+
# Everything listed in level 4
# Randomize or animate something

# Recommended Lessons:
# P5.js intro
# P5.js drawing
# P5.js colour
# 
# Challenge Difficulty:**
# 
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
# 
# Upload your code to githun when finished
# 
# Good luck!
#-----------------------------------------------------------------------------
import pygame
pygame.init()

windowWidth = 500
windowHeight = 500
window = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()

RED = (255, 0, 0, 150)
BLUE = (0, 0, 255, 120)

plaid_window = pygame.Surface((windowWidth, windowHeight), pygame.SRCALPHA)

while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        break

    window.fill((255, 255, 255))

    # clear the plaid surface so it doesn’t stay black
    plaid_window.fill((0, 0, 0, 0))

    for x in range(0, windowWidth, 50):
        pygame.draw.line(plaid_window, RED, (x, 0), (x, windowHeight), 5)

    for y in range(0, windowHeight, 50):
        pygame.draw.line(plaid_window, BLUE, (0, y), (windowWidth, y), 10)

    window.blit(plaid_window, (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
