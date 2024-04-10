students = []

class student ():
    def __init__(self, firstname="Rose", lastname="Fairyrise", tnumber="T0012345",scores=[89,0,90,100]):
        self.firstName = firstname
        self.lastName = lastname
        self.tnumber = tnumber
        self.scores = scores

firstStudent = student()

def missingGrade(scores):
    for i in range(len(scores)):
        if scores[i] == 0:
            print(i)

def runningAdverage(scores):
    TOTAL = 0
    COUNT = 0
    for i in range(len(scores)):
        if scores[i] != 0:
            TOTAL += scores[i]
            COUNT += 1
    ADVERAGE = TOTAL/COUNT
    return ADVERAGE

def semesterAdverage(scores):
    TOTAL = 0
    for i in range(len(scores)):
        TOTAL += scores[i]
    ADVERAGE = TOTAL/len(scores)
    return ADVERAGE

def letterGrade(num):
    if num >= 90:
        return "A"
    elif num >= 80 and num < 90:
        return "B"
    elif num >= 70 and num < 80:
        return "C"
    elif num >= 60 and num < 70:
        return "D"
    else:
        return "F"
    

studentScores = open("Unit 10/10.Project Student Scores.txt")
readScores = studentScores.readline()

while readScores != '':
    readSheet = readScores.split(",")
    students.append(readSheet)
    readScores = studentScores.readline()

for i in range(len(students)):
    for j in range(len(students[i])):
        currentStudent = student(firstname=students[i][0], lastname=students[i][1], tnumber=students[i][2], scores=students[i][3:])
    totalNumScore = []
    for n in range (len(currentStudent.scores)):
        if currentStudent.scores[n] == '':
            totalNumScore.append(0)
        else: 
            totalNumScore.append(int(currentStudent.scores[n]))
    x = runningAdverage(totalNumScore)
    y = semesterAdverage(totalNumScore)
    z = letterGrade(y)

    print("{:>10s}{:>15s}{:>20s}{:>20s}{:>20s}{:>20s}".format("First Name", "Last Name", "ID Number", "Running Average","Semester Average", "Letter Grade"))
    print("{:>10s}{:>15s}{:>20s}{:>20f}{:>20f}{:>20s}".format(currentStudent.firstName, currentStudent.lastName, currentStudent.tnumber,x,y,z))
    
    


studentScores.close()