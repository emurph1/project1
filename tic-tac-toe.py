#Emily Murphy
#2017-11-1
#tic-tac-toe.py - tic-tac-toe game
from ggame import *
from random import randint

black = Color(0x000000,1)
white = Color(0xFFFFFF,1)
red = Color(0xFF0000,1)
blue = Color(0x0000FF,1)
green = Color(0x00FF00,1)

blueOutline = LineStyle(20, blue)
whiteOutline = LineStyle(1, white)


 #finds the winner and says who wins
def winner():
    if (data["sq1"] == 'X' and data["sq2"] == 'X' and data["sq3"] == 'X') or \
     (data["sq4"] == 'X' and data["sq5"] == 'X' and data["sq6"] == 'X') or \
     (data["sq7"] == 'X' and data["sq8"] == 'X' and data["sq9"] == 'X') or \
     (data["sq1"] == 'X' and data["sq4"] == 'X' and data["sq7"] == 'X') or \
     (data["sq2"] == 'X' and data["sq5"] == 'X' and data["sq8"] == 'X') or \
     (data["sq3"] == 'X' and data["sq6"] == 'X' and data["sq9"] == 'X') or \
     (data["sq1"] == 'X' and data["sq5"] == 'X' and data["sq9"] == 'X') or \
     (data["sq3"] == 'X' and data["sq5"] == 'X' and data["sq7"] == 'X'):
        Sprite(pWinner, (250, 100))
    elif (data["sq1"] == 'O' and data["sq2"] == 'O' and data["sq3"] == 'O') or \
     (data["sq4"] == 'O' and data["sq5"] == 'O' and data["sq6"] == 'O') or \
     (data["sq7"] == 'O' and data["sq8"] == 'O' and data["sq9"] == 'O') or \
     (data["sq1"] == 'O' and data["sq4"] == 'O' and data["sq7"] == 'O') or \
     (data["sq2"] == 'O' and data["sq5"] == 'O' and data["sq8"] == 'O') or \
     (data["sq3"] == 'O' and data["sq6"] == 'O' and data["sq9"] == 'O') or \
     (data["sq1"] == 'O' and data["sq5"] == 'O' and data["sq9"] == 'O') or \
     (data["sq3"] == 'O' and data["sq5"] == 'O' and data["sq7"] == 'O'):
        Sprite(cWinner,(250,100))
    else:
        return False
#computer turn
def computerTurn(num):
    if num == 1 and (data["sq1"] != 'X' or data["sq1"] != 'O'):
        Sprite(redCircle,(35,20)) 
        Sprite(whiteCircle,(45,30))
        data['sq1'] = 'O'
    elif num == 2 and (data["sq2"] != 'X' or data["sq2"] != 'O'):
        Sprite(redCircle,(335,20)) 
        Sprite(whiteCircle,(345,30))
        data['sq2'] = 'O'
    elif num == 3 and (data["sq3"] != 'X' or data["sq3"] != 'O'):
        Sprite(redCircle,(625,20)) 
        Sprite(whiteCircle,(635,30))
        data['sq3'] = 'O'
    elif num == 4 and (data["sq4"] != 'X' or data["sq4"] != 'O'):
        Sprite(redCircle,(35,230)) 
        Sprite(whiteCircle,(45,240))
        data['sq4'] = 'O'
    elif num == 5 and (data["sq5"] != 'X' or data["sq5"] != 'O'):
        Sprite(redCircle,(335,230)) 
        Sprite(whiteCircle,(345,240))
        data['sq5'] = 'O'
    elif num == 6 and (data["sq6"] != 'X' or data["sq6"] != 'O'):    
        Sprite(redCircle,(625,230)) 
        Sprite(whiteCircle,(635,240))
        data['sq6'] = 'O'
    elif num == 7 and (data["sq7"] != 'X' or data["sq7"] != 'O'):  
        Sprite(redCircle,(35,430)) 
        Sprite(whiteCircle,(45,440))
        data['sq7'] = 'O'
    elif num == 8 and (data["sq8"] != 'X' or data["sq8"] != 'O'):   
        Sprite(redCircle,(335,430)) 
        Sprite(whiteCircle,(345,440))
        data['sq8'] = 'O'
    elif num == 9 and (data["sq9"] != 'X' or data["sq9"] != 'O'):
        Sprite(redCircle,(635,430))
        Sprite(whiteCircle,(645,440))
        data['sq9'] = 'O'
    else:
        computerTurn(randint(1,9))
    winner()

#click that sprites X when it is player turn
def playerX(event):
    if event.x < 250 and event.y <200 and (data["sq1"] != 'X' or data["sq1"] != 'O'): #square1
        Sprite(blueLine1,(35,10)) 
        Sprite(blueLine2,(35,10))
        data['sq1'] = 'X'
    elif event.x < 550 and event.x > 250 and event.y <200 and (data["sq2"] != 'X' or data["sq2"] != 'O'): #square2
        Sprite(blueLine1,(335,10)) 
        Sprite(blueLine2,(335,10))
        data['sq2'] = 'X'
    elif event.x < 800 and event.x > 550 and event.y < 200 and (data["sq3"] != 'X' or data["sq3"] != 'O'):#square3
        Sprite(blueLine1,(625,10)) 
        Sprite(blueLine2,(625,10))
        data['sq3'] = 'X'
    elif event.x < 250 and event.y <415 and event.y >200 and (data["sq4"] != 'X' or data["sq4"] != 'O'): #square4
        Sprite(blueLine1,(35,220)) 
        Sprite(blueLine2,(35,220))
        data['sq4'] = 'X'
    elif event.x < 550 and event.x > 250 and event.y < 415 and event.y > 200 and (data["sq5"] != 'X' or data["sq5"] != 'O'): #square5
        Sprite(blueLine1,(335,220)) 
        Sprite(blueLine2,(335,220))
        data['sq5'] = 'X'
    elif event.x < 800 and event.x > 550 and event.y < 415 and event.y >200 and (data["sq6"] != 'X' or data["sq6"] != 'O'): #square6
        Sprite(blueLine1,(625,220)) 
        Sprite(blueLine2,(625,220))
        data['sq6'] = 'X'
    elif event.x < 250 and event.y <600 and event.y > 415 and (data["sq7"] != 'X' or data["sq7"] != 'O'): #square7
        Sprite(blueLine1,(35,420)) 
        Sprite(blueLine2,(35,420))
        data['sq7'] = 'X'
    elif event.x < 550 and event.x > 250 and event.y <600 and event.y > 415 and (data["sq8"] != 'X' or data["sq8"] != 'O'): #square8
        Sprite(blueLine1,(335,420)) 
        Sprite(blueLine2,(335,420))
        data['sq8'] = 'X'
    elif event.x < 800 and event.x > 550  and event.y <600 and event.y > 415 and (data["sq9"] != 'X' or data["sq9"] != 'O'): #square9
        Sprite(blueLine1,(635,420))
        Sprite(blueLine2,(635,420))
        data['sq9'] = 'X'
    computerTurn(randint(1,9))
    winner()
    
#runs the game
if __name__ == '__main__':
    
    data = {}
    data['sq1'] = ''
    data['sq2'] = ''
    data['sq3'] = ''
    data['sq4'] = ''
    data['sq5'] = ''
    data['sq6'] = ''
    data['sq7'] = ''
    data['sq8'] = ''
    data['sq9'] = ''

        
#creates the board
    blackRect1 = RectangleAsset(826, 25, whiteOutline, black) #TOP HORIZONTAL
    blackRect2 = RectangleAsset(826, 25, whiteOutline, black) #BOTTOM HORIZONTAL
    blackRect3 = RectangleAsset(25, 600, whiteOutline, black) #LEFT VERTICAL
    blackRect4 = RectangleAsset(25, 600, whiteOutline, black) #RIGHT VERITCAL
    pWinner = TextAsset('Player Wins!! Game Over.', fill=green, style= 'bold 80pt Times')
    cWinner = TextAsset('Computer Wins!:( Game Over', fill=green, style= 'bold 80pt Times')
    nWinner = TextAsset('No one wins!:( Game Over', fill=green, style= 'bold 80pt Times')
    diffSq = TextAsset('Please choose a different square', fill = green, style = 'bold 80pt Times')
    
    Sprite(blackRect1, (0,200))#TOP HORIZONTAL LINE
    Sprite(blackRect2, (0,400))#BOTTOM HORIZONAL LINE
    Sprite(blackRect3, (250,0))#THE LEFT VERITCAL LINE
    Sprite(blackRect4, (550,0)) #THE RIGHT VERTICAL LINE
    
#pieces: cirlce and 'x'
    redCircle = CircleAsset(75, whiteOutline, red)
    whiteCircle = CircleAsset(65, whiteOutline, white)
    blueLine1 = LineAsset(120, 150, blueOutline)
    blueLine2 = LineAsset(120, -150, blueOutline)
    
    
App().listenMouseEvent('click',playerX)
App().run()
