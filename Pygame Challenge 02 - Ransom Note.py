# -----------------------------------------------------------------------------
# TEXT & FONT LAB - RANSOM NOTE
# 
# Use your new knowledge of text in Pygame to make a ransom note similar to the picture above.
# 
# You use whatever fonts you want as long as you use at least 1 custom font.
# 
# The message can say whatever you want as long as it is school safe (remember the code of conduct).
# 
# Lab Requirements:
# LEVEL 3
# Use at least 3 different font styles
# Use 3 different colours
# Write a message that is school safe and does not have anyone’s personal information (including names)

# LEVEL 4
# Everything listed in level 3 
# Use at least 4 different font styles
# Use 4 different colours

# LEVEL 4+
# Everything listed in level 4
# Use a custom downloaded font
# 
# Recommended Lessons:
# Github
# Thonny
# Pygame Intro
# Pygame Window
# Pygame Game Loop
# Pygame Drawing
# Pygame Colours
# Pygame Text & Fonts
# 
# 
# Challenge Difficulty:**
# 
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
# 
# Upload your code to github when finished
# 
# Good luck!
#-----------------------------------------------------------------------------
import pygame
pygame.init()

# *********SETUP**********

windowWidth = 500
windowHeight = 500
window = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()  #will allow us to set framerate
#Load Fonts
    #These 3 are loading base system fonts and giving them traits like bold and italic
font1 = pygame.font.SysFont("arial", 40, bold=True)
font2 = pygame.font.SysFont("comicsansms", 50)
font3 = pygame.font.SysFont("timesnewroman", 60, italic=True)
    #This is for loading the custom downloaded font
font4 = pygame.font.Font("Fonts/Note Font.ttf", 40)
    #colors for all the text
RED = (255, 60, 60) 
BLUE = (60, 120, 255) 
GREEN = (60, 200, 100) 
YELLOW = (255, 230, 80)

# *********GAME LOOP**********
while True:
    # *********EVENTS**********
    ev = pygame.event.poll()    # Look for any event
    if ev.type == pygame.QUIT:  # windowow close button clicked?
        break                   #   ... leave game loop

    # *********DRAW THE FRAME**********

    #generates a light background for the words
    window.fill((240, 240, 240))

    #Messages for the Ransom notes
    text1 = font1.render("test message", True, RED)
    text2 = font2.render("test message", True, BLUE)
    text3 = font3.render("test message", True, GREEN)
    text4 = font4.render("test message", True, YELLOW)

    #Uses rect in pygame to make rectangles and center them in the middle of the window in a stack
    t1_rect = text1.get_rect(center=(windowWidth//2, 150)) 
    t2_rect = text2.get_rect(center=(windowWidth//2, 200)) 
    t3_rect = text3.get_rect(center=(windowWidth//2, 250)) 
    t4_rect = text4.get_rect(center=(windowWidth//2, 300))
    #PUT YOUR DRAWING, IMAGE PLACEMENT, BLIT ETC.. COMMANDS HERE FOR EACH GAMESTATE'''
    #makes the blit to show each text and the rectangle for them
    window.blit(text1, t1_rect) 
    window.blit(text2, t2_rect) 
    window.blit(text3, t3_rect) 
    window.blit(text4, t4_rect)
    # *********SHOW THE FRAME TO THE USER**********
    pygame.display.flip()
    clock.tick(60) #Force frame rate to 60fps or lower


pygame.quit()