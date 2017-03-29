import pygame
import os
import sys
import planes
from collections import deque
# Define drag and drop task images

def move_up_tasks(self, plane, coordinates):
    # When a task is taken out of the task list, we need to move the remaining tasks up an insert another task
    x = 0
    for key, value in screen.TaskList.subplanes.iteritems():
        value.rect.x = 0
        value.rect.y = x * 45
        x = x + 1
    # Add a task to replace the previous task
    if len(tasks) > 0:
        screen.TaskList.sub(Task("Task" + str(screen.TaskList.currentTask), pygame.Rect((0, 45 * 3), (tasks[0].get_width(), tasks[0].get_height())), tasks[0], social[0], health[0], grades[0], draggable = True))
        screen.TaskList.currentTask = screen.TaskList.currentTask + 1
        screen.TaskList.count = screen.TaskList.count + 1
        tasks.remove(tasks[0])
        social.remove(social[0])
        health.remove(health[0])
        grades.remove(grades[0])
        print tasks
    print "callback function"

class Task(planes.Plane):
    def __init__(self, name, rect, image, social, health, grades, highlight = True, draggable = False, grab = False):
        planes.Plane.__init__(self, name, rect, draggable, grab)
        self.social = social
        self.health = health
        self.grades = grades
        self.name = name
        self.moving = False
        self.image = image

class Trash(planes.Plane):
    def __init__(self, name, rect, draggable = False, grab = False):
        planes.Plane.__init__(self, name, rect, draggable, grab)

    def dropped_upon(self, plane, coordinates):
        if isinstance(plane, Task):
            plane.destroy()

class TaskList(planes.Plane):
    def __init__(self, name, rect, draggable = False, grab = False):
        planes.Plane.__init__(self, name, rect, draggable, grab)
        self.count = len(self.subplanes)
        self.name = name
        self.currentTask = 5

    def dropped_upon(self, plane, coordinates):
            self.count = len(self.subplanes)
            if(self.count < 4):
                print coordinates[0]
                print self.rect.x
                newX = 65
                newY = self.count * 45 + 25
                coordinates = ((newX, newY))

                planes.Plane.dropped_upon(self, plane, coordinates)

                plane.moving = False
                self.count = len(self.subplanes)

                print self.name

class Day(planes.Plane):

        def __init__(self, name, rect, draggable = False, grab = False):
            planes.Plane.__init__(self, name, rect, draggable, grab)
            self.count = len(self.subplanes)
            self.name = name
            self.dropped_upon_callback = move_up_tasks

	def dropped_upon(self, plane, coordinates):
                self.count = len(self.subplanes)
                if(self.count < 4):
                    newX = 65
                    newY = self.count * 45 + 25
                    coordinates = ((newX, newY))
                    plane.draggable = False
                    global currentSocial
                    global currentHealth
                    global currentGrades
                    currentSocial = currentSocial + plane.social
                    currentHealth = currentHealth + plane.health
                    currentGrades = currentGrades + plane.grades
    
                    planes.Plane.dropped_upon(self, plane, coordinates)

                    plane.moving = False
                    self.count = len(self.subplanes)

                    print self.name

class DropDisplay(planes.Display):

	def dropped_upon(self, plane, coordinates):

		if isinstance(plane, Task):

			planes.Display.dropped_upon(self, plane, coordinates)

			plane.moving = False

class StatusBar(planes.Plane):
    def __init__(self, name, rect, image, draggable = False, grab = False):
        planes.Plane.__init__(self, name, rect, draggable, grab)
        self.image = image

    
#setup folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
# initialize game engine
pygame.init()
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
SECONDEVENT, t = pygame.USEREVENT+1, 1000
pygame.time.set_timer(SECONDEVENT, t)

# Load images for status bars
health0 = pygame.image.load(os.path.join(img_folder, "health0.png")).convert()
health25 = pygame.image.load(os.path.join(img_folder, "health25.png")).convert()
health50 = pygame.image.load(os.path.join(img_folder, "health50.png")).convert()
health75 = pygame.image.load(os.path.join(img_folder, "health75.png")).convert()
health100 = pygame.image.load(os.path.join(img_folder, "health100.png")).convert()
grade0 = pygame.image.load(os.path.join(img_folder, "grade0.png")).convert()
grade25 = pygame.image.load(os.path.join(img_folder, "grade25.png")).convert()
grade50 = pygame.image.load(os.path.join(img_folder, "grade50.png")).convert()
grade75 = pygame.image.load(os.path.join(img_folder, "grade75.png")).convert()
grade100 = pygame.image.load(os.path.join(img_folder, "grade100.png")).convert()
social0 = pygame.image.load(os.path.join(img_folder, "social0.png")).convert()
social25 = pygame.image.load(os.path.join(img_folder, "social25.png")).convert()
social50 = pygame.image.load(os.path.join(img_folder, "social50.png")).convert()
social75 = pygame.image.load(os.path.join(img_folder, "social75.png")).convert()
social100 = pygame.image.load(os.path.join(img_folder, "social100.png")).convert()

healthRect = health0.get_rect()
healthRect.topleft = (670, 330)
screen.sub(StatusBar("health", healthRect, health0))

socialRect = social0.get_rect()
socialRect.topleft = (670, 360)
screen.sub(StatusBar("social", socialRect, social0))

gradesRect = grade0.get_rect()
gradesRect.topleft = (670, 300)
screen.sub(StatusBar("grades", gradesRect, grade0))
# Create Task List
screen.sub(TaskList("TaskList", pygame.Rect((15, 200), (135, 215)), draggable = False, grab = True))
screen.TaskList.image.fill((228, 255, 250))

# Create trash Can
screen.sub(Trash("Trash", pygame.Rect((105, 420), (35, 40))))
#screen.Trash.image.fill((0, 0, 0))

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

# LEVEL 1

# Goals
healthGoal = 93.0
gradesGoal = 85.0
socialGoal = 66.0
currentSocial = 0
currentGrades = 0
currentHealth = 0

# Time
timeAllowed = 120
# Create tasks
numberOfTasks = 10
task1 = pygame.image.load(os.path.join(img_folder, "Apply for some jobs.png")).convert()
task2 = pygame.image.load(os.path.join(img_folder, "Clean your apartment.png")).convert()
task3 = pygame.image.load(os.path.join(img_folder, "Coffee break.png")).convert()
task4 = pygame.image.load(os.path.join(img_folder, "Discussion board post.png")).convert()
task5 = pygame.image.load(os.path.join(img_folder, "Do sit-ups in between classes.png")).convert()
task6 = pygame.image.load(os.path.join(img_folder, "Get blackout drunk.png")).convert()
task7 = pygame.image.load(os.path.join(img_folder, "Get your flu shot.png")).convert()
task8 = pygame.image.load(os.path.join(img_folder, "Go dancing.png")).convert()
task9 = pygame.image.load(os.path.join(img_folder, "Go out for a drink.png")).convert()
task10 = pygame.image.load(os.path.join(img_folder, "Go out for ice cream.png")).convert()
task11 = pygame.image.load(os.path.join(img_folder, "Research for English paper.png")).convert()
task12 = pygame.image.load(os.path.join(img_folder, "Weekly English paper .png")).convert()
task13 = pygame.image.load(os.path.join(img_folder, "Interview for journalism.png")).convert()
task14 = pygame.image.load(os.path.join(img_folder, "Work on coding website.png")).convert()
task15 = pygame.image.load(os.path.join(img_folder, "Study for Exam .png")).convert()
task16 = pygame.image.load(os.path.join(img_folder, "Skip lecture to sleep in.png")).convert()
task17 = pygame.image.load(os.path.join(img_folder, "Grab lunch with friends.png")).convert()
task18 = pygame.image.load(os.path.join(img_folder, "Pet a dog.png")).convert()
task19 = pygame.image.load(os.path.join(img_folder, "Go to the gym.png")).convert()
task20 = pygame.image.load(os.path.join(img_folder, "Walk the dog.png")).convert()
task21 = pygame.image.load(os.path.join(img_folder, "Make a salad.png")).convert()
task22 = pygame.image.load(os.path.join(img_folder, "Order a pizza, you deserve it.png")).convert()
task23 = pygame.image.load(os.path.join(img_folder, "Sleep the day away.png")).convert()
task24 = pygame.image.load(os.path.join(img_folder, "Skip class .png")).convert()
task25 = pygame.image.load(os.path.join(img_folder, "Stay up all night studying.png")).convert()
task26 = pygame.image.load(os.path.join(img_folder, "Spend some time with family.png")).convert()
task27 = pygame.image.load(os.path.join(img_folder, "Clean your apartment.png")).convert()
task28 = pygame.image.load(os.path.join(img_folder, "Go to spin class.png")).convert()
task29 = pygame.image.load(os.path.join(img_folder, "Skip breakfast to sleep in.png")).convert()
task30 = pygame.image.load(os.path.join(img_folder, "Order take out.png")).convert()
task31 = pygame.image.load(os.path.join(img_folder, "Weekly science homework.png")).convert()
task32 = pygame.image.load(os.path.join(img_folder, "Weekly math homework.png")).convert()
tasks = [task5, task6, task7, task8, task9, task10, task11, task12, task13, task14, task15, task16, task17,
         task18, task19, task20, task21, task22, task23, task24, task25, task26, task27, task28, task29, task30,
         task31, task32]
social = [0, 30, 0, 16, 10, 6, 0, 0, 10, 0, 0, 0, 20, 0, 0, 0, 0, 0, -10, 20, 0, 10, 0, 10, 0, 0, 0, 0]
health = [20, -20, 20, 10, -4, 4, 0, 0, 0, 0, 0, 10, 0, 6, 30, 20, 10, -10, 16, 0, -10, 0, 10, 20, 10, -10, 0, 0]
grades = [0, 0, 0, 0, 0, 0, 20, 20, 20, 20, 20, -10, 0, 0, 10, 0, 0, 0, -10, -10, 20, 0, 0, 0, 0, 0, 20, 20]


# Load the first four tasks into the task list
screen.TaskList.sub(Task("Task1", task1.get_rect(), task1, -5, 0, 0, draggable = True))
screen.TaskList.sub(Task("Task2", pygame.Rect((0, task2.get_height()),(task2.get_width(), task2.get_height())), task2, 2, 0, 0, draggable = True))
screen.TaskList.sub(Task("Task3", pygame.Rect((0, task3.get_height() * 2), (task3.get_width(), task3.get_height())), task3, 5, 8, 0, draggable = True))
screen.TaskList.sub(Task("Task4", pygame.Rect((0, task4.get_height() * 3), (task4.get_width(), task4.get_height())), task4, 0, 0, 10, draggable = True))
screen.TaskList.count = 4
# Hold tasks in an array.

# Loop until the user clicks close button
done = False
while done == False:
    # write event handlers here
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
        if event.type == SECONDEVENT:
            timeAllowed = timeAllowed - 1
            print str(timeAllowed)
    # write game logic here
    screen.process(events)

    if timeAllowed <= 0:
        print "Time expired! Game is over!"
        done= True
    if currentSocial >= socialGoal and currentGrades >= gradesGoal and currentHealth >= healthGoal:
        print "You met all goals! You won the game!"
        done = True
 
    # write draw code here
    if (currentHealth / healthGoal * 100.0) < 25:
        screen.health.image = health0
    elif (currentHealth / healthGoal * 100.0) > 25 and (currentHealth / healthGoal * 100) < 50:
        screen.health.image = health25
    elif (currentHealth / healthGoal * 100.0) > 50 and (currentHealth / healthGoal * 100) < 75:
        screen.health.image = health50
    elif (currentHealth / healthGoal * 100.0) > 75 and (currentHealth / healthGoal * 100) < 100:
        screen.health.image = health75
    else:
        screen.health.image = health100

    if (currentSocial / socialGoal * 100.0) < 25:
       screen.social.image = social0
    elif (currentSocial / socialGoal * 100.0) > 25 and (currentSocial / socialGoal * 100.0) < 50:
        screen.social.image = social25
    elif (currentSocial / socialGoal * 100.0) > 50 and (currentSocial / socialGoal * 100.0) < 75:
        screen.social.image = social50
    elif (currentSocial / socialGoal * 100.0) > 75 and (currentSocial / socialGoal * 100.0) < 100:
        screen.social.image = social75
    else:
        screen.social.image = social100

    if (currentGrades/ gradesGoal * 100.0) < 25:
        screen.grades.image = grade0
    elif (currentGrades / gradesGoal * 100.0) > 25 and (currentGrades / gradesGoal * 100.0) < 50:
        screen.grades.image = grade25
    elif (currentGrades / gradesGoal * 100.0) > 50 and (currentGrades / gradesGoal * 100.0) < 75:
        screen.grades.image = grade50
    elif (currentGrades / gradesGoal * 100.0) > 75 and (currentGrades / gradesGoal * 100.0) < 100:
        screen.grades.image = grade75
    else:
        screen.grades.image = grade100
    # display what is drawn here
    screen.update()
    screen.render()
    pygame.display.flip()
    # run at 20 fps
    clock.tick(60)
 
# close the window and quit
pygame.quit()
