import time
import os
sleeptime = 0.25


#example program+board
def program():
   while True:
       forward()
       while hascorn():
           take()
       if getpos()[0] == 0:
           while cangive():
               give()
           turnRight()
           turnRight()
           for i in range(0,6):
               forward()
           break
       if getinfront() == "M":
          turnRight()
          forward()
          turnLeft()
       
           
           
startingfieldvalue = 0
usestrboard=True
strboard = ["0000000MM",
          "000000MMM",
          "00000MMMM",
          "0003MMMMM",
          "000MMMMMM",
          ">0MMMMMMM"]
board = [[0,0,0,0,0,0,"M",0,0],
        [0,0,0,0,0,"M",0,0,0],
        [0,0,0,0,"M",0,0,0,0],
        [0,0,0,"M",0,0,0,0,0],
    ["⇨",0,"M",0,0,0,0,0,0]]
def gethamster(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] in ("⇧", "⇨", "⇩", "⇦"):
                return (i, j)
def makeboard(bboard):
    b = []
    for row in bboard:
        r = []
        for letter in row:
            if letter == ">":
               r.append("⇨")
            else:
                try:
                    r.append(int(letter))
                except:
                    r.append(letter)
        b.append(r)
    return b
if usestrboard:
   board=makeboard(strboard)
cvalue = startingfieldvalue
hpos = gethamster(board)

hampster=["⇧","⇨","⇩","⇦"]
corn = 0
rotnames=["up","right","down","left"]
def gettile(x,y):
    return board[x][y]
def cangive():
    global corn
    if corn>0:
        return True
    else:
        return False
def getinfront():
    p = getpos()
    x = p[0]
    y = p[1]
    hamster = board[hpos[0]][hpos[1]]
    if hamster == "⇧":
        x-=1
    if hamster == "⇩":
        x+=1
    if hamster == "⇨":
        y+=1
    if hamster == "⇦":
        y-=1
    return gettile(x,y)
def take():
    global cvalue
    global corn
    if cvalue<=0:
        raise Exception("No corn on tile")
    cvalue-=1
    corn+=1
    printboard()
    
def give():
    global cvalue
    global corn
    if corn<=0:
        raise Exception("No corn to give")
    cvalue+=1
    corn-=1
    printboard()
    
def updatepos(newpos):
    global hpos
    global cvalue
    global board
    hamster = board[hpos[0]][hpos[1]]
    
    #check if valid
    if len(board)<=newpos[0]:
       print(board)
       raise Exception("Hit border")
       
    if len(board[0])<=newpos[1]:
       print(board)
       raise Exception("Hit border")
    newtile = board[newpos[0]][newpos[1]]
    if newtile == "M":
       raise Exception("Hit wall")
    
    time.sleep(1)
    board[hpos[0]][hpos[1]] = cvalue
    cvalue = newtile
    board[newpos[0]][newpos[1]] = hamster
    hpos = newpos
    printboard()
    
def setpos(pos):
    updatepos(pos)
def getpos():
    return hpos
def forward():
    newpos = [hpos[0],hpos[1]]
    hamster = board[hpos[0]][hpos[1]]
    if hamster == "⇧":
        newpos[0]-=1
    if hamster == "⇩":
        newpos[0]+=1
    if hamster == "⇨":
        newpos[1]+=1
    if hamster == "⇦":
        newpos[1]-=1
    updatepos(newpos)
def backwards():
    newpos = [hpos[0],hpos[1]]
    hamster = board[hpos[0]][hpos[1]]
    if hamster == "⇧":
        newpos[0]+=1
    if hamster == "⇩":
        newpos[0]-=1
    if hamster == "⇨":
        newpos[1]-=1
    if hamster == "⇦":
        newpos[1]+=1
    updatepos(newpos)
def printboard():
    global cvalue
    global corn
    os.system("cls")
    for line in board:
        for tile in line:
            #print(tile,end="")
            print(str(tile)+" ", end="")
        print()
    print()
    print("⇨ = "+str(cvalue))
    print("C = "+str(corn))
    time.sleep(sleeptime)
def hascorn():
    if cvalue>0:
        return True
    else:
        return False
def turnLeft():
    orientation = hampster.index(board[hpos[0]][hpos[1]])
    if orientation+1 == 4:
       orientation=-1
    board[hpos[0]][hpos[1]] = hampster[orientation+1]
    printboard()
    
def turnRight():
    time.sleep(1)
    orientation = hampster.index(board[hpos[0]][hpos[1]])
    if orientation-1 == -1:
       orientation=4
    board[hpos[0]][hpos[1]] = hampster[orientation-1]
    printboard()
    
def getOrientation():
    return rotnames[hampster.index(board[hpos[0]][hpos[1]])]
def setRotation(rot):
    board[hpos[0]][hpos[1]] = hampster[rotnames.index(rot)]
    printboard()
    
def getBoardLength():
    return len(board[1])-1
def getBoardDepth():
    return len(board)-1
printboard()
program()

