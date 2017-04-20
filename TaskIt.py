import pygame
import os
import sys
import planes
import planes.gui
from collections import deque
from random import randint
# Define drag and drop task images
def move_up_tasks(self, plane, coordinates):
    # When a task is taken out of the task list, we need to move the remaining tasks up an insert another task
    x = 0
    for key, value in screen.TaskList.subplanes.iteritems():
        value.rect.x = 0
        value.rect.y = x * 45
        x = x + 1
    # Add a task to replace the previous task
    if len(tasksForLevel) > 0:
        screen.TaskList.sub(Task("Task" + str(screen.TaskList.currentTask), pygame.Rect((0, 45 * 3), (tasks[0].get_width(), tasks[0].get_height())), tasksForLevel[0], socialForLevel[0], healthForLevel[0], gradesForLevel[0], draggable = True))
        screen.TaskList.currentTask = screen.TaskList.currentTask + 1
        screen.TaskList.count = screen.TaskList.count + 1
        tasksForLevel.remove(tasksForLevel[0])
        socialForLevel.remove(socialForLevel[0])
        healthForLevel.remove(healthForLevel[0])
        gradesForLevel.remove(gradesForLevel[0])
        print tasksForLevel
    print "callback function"

def left_clicked(self):
        print "Clicked " + self.name
        global showStart
        global start
        global showAbout
        global showRules
        global done
        if self.name == "Play":
            showStart = False
            start = True
        elif self.name == "About":
            showStart = False
            showAbout = True
        elif self.name == "Rules":
            showStart = False
            showRules = True
        elif self.name == "Logo":
            done = True

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
    def __init__(self, name, rect, image, draggable = False, grab = False):
        planes.Plane.__init__(self, name, rect, draggable, grab)
        self.dropped_upon_callback = move_up_tasks
        self.image = image

    def dropped_upon(self, plane, coordinates):
        screen.TaskList.remove(plane)
        planes.Plane.dropped_upon(self, plane, coordinates)
       
class TaskList(planes.Plane):
    def __init__(self, name, rect, draggable = False, grab = False):
        planes.Plane.__init__(self, name, rect, draggable, grab)
        self.count = len(self.subplanes)
        self.name = name
        self.currentTask = 5

    def dropped_upon(self, plane, coordinates):
            self.count = len(self.subplanes)
            global dropSound
            pygame.mixer.music.pause()
            dropSound.play()
            pygame.mixer.music.unpause()
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
                global dropSound
                pygame.mixer.music.pause()
                dropSound.play()
                pygame.mixer.music.unpause()
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

    def dropped_upon(self, plane, coordinates):

        if isinstance(plane, Task):

            planes.Display.dropped_upon(self, plane, coordinates)

            plane.moving = False

class StatusBar(planes.Plane):
    def __init__(self, name, rect, image, draggable = False, grab = False):
        planes.Plane.__init__(self, name, rect, draggable, grab)
        self.image = image

class Button(planes.Plane):
    def __init__(self, name, rect, image, draggable = False, grab = False):
        planes.Plane.__init__(self, name, rect, draggable, grab)
        self.image = image
        self.name = name
        self.moving = False
        self.left_click_callback = left_clicked


#setup folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
audio_folder = os.path.join(game_folder, 'audio')

#Preinitialize audio mixer
pygame.mixer.pre_init(44100, -16, 2, 2048)
# initialize game engine
pygame.init()

# set screen width/height and caption
screen = DropDisplay((800, 480))
screen.grab = False
pygame.display.set_caption("Task It")
# initialize clock. used later in the loop.
clock = pygame.time.Clock()
SECONDEVENT, t = pygame.USEREVENT+1, 1000
pygame.time.set_timer(SECONDEVENT, t)

# START SCREEN

# Load the start screen

startImage = pygame.image.load(os.path.join(img_folder, "MainScreen.png")).convert()
aboutScreen = pygame.image.load(os.path.join(img_folder, "aboutscreen.jpg")).convert()
rulesScreen = pygame.image.load(os.path.join(img_folder, "rulesScreen.jpg")).convert()

playImage = pygame.image.load(os.path.join(img_folder, "play.png")).convert_alpha()
aboutImage = pygame.image.load(os.path.join(img_folder, "about.png")).convert_alpha()
rulesImage = pygame.image.load(os.path.join(img_folder, "rules.png")).convert_alpha()

# We are now going to load and start the background music
pygame.mixer.music.load(os.path.join(audio_folder, "Task_It_theme.ogg"))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Load other sounds
dropSound = pygame.mixer.Sound("drop_sound.ogg")
levelCompleteSound = pygame.mixer.Sound("level_complete.ogg")
timeExpiringSound = pygame.mixer.Sound("time_expiring.ogg")
timesUpSound = pygame.mixer.Sound("times_up.ogg")

start = False
showAbout = False
showRules = False
showStart = True
done = False
startScreenElements = False
while True:
    while not start:
        if showStart:
            screen.sub(Button("Play", pygame.Rect((130, 285), (playImage.get_width(), playImage.get_height())), playImage))
            screen.sub(Button("About", pygame.Rect((340, 295), (aboutImage.get_width(), aboutImage.get_height())), aboutImage))
            screen.sub(Button("Rules", pygame.Rect((550, 300), (rulesImage.get_width(), rulesImage.get_height())), rulesImage))
            screen.image = startImage
            startScreenElements = True
            
        while showStart:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    

            # display what is drawn here
            screen.process(events)
            screen.update()
            screen.render()
            pygame.display.flip()
            # run at 20 fps
            clock.tick(60)
        # DELETE ELEMENTS FROM START SCREEN
        if startScreenElements:
            screen.Play.destroy()
            screen.About.destroy()
            screen.Rules.destroy()
            startScreenElements = False
        
        # ABOUT SCREEN
        if showAbout:
            # Set up about screen
            screen.image = aboutScreen

        while showAbout:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                   pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    showAbout = False
                    showStart = True

            # display what is drawn here
            screen.process(events)
            screen.update()
            screen.render()
            pygame.display.flip()
            # run at 20 fps
            clock.tick(60)

        # RULES SCREEN
        if showRules:
            screen.image = rulesScreen

        while showRules:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    showRules = False
                    showStart = True

            # display what is drawn here
            screen.process(events)
            screen.update()
            screen.render()
            pygame.display.flip()
            # run at 20 fps
            clock.tick(60)


    # LOAD LEVEL IMAGES

    # Load images for status bars
    health0 = pygame.image.load(os.path.join(img_folder, "health0.png")).convert_alpha()
    health25 = pygame.image.load(os.path.join(img_folder, "health25.png")).convert_alpha()
    health50 = pygame.image.load(os.path.join(img_folder, "health50.png")).convert_alpha()
    health75 = pygame.image.load(os.path.join(img_folder, "health75.png")).convert_alpha()
    health100 = pygame.image.load(os.path.join(img_folder, "health100.png")).convert_alpha()
    grade0 = pygame.image.load(os.path.join(img_folder, "grade0.png")).convert_alpha()
    grade25 = pygame.image.load(os.path.join(img_folder, "grade25.png")).convert_alpha()
    grade50 = pygame.image.load(os.path.join(img_folder, "grade50.png")).convert_alpha()
    grade75 = pygame.image.load(os.path.join(img_folder, "grade75.png")).convert_alpha()
    grade100 = pygame.image.load(os.path.join(img_folder, "grade100.png")).convert_alpha()
    social0 = pygame.image.load(os.path.join(img_folder, "social0.png")).convert_alpha()
    social25 = pygame.image.load(os.path.join(img_folder, "social25.png")).convert_alpha()
    social50 = pygame.image.load(os.path.join(img_folder, "social50.png")).convert_alpha()
    social75 = pygame.image.load(os.path.join(img_folder, "social75.png")).convert_alpha()
    social100 = pygame.image.load(os.path.join(img_folder, "social100.png")).convert_alpha()

    # Create tasks
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
    tasks = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10, task11, task12, task13, task14, task15, task16, task17,
             task18, task19, task20, task21, task22, task23, task24, task25, task26, task27, task28, task29, task30,
             task31, task32]
    social = [-5, 2, 5, 0,  0, 30, 0, 16, 10, 6, 0, 0, 10, 0, 0, 0, 20, 0, 0, 0, 0, 0, -10, 20, 0, 10, 0, 10, 0, 0, 0, 0]
    health = [0, 0, 8, 0, 20, -20, 20, 10, -4, 4, 0, 0, 0, 0, 0, 10, 0, 6, 30, 20, 10, -10, 16, 0, -10, 0, 10, 20, 10, -10, 0, 0]
    grades = [0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 20, 20, 20, 20, 20, -10, 0, 0, 10, 0, 0, 0, -10, -10, 20, 0, 0, 0, 0, 0, 20, 20]

    #LEVEL GENERATION -- RANDOM
    #Level number - starts at 1
    level = 1
    continueGame = True
    while continueGame:
        # Show Week Number
           # NEED TO SHOW WEEK/LEVEL NUMBER
        # Time
        timeAllowed = 60.0
        timeLeft = timeAllowed

        # Select Tasks for this level
        numberOfTasks = 28
        tasksForLevel = []
        socialForLevel = []
        healthForLevel = []
        gradesForLevel = []
        for x in range(0, numberOfTasks - 1):
            randomIndex = randint(0, len(tasks) - 1)
            tasksForLevel.append(tasks[randomIndex])
            socialForLevel.append(social[randomIndex])
            healthForLevel.append(health[randomIndex])
            gradesForLevel.append(grades[randomIndex])

        # Calculate goals for this level
        healthGoal = 0.0
        gradesGoal = 0.0
        socialGoal = 0.0
        currentSocial = 0
        currentGrades = 0
        currentHealth = 0

        tempSocial = 0.0
        for score in socialForLevel:
            tempSocial = tempSocial + score

        tempGrades = 0.0
        for score in gradesForLevel:
            tempGrades = tempGrades + score

        tempHealth = 0.0
        for score in healthForLevel:
            tempHealth = tempHealth + score

        healthGoal = tempHealth / 2
        gradesGoal = tempGrades / 2
        socialGoal = tempSocial / 2

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
        trashcanimage = pygame.image.load(os.path.join(img_folder, "trash.png")).convert_alpha()
        screen.sub(Trash("Trash", pygame.Rect((105, 420), (35, 40)), trashcanimage))

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

        # Load the background image
        background = pygame.image.load(os.path.join(img_folder, "Taskitboard.png")).convert()
        goal = pygame.image.load(os.path.join(img_folder, "Goal.png")).convert_alpha()
        screen.image = background
        backgroundRect = background.get_rect()

        # Load the goal label
        screen.sub(Button("Goal", pygame.Rect((55, 20), (goal.get_width(), goal.get_height())), goal))

        # Print the goals to the screen
        myfont = pygame.font.SysFont('Comic Sans MS', 25, bold=True)
        healthLabel = myfont.render('Health: ' + str(int(healthGoal)), False, (0,0,0))
        healthPlane = planes.Plane("healthLabel", pygame.Rect((50, 50), (healthLabel.get_width(), healthLabel.get_height())))
        healthPlane.image = healthLabel
        screen.sub(healthPlane)

        gradesLabel = myfont.render("Grades: " + str(int(gradesGoal)), False, (0,0,0))
        gradesPlane = planes.Plane("gradesLabel", pygame.Rect((50, 70), (gradesLabel.get_width(), gradesLabel.get_height())))
        gradesPlane.image = gradesLabel
        screen.sub(gradesPlane)

        socialLabel = myfont.render("Social: " + str(int(socialGoal)), False, (0,0,0))
        socialPlane = planes.Plane("socialLabel", pygame.Rect((50, 90), (socialLabel.get_width(), socialLabel.get_height())))
        socialPlane.image = socialLabel
        screen.sub(socialPlane)

        # Put the end level logo/button on screen
        logo = pygame.image.load(os.path.join(img_folder, "taskitlogo.png")).convert_alpha()
        screen.sub(Button("Logo", pygame.Rect((645, 390), (logo.get_width(), logo.get_height())), logo))

        # Do a bar for the timer
        timerBar = planes.gui.ProgressBar("TimerBar", pygame.Rect((670, 265), (100, 20)), 100, text='Time Left: ' + str(int(timeLeft)), background_color=(0,0,0))
        screen.sub(timerBar)

        # Make a label for the week number
        weekLabel = myfont.render("Week " + str(level), False, (0,0,0))
        weekPlane = planes.Plane("weekLabel", pygame.Rect((670, 245), (weekLabel.get_width(), weekLabel.get_height())))
        weekPlane.image = weekLabel
        screen.sub(weekPlane)

        # Load the first four tasks into the task list
        screen.TaskList.sub(Task("Task1", task1.get_rect(), tasksForLevel[0], socialForLevel[0], healthForLevel[0], gradesForLevel[0], draggable = True))
        tasksForLevel.remove(tasksForLevel[0])
        socialForLevel.remove(socialForLevel[0])
        healthForLevel.remove(healthForLevel[0])
        gradesForLevel.remove(gradesForLevel[0])
        screen.TaskList.sub(Task("Task2", pygame.Rect((0, task2.get_height()),(task2.get_width(), task2.get_height())), tasksForLevel[0], socialForLevel[0], healthForLevel[0], gradesForLevel[0], draggable = True))
        tasksForLevel.remove(tasksForLevel[0])
        socialForLevel.remove(socialForLevel[0])
        healthForLevel.remove(healthForLevel[0])
        gradesForLevel.remove(gradesForLevel[0])
        screen.TaskList.sub(Task("Task3", pygame.Rect((0, task3.get_height() * 2), (task3.get_width(), task3.get_height())), tasksForLevel[0], socialForLevel[0], healthForLevel[0], gradesForLevel[0], draggable = True))
        tasksForLevel.remove(tasksForLevel[0])
        socialForLevel.remove(socialForLevel[0])
        healthForLevel.remove(healthForLevel[0])
        gradesForLevel.remove(gradesForLevel[0])
        screen.TaskList.sub(Task("Task4", pygame.Rect((0, task4.get_height() * 3), (task4.get_width(), task4.get_height())), tasksForLevel[0], socialForLevel[0], healthForLevel[0], gradesForLevel[0], draggable = True))
        tasksForLevel.remove(tasksForLevel[0])
        socialForLevel.remove(socialForLevel[0])
        healthForLevel.remove(healthForLevel[0])
        gradesForLevel.remove(gradesForLevel[0])
        screen.TaskList.count = 4
        # Hold tasks in an array.
        done = False
        # Loop until the user clicks close button
        while not done:
            # write event handlers here
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == SECONDEVENT:
                    timeLeft = timeLeft - 1
                    timerBar.percent = int((timeLeft / timeAllowed) * 100)
                    timerBar.text = "Time Left: " + str(int(timeLeft))
                    if timeLeft / timeAllowed == 0.25:
                        pygame.mixer.music.pause()
                        timeExpiringSound.play()
                        pygame.mixer.music.unpause()
                    timerBar.redraw()
                    timerBar.update()
            # write game logic here
            screen.process(events)

            if timeLeft <= 0:
                print "Time expired! Game is over!"
                pygame.mixer.music.pause()
                timesUpSound.play()
                pygame.mixer.music.unpause()
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

        # Load end level screen
        screen.remove_all()
        endlevel = pygame.image.load(os.path.join(img_folder, "levelcomplete.png")).convert()
        screen.image = endlevel

        finalGrade = None
        finalSocial = None
        finalHealth = None

        if (currentHealth / healthGoal * 100.0) < 25:
            finalHealth = health0
        elif (currentHealth / healthGoal * 100.0) > 25 and (currentHealth / healthGoal * 100) < 50:
            finalHealth = health25
        elif (currentHealth / healthGoal * 100.0) > 50 and (currentHealth / healthGoal * 100) < 75:
            finalHealth = health50
        elif (currentHealth / healthGoal * 100.0) > 75 and (currentHealth / healthGoal * 100) < 100:
            finalHealth = health75
        else:
            finalHealth = health100

        if (currentSocial / socialGoal * 100.0) < 25:
            finalSocial = social0
        elif (currentSocial / socialGoal * 100.0) > 25 and (currentSocial / socialGoal * 100.0) < 50:
            finalSocial = social25
        elif (currentSocial / socialGoal * 100.0) > 50 and (currentSocial / socialGoal * 100.0) < 75:
            finalSocial = social50
        elif (currentSocial / socialGoal * 100.0) > 75 and (currentSocial / socialGoal * 100.0) < 100:
            finalSocial = social75
        else:
            finalSocial = social100

        if (currentGrades/ gradesGoal * 100.0) < 25:
            finalGrade = grade0
        elif (currentGrades / gradesGoal * 100.0) > 25 and (currentGrades / gradesGoal * 100.0) < 50:
            finalGrade = grade25
        elif (currentGrades / gradesGoal * 100.0) > 50 and (currentGrades / gradesGoal * 100.0) < 75:
            finalGrade = grade50
        elif (currentGrades / gradesGoal * 100.0) > 75 and (currentGrades / gradesGoal * 100.0) < 100:
            finalGrade = grade75
        else:
            finalGrade = grade100

        
        screen.sub(StatusBar("health", pygame.Rect((320, 200), (finalHealth.get_width(), finalHealth.get_height())), finalHealth))
        screen.sub(StatusBar("social", pygame.Rect((320, 250), (finalSocial.get_width(), finalSocial.get_height())), finalSocial))
        screen.sub(StatusBar("grades", pygame.Rect((320, 150), (finalGrade.get_width(), finalGrade.get_height())), finalGrade))
        

        # END LEVEL SCREEN
        showEndLevelScreen = True
        pygame.mixer.music.pause()
        levelCompleteSound.play()
        pygame.mixer.music.unpause()
        while showEndLevelScreen:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if finalGrade is grade100 and finalSocial is social100 and finalHealth is health100:
                        showEndLevelScreen = False
                        level += 1
                        screen.remove_all()
                    else:
                        showEndLevelScreen = False
                        start = False
                        showAbout = False
                        showRules = False
                        showStart = True
                        done = True
                        continueGame = False
                        startScreenElements = False
                        screen.remove_all()

            screen.process(events)
            
            # display what is drawn here
            screen.update()
            screen.render()
            pygame.display.flip()
            # run at 20 fps
            clock.tick(60)
    
 
# close the window and quit
pygame.quit()
