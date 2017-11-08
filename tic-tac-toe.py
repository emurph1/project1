#Emily Murphy
#2017-11-1
#tic-tac-toe.py - tic-tac-toe game
from ggame import *
from random import randint

black = Color(0x000000,1)
white = Color(0xFFFFFF,1)
red = Color(0xFF0000,1)
blue = Color(0x0000FF,1)

blueOutline = LineStyle(20, blue)
whiteOutline = LineStyle(1, white)

def isEmpty(squares):
    if data['square1'] == O or data['square2'] == X:
        return False
    else: 
        return True
    if data['square2'] == O or data['square2'] == X:
        return False
    else: 
        return True 
    if data['square3'] == O or data['square3'] == X:
        return False
    else: 
        return True
    if data['square4'] == O or data['square4'] == X:
        return False
    else: 
        return True
    if data['square5'] == O or data['square5'] == X:
        return False
    else: 
        return True
    if data['square6'] == O or data['square6'] == X:
        return False
    else: 
        return True
    if data['square7'] == O or data['square7'] == X:
        return False
    else: 
        return True
    if data['square8'] == O or data['square8'] == X:
        return False
    else: 
        return True
    if data['square9'] == O or data['square9'] == X:
        return False
    else: 
        return True

#information on whether the board is full or not
def fullBoard():
    if data['square1'] and data['square2'] and data['square3'] and data['square4'] and data['square5'] and data['square6'] and data['square7'] and data['square8'] and data['square9'] == O or X:
        return True
    else:
        return False
    
#def winner():

#computer turn
def computerTurn():
    num = 3
    if num == 1:
        Sprite(redCircle,(130,100))
        Sprite(whiteCircle,(130,100))
    if num == 2:
        Sprite(redCircle,(410,100))
        Sprite(whiteCircle,(410,100))
    if num == 3:
        Sprite(redCircle,(700,100))
        Sprite(whiteCircle,(700,100))   
    
        

#click that sprites X when it is player turn
def mouseClick(event):
    if event.x < 250 and event.y <200: #square1
        Sprite(blueLine1,(70,30)) 
        Sprite(blueLine2,(70,180))
        data['square1'] += 'X'
    elif event.x < 550 and event.x > 250 and event.y <200: #square2
        Sprite(blueLine1,(350,20)) 
        Sprite(blueLine2,(350,170))
        data['square2'] += 'X'
    elif event.x < 800 and event.x > 550 and event.y < 200:#square3
        Sprite(blueLine1,(630,30)) 
        Sprite(blueLine2,(630,180))
        data['square3'] += 'X'
    elif event.x < 250 and event.y <415 and event.y >200: #square4
        Sprite(blueLine1,(70,240)) 
        Sprite(blueLine2,(70,390))
        data['square4'] += 'X'
    elif event.x < 550 and event.x > 250 and event.y < 415 and event.y > 200: #square5
        Sprite(blueLine1,(350,240)) 
        Sprite(blueLine2,(350,390))
        data['square5'] += 'X'
    elif event.x < 800 and event.x > 550 and event.y < 415 and event.y >200: #square6
        Sprite(blueLine1,(630,240)) 
        Sprite(blueLine2,(630,390))
        data['square6'] += 'X'
    elif event.x < 250 and event.y <600 and event.y > 415: #square7
        Sprite(blueLine1,(70,440)) 
        Sprite(blueLine2,(70,590))
        data['square7'] += 'X'
    elif event.x < 550 and event.x > 250 and event.y <600 and event.y > 415: #square8
        Sprite(blueLine1,(350,440)) 
        Sprite(blueLine2,(350,590))
        data['square8'] += 'X'
    elif event.x < 800 and event.x > 550  and event.y <600 and event.y > 415: #square9
        Sprite(blueLine1,(630,440)) 
        Sprite(blueLine2,(630,590))
        data['square9'] += 'X'
    computerTurn()
        
#runs the game
if __name__ == '__main__':
    
    data = {}
    data['square1'] = ''
    data['square2'] = ''
    data['square3'] = ''
    data['square4'] = ''
    data['square5'] = ''
    data['square6'] = ''
    data['square7'] = ''
    data['square8'] = ''
    data['square9'] = ''

#creates the board
    blackRect1 = RectangleAsset(826, 25, whiteOutline, black) #TOP HORIZONTAL
    blackRect2 = RectangleAsset(826, 25, whiteOutline, black) #BOTTOM HORIZONTAL
    blackRect3 = RectangleAsset(25, 600, whiteOutline, black) #LEFT VERTICAL
    blackRect4 = RectangleAsset(25, 600, whiteOutline, black) #RIGHT VERITCAL

    Sprite(blackRect1, (0,200))#TOP HORIZONTAL LINE
    Sprite(blackRect2, (0,400))#BOTTOM HORIZONAL LINE
    Sprite(blackRect3, (250,0))#THE LEFT VERITCAL LINE
    Sprite(blackRect4, (550,0)) #THE RIGHT VERTICAL LINE
    
#pieces: cirlce and 'x'
    redCircle = CircleAsset(75, whiteOutline, red) 
    whiteCircle = CircleAsset(60, whiteOutline, white)
    blueLine1 = LineAsset(120, 150, blueOutline)
    blueLine2 = LineAsset(120, -150, blueOutline)
    
App().listenMouseEvent('click',mouseClick)
App().run()