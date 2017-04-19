# Imports
import sys
import nltk

class Room():
    def __init__(self, name, description, items = None, north = None, south = None, east = None, west = None):
        self.name = name
        self.description = description
        self.items = items
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def printDescription(self):

        # Newline
        print ""
        print "You are currently in " + self.name + ". "  + self.description
        # Newline
        print ""

    def goNorth(self):
        if self.north is not None:
            global currentRoom
            currentRoom = self.north
            currentRoom.printDescription()
        else:
            print "There doesn't seem to be anything to the North"

    def goSouth(self):
        if self.south is not None:
            global currentRoom
            currentRoom = self.south
            currentRoom.printDescription()
        else:
            print "There doesn't seem to be anything to the South"

    def goEast(self):
        if self.east is not None:
            global currentRoom
            currentRoom = self.east
            currentRoom.printDescription()
        else:
            print "There doesn't seem to be anything to the East"

    def goWest(self):
        if self.west is not None:
            global currentRoom
            currentRoom = self.west
            currentRoom.printDescription()
        else:
            print "There doesn't seem to be anything to the West"

    def setNorth(self, room):
        self.north = room

    def setSouth(self, room):
        self.south = room

    def setEast(self, room):
        self.east = room

    def setWest(self, room):
        self.west = room

class Clock():
    def __init__(self, dayOfWeek, month, day, year, hours, minutes):
        self.dayOfWeek = dayOfWeek
        self.month = month
        self.day = day
        self.year = year
        self.hours = hours
        self.minutes = minutes
    def printDateAndTime(self):
        # Print date
        string = ""
        string += self.dayOfWeek
        string += ", "
        if self.month < 10:
             string += "0"
             string += str(self.month)
        else:
            string += str(self.month)
        string += "/"
        if self.day < 10:
            string += "0"
            string += str(self.day)
        else:
            string += str(self.day)
        string += "/"
        string += str(self.year)

        string += "  "

        # Print time
        if self.hours < 10:
            string += "0"
            string += str(self.hours)
        else:
            string += str(self.hours)
        string += ":"
        if self.minutes < 10:
            string += "0"
            string += str(self.minutes)
        else:
            string += str(self.minutes)
        print string

    def tick(self, minutes):
        for i in xrange(0, minutes):
            if self.minutes < 59:
                self.minutes += 1
            else:
                if self.hours < 23:
                    self.minutes = 0
                    self.hours += 1
                else:
                    self.minutes = 0
                    self.hours = 0
                    self.nextDay()

    def nextDay(self):
        if self.dayOfWeek == "Sunday":
            self.dayOfWeek = "Monday"
        elif self.dayOfWeek == "Monday":
            self.dayOfWeek = "Tuesday"
        elif self.dayOfWeek == "Tuesday":
            self.dayOfWeek = "Wednesday"
        elif self.dayOfWeek == "Wednesday":
            self.dayOfWeek = "Thursday"
        elif self.dayOfWeek == "Thursday":
            self.dayOfWeek = "Friday"
        elif self.dayOfWeek == "Friday":
            self.dayOfWeek = "Saturday"
        elif self.dayOfWeek == "Saturday":
            self.dayOfWeek = "Sunday"

        if self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10 or self.month == 12:
            if self.day < 31:
                self.day += 1
            else:
                self.day = 1
                if self.month < 12:
                    self.month += 1
                else:
                    self.month = 1
                    self.year += 1
        elif self.month == 2:
            if self.year % 4 == 0:
                if self.day < 29:
                    self.day += 1
                else:
                    self.day = 1
                    self.month = 3
            else:
                if self.day < 28:
                    self.day += 1
                else:
                    self.day = 1
                    self.month = 3
        else:
            if self.day < 29:
                self.day += 1
            else:
                self.day = 1
                self.month += 1
        
def turnInEssay(number):
    global essay1Submitted
    global essay2Submitted
    global essay3Submitted
    global essay1Grade
    global essay2Grade
    global essay3Grade
    global essay1Goal
    global essay2Goal
    global essay3Goal
    global workOnEssay1
    global workOnEssay2
    global workOnEssay3

    if number == 1 and essay1Submitted:
        print "You already submitted Essay 1"
        return
    elif number == 2 and essay2Submitted:
        print "You already submitted Essay 2"
        return
    elif number == 3 and essay3Submitted:
        print "You already submitted Essay 3"
        return
    
    if number == 1:
        goal = essay1Goal
        actual = workOnEssay1
    elif number == 2:
        goal = essay2Goal
        actual = workOnEssay2
    elif number == 3:
        goal = essay3Goal
        actual = workOnEssay3

    percentage = (actual / goal) * 100

    if percentage >= 90:
        print "You gat an A!"
        if number == 1:
            essay1Submitted = True
            essay1Grade = 'A'
        elif number == 2:
            essay2Submitted = True
            essay2Grade = 'A'
        elif number == 3:
            essay3Submitted = True
            essay3Grade = 'A'
    elif percentage < 90 and percentage >= 80:
        print "You got a B."
        if number == 1:
            essay1Submitted = True
            essay1Grade = 'B'
        elif number == 2:
            essay2Submitted = True
            essay2Grade = 'B'
        elif number == 3:
            essay3Submitted = True
            essay3Grade = 'B'
    elif percentage < 80 and percentage >= 70:
        print "You got a C."
        if number == 1:
            essay1Submitted = True
            essay1Grade = 'C'
        elif number == 2:
            essay2Submitted = True
            essay2Grade = 'C'
        elif number == 3:
            essay3Submitted = True
            essay3Grade = 'C'
    elif percentage < 70 and percentage >= 60:
        print "You got a D."
        if number == 1:
            essay1Submitted = True
            essay1Grade = 'D'
        elif number == 2:
            essay2Submitted = True
            essay2Grade = 'D'
        elif number == 3:
            essay3Submitted = True
            essay3Grade = 'D'
    else:
        print "You got an F."
        if number == 1:
            essay1Submitted = True
            essay1Grade = 'F'
        elif number == 2:
            essay2Submitted = True
            essay2Grade = 'F'
        elif number == 3:
            essay3Submitted = True
            essay3Grade = 'F'

    

def turnInProject(number):
    pass
    
        


# Print menu
print "\nWelcome to Ace Your Finals. An interactive fiction written by Dustin Teel using Python and NLTK!"

print "You are on the campus of West Virginia University.  It is your final semester; it is dead week."
print "You have three finals to study for, three projects to complete, and three essays to write."
print "Each turn takes 5 minutes to complete.  Finish all of your work before May 5, 2017 at 23:59 and before their individual due dates.  Good luck!"

# Start game loop
continueGame = True

# Create initial rooms
CROSS = Room("Evansdale Crossing", "Retail building that contains restaurants, classrooms, and shops.")
PRT = Room("Personal Rapid Transit Station", "The Engineering PRT Station.")
MRB = Room("Mineral Resources Building", "Classroom building")
ESB = Room("Engineering Sciences Building", "Classroom building")
ERB = Room("Engineering Research Building", "Office building")
NRCCE = Room("Classroom Building", "Classroom Building")
LIB = Room("Evansdale Library", "A place to study")
AERB = Room("Advanced Engineering Reserach Building", "The main building for the computer science department.")
ASB = Room("Ag Sciences Building", "Classroom Building")
SASB = Room("South Ag Sciences Building", "Classroom Buidling")
NASB = Room("New Ag Sciences Building", "Classroom Building")
PERC = Room("Percival Hall", "Classroom Building")
ALLEN = Room("Allen Hall", "Classroom Building")

TOWERSPRT = Room("Towers PRT", "Your hub to Towers")
TOWERS = Room("Towers", "A place to sleep")

# Set room directions
CROSS.setSouth(PRT)
PRT.setNorth(CROSS)
PRT.setSouth(MRB)
MRB.setNorth(PRT)
MRB.setSouth(ESB)
MRB.setEast(AERB)
ESB.setNorth(MRB)
ESB.setEast(ERB)
ERB.setWest(ESB)
ERB.setEast(NRCCE)
NRCCE.setWest(ERB)
NRCCE.setEast(LIB)
LIB.setWest(NRCCE)
LIB.setNorth(AERB)
LIB.setEast(SASB)
AERB.setWest(MRB)
AERB.setEast(ASB)
AERB.setSouth(LIB)
ASB.setWest(AERB)
ASB.setEast(ALLEN)
ASB.setSouth(SASB)
SASB.setWest(LIB)
SASB.setNorth(ASB)
SASB.setEast(NASB)
NASB.setWest(SASB)
NASB.setEast(PERC)
PERC.setWest(NASB)
PERC.setNorth(ALLEN)
ALLEN.setWest(ASB)
ALLEN.setSouth(PERC)
TOWERSPRT.setSouth(TOWERS)
TOWERS.setNorth(TOWERSPRT)


currentRoom = AERB

currentRoom.printDescription()

# Create clock
clock = Clock("Saturday", 4, 22, 2017, 23, 0);

print "Type (h)elp for a hint."


# Variables to hold progress:
studyExam1 = 0
studyExam2 = 0
studyExam3 = 0

exam1Goal = 60.0
exam2Goal = 120.0
exam3Goal = 90.0

exam1Time = [5, 1, 2017, 14, 0]
exam2Time = [5, 3, 2017, 8, 0]
exam3Time = [5, 5, 2017, 19, 0]

workOnEssay1 = 0
workOnEssay2 = 0
workOnEssay3 = 0

essay1Goal = 100.0
essay2Goal = 90.0
essay3Goal = 60.0

essay1Submitted = False
essay2Submitted = False
essay3Submitted = False

essay1Grade = ' '
essay2Grade = ' '
essay3Grade = ' '

essay1Due = [4, 24, 2017, 23, 59]
essay2Due = [4, 25, 2017, 23, 59]
essay3Due = [4, 26, 2017, 23, 59]

workOnProject1 = 0
workOnProject2 = 0
workOnProject3 = 0

project1Goal = 60.0
project2Goal = 90.0
project3Goal = 120.0

project1Due = [4, 24, 2017, 23, 59]
project2Due = [4, 26, 2017, 23, 59]
project3Due = [4, 28, 2017, 23, 59]


while continueGame:
    # Prompt user for input and read user input
    input = raw_input(">")

    # Process input (First using known commands)
    if input == "h" or input == "help":
        print "Welcome to help!"
        print "You can use the following commands:"
        print "(l)ook will give you a description of where you are"
        print "e(x)amine <item> will give you a description of an item"
        print "schedule will show you your due dates and exam times."
        print "(t)ime will tell you the current day and time"
        print "You can move through the world using (n)orth, (s)outh, (e)ast, and (w)est."
        print "The challenge is to find out which additional commands allow you to accomplish your goals."
    elif input == "l" or input == "look":
        currentRoom.printDescription()
    elif input == "schedule":
        print "\nYour schedule:"
        print "04/24/2017"
        print "Project 1 due at 23:59 on eCampus"
        print "Essay 1 due at 23:59 on eCampus"
        print "04/25/2017"
        print "Essay 2 due at 23:59 on eCampus"
        print "04/26/2017"
        print "Project 2 due at 23:59 on eCampus"
        print "Essay 3 due at 23:59 on eCampus"
        print "04/28/2017"
        print "Project 3 due at 23:59 on eCampus"
        print "05/01/2017"
        print "Exam 1 at 14:00 in ESB"
        print "05/03/2017"
        print "Exam 2 at 08:00 in AERB"
        print "05/05/2017"
        print "Exam 3 at 19:00 in ESB"
    elif input == "t" or input == "time":
        clock.printDateAndTime()
    elif input == "n" or input == "north":
        currentRoom.goNorth()
    elif input == "s" or input == "south":
        currentRoom.goSouth()
    elif input == "e" or input == "east":
        currentRoom.goEast()
    elif input == "w" or input == "west":
        currentRoom.goWest()
    else:
        tokens = nltk.word_tokenize(input)
        if "study" in tokens and "exam" in tokens:
            if "1" in tokens or "one" in tokens:
                if currentRoom is LIB:
                    # Study for exam
                    print "You just studied for Exam 1!"
                    studyExam1 += 5
                else:
                    print "You can't study here!"
            elif "2" in tokens or "two" in tokens:
                if currentRoom is LIB:
                    # Study for exam
                    print "You just studied for Exam 2!"
                    studyExam2 += 5
                else:
                    print "You can't study here!"
            elif "3" in tokens or "three" in tokens:
                if currentRoom is LIB:
                    # Study for exam
                    print "You just studied for Exam 3!"
                    studyExam3 += 5
        elif "work" in tokens and "project" in tokens:
            if "1" in tokens or "one" in tokens:
                if currentRoom is AERB:
                    # Work on project
                    print "You just worked on your Computer Science Project (Project 1)!"
                    workOnProject1 += 5
                else:
                    print "You can't work on a Computer Science project here!"
            elif "2" in tokens or "two" in tokens:
                if currentRoom is PERC:
                    # Work on project
                    print "You just worked on your English Project (Project 2)!"
                    workOnProject2 += 5
                else:
                    print "You can't work on an Engligh Project here!"
            elif "3" in tokens or "three" in tokens:
                if currentRoom is ERB:
                    # Work on project
                    print "You just worked on your Computer Engineering Research Project (Project 3)!"
                    workOnProject3 += 5
                else:
                    print "You can't work on a Computer Engineering Research Project here!"
        elif ("work" in tokens or "write" in tokens or "type" in tokens) and "essay" in tokens:
            if "1" in tokens or "one" in tokens:
                if essay1Submitted:
                    print "You already submitted Essay 1!"
                else:
                    workOnEssay1 += 5
                    print "You just worked on Essay 1!"
            elif "2" in tokens or "two" in tokens:
                if essay2Submitted:
                    print "You already submitted Essay 2!"
                else:
                    workOnEssay2 += 5
                    print "You just worked on Essay 2!"
            elif "3" in tokens or "three" in tokens:
                if essay3Submitted:
                    print "You already submitted Essay 3!"
                else:
                    workOnEssay3 += 5
                    print "You just worked on Essay 3!"
        elif "submit" in tokens or ("turn" in tokens and "in" in tokens):
            if "essay" in tokens:
                if "1" in tokens or "one" in tokens:
                    turnInEssay(1)
                elif "2" in tokens or "two" in tokens:
                    turnInEssay(2)
                elif "3" in tokens or "three" in tokens:
                    turnInEssay(3)
                else:
                    print "Tell me which essay next time"
            elif "project" in tokens:
                if "1" in tokens or "one" in tokens:
                    turnInProject(1)
                elif "2" in tokens or "two" in tokens:
                    turnInProject(2)
                elif "3" in tokens or "three" in tokens:
                    turnInProject(3)
        else:
            print "I'm afraid I do not understand your command."
                    

    clock.tick(5)
    

    
