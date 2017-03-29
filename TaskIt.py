import pygame
import os
import sys
import planes
from collections import deque
# Define drag and drop task images
class Task(planes.Plane):
    def __init__(self, name, rect, image, highlight = True, draggable = False, grab = False):
        planes.Plane.__init__(self, name, rect, draggable, grab)
        self.moving = False
        self.image = image

class Day(planes.Plane):
    def __init__(self, name, rect, draggable = False, grab = False):
        planes.Plane.__init__(self, name, rect, draggable, grab)
        self.count = len(self.subplanes)

    def dropped_upon(self, plane, coordinates):
        self.count = len(self.subplanes)
        print(coordinates[0])
        print(self.rect.x)
        newX = 65
        newY = self.count * 70 + 35
        coordinates = ((newX, newY))          
        planes.Plane.dropped_upon(self, plane, coordinates)
        plane.moving = False
        self.count = len(self.subplanes)
        drop_sound.play()

class DropDisplay(planes.Display):
    def dropped_upon(self, plane, coordinates):
        if isinstance(plane, Task):
            planes.Display.dropped_upon(self, plane, coordinates)
            plane.moving = False

#setup folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
audio_folder = os.path.join(game_folder, 'audio')

#Preinitialize audio mixer
pygame.mixer.pre_init(44100, -16, 2, 2048)
# initialize game engine
pygame.init()

#Set up game audio
pygame.mixer.music.load(os.path.join(audio_folder, "Task_It_theme.mp3"))

pygame.mixer.music.play(-1)
drop_sound = pygame.mixer.Sound(os.path.join(audio_folder,'drop_sound.wav'))

# set screen width/height and caption
screen = DropDisplay((800, 480))
screen.grab = False
# Load the background image
background = pygame.image.load(os.path.join(img_folder, "Taskitboard.jpg")).convert()
screen.image = background
backgroundRect = background.get_rect()
pygame.display.set_caption("Task It")
# initialize clock. used later in the loop.
clock = pygame.time.Clock()

# Create Task List
screen.sub(Day("TaskList", pygame.Rect((15, 200), (135, 215)), draggable = False, grab = True))
screen.TaskList.image.fill((228, 255, 250))

# Create Days
# Sunday
screen.sub(Day("Sunday", pygame.Rect((185, 50), (130, 185)), draggable = False, grab = True))
screen.Sunday.image.fill((228, 255, 250))
# Monday
screen.sub(Day("Monday", pygame.Rect((340, 50), (130, 185)), draggable = False, grab = True))
screen.Monday.image.fill((228, 255, 250))
# Tuesday
screen.sub(Day("Tuesday", pygame.Rect((495, 50), (130, 185)), draggable = False, grab = True))
screen.Tuesday.image.fill((228, 255, 250))
# Wednesday
screen.sub(Day("Wednesday", pygame.Rect((650, 50), (130, 185)), draggable = False, grab = True))
screen.Wednesday.image.fill((228, 255, 250))
# Thursday
screen.sub(Day("Thursday", pygame.Rect((185, 290), (130, 180)), draggable = False, grab = True))
screen.Thursday.image.fill((228, 255, 250))
# Friday
screen.sub(Day("Friday", pygame.Rect((340, 290), (130, 180)), draggable = False, grab = True))
screen.Friday.image.fill((228, 255, 250))
# Saturday
screen.sub(Day("Saturday", pygame.Rect((495, 290), (130, 180)), draggable = False, grab = True))
screen.Saturday.image.fill((228, 255, 250))

# Create tasks
task1 = pygame.image.load(os.path.join(img_folder, "Task1.png")).convert()
screen.TaskList.sub(Task("Task1", task1.get_rect(), task1, draggable = True))

task2 = pygame.image.load(os.path.join(img_folder, "Task1.png")).convert()
screen.TaskList.sub(Task("Task2", pygame.Rect((0, task2.get_height()),(task2.get_width(), task2.get_height())), task2, draggable = True))
task3 = pygame.image.load(os.path.join(img_folder, "Task1.png")).convert()
screen.TaskList.sub(Task("Task3", pygame.Rect((0, task3.get_height() * 2), (task3.get_width(), task3.get_height())), task3, draggable = True))
 
# Loop until the user clicks close button
done = False
while done == False:
    # write event handlers here
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
    # write game logic here
    screen.process(events)

    # write draw code here

    # display what is drawn here
    screen.update()
    screen.render()
    pygame.display.flip()
    # run at 20 fps
    clock.tick(60)
 
# close the window and quit
pygame.quit()