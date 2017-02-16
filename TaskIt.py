import pygame
import os
#setup folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
# initialize game engine
pygame.init()
# set screen width/height and caption
screen = pygame.display.set_mode((640, 545))
# Load the background image
background = pygame.image.load(os.path.join(img_folder, "TaskItBoard.jpg")).convert()
backgroundRect = background.get_rect()
pygame.display.set_caption("Task It")
# initialize clock. used later in the loop.
clock = pygame.time.Clock()
 
# Loop until the user clicks close button
done = False
while done == False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # write game logic here
 
    # clear the screen by blitting the background
    screen.blit(background, backgroundRect)
    # write draw code here
 
    # display what is drawn here
    pygame.display.update()
    # run at 20 fps
    clock.tick(20)
 
# close the window and quit
pygame.quit()
