import pygame
import os
import sys
import planes
from collections import deque
# Define drag and drop task images
class Task(planes.Plane):

    def __init__(self, name, rect, image, draggable = False, grab = False):
        planes.Plane.__init__(self, name, rect, draggable, grab)

        self.moving = False
        self.image = image

class Day(planes.Plane):

	def dropped_upon(self, plane, coordinates):

		planes.Plane.dropped_upon(self, plane, coordinates)

		plane.moving = False

class DropDisplay(planes.Display):

	def dropped_upon(self, plane, coordinates):

		if isinstance(plane, Task):

			planes.Display.dropped_upon(self, plane, coordinates)

			plane.moving = False
    
#setup folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
# initialize game engine
pygame.init()
# set screen width/height and caption
screen = DropDisplay((1276, 800))
screen.grab = False
# Load the background image
background = pygame.image.load(os.path.join(img_folder, "TaskItBoard.jpg")).convert()
screen.image = background
backgroundRect = background.get_rect()
pygame.display.set_caption("Task It")
# initialize clock. used later in the loop.
clock = pygame.time.Clock()

# Create Task List
screen.sub(Day("TaskList", pygame.Rect((28, 331),(219, 436)), draggable = False, grab = True))
screen.TaskList.image.fill((229, 254, 248))

# Create Days
# Sunday
screen.sub(Day("Sunday", pygame.Rect((292, 96), (219, 303)), draggable = False, grab = True))
screen.Sunday.image.fill((229, 254, 248))
# Monday
screen.sub(Day("Monday", pygame.Rect((537, 96),(219, 303)), draggable = False, grab = True))
screen.Monday.image.fill((229, 254, 248))
# Tuesday
screen.sub(Day("Tuesday", pygame.Rect((782, 96),(219, 303)), draggable = False, grab = True))
screen.Tuesday.image.fill((229, 254, 248))
# Wednesday
screen.sub(Day("Wednesday", pygame.Rect((1027, 96),(219, 303)), draggable = False, grab = True))
screen.Wednesday.image.fill((229, 254, 248))

# Thursday
screen.sub(Day("Thursday", pygame.Rect((292 ,475), (219, 303)), draggable = False, grab = True))
screen.Thursday.image.fill((229, 254, 248))
# Friday
screen.sub(Day("Friday", pygame.Rect((537, 475), (219, 303)), draggable = False, grab = True))
screen.Friday.image.fill((229, 254, 248))
# Saturday
screen.sub(Day("Saturday", pygame.Rect((782, 475), (219, 303)), draggable = False, grab = True))
screen.Saturday.image.fill((229, 254, 248))


# Create tasks
task1 = pygame.image.load(os.path.join(img_folder, "Task1.png")).convert()
screen.TaskList.sub(Task("Task1", task1.get_rect(), task1, draggable = True))

task2 = pygame.image.load(os.path.join(img_folder, "Task1.png")).convert()
screen.TaskList.sub(Task("Task2", pygame.Rect((0, task2.get_height()),(task2.get_width(), task2.get_height())), task2, draggable = True))

task3 = pygame.image.load(os.path.join(img_folder, "Task1.png")).convert()
screen.TaskList.sub(Task("Task3", pygame.Rect((0, task3.get_height() * 2), (task3.get_width(), task3.get_height())), task3, draggable = True))

task4 = pygame.image.load(os.path.join(img_folder, "Task1.png")).convert()
screen.TaskList.sub(Task("Task4", pygame.Rect((0, task4.get_height() * 3), (task4.get_width(), task4.get_height())), task4, draggable = True))
 
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
