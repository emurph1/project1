#Emily Murphy
#2017-11-1
#tic-tac-toe.py - tic-tac-toe game
from ggame import *

black = Color(0x000000,1)
white = Color(0xFFFFFF,1)
red = Color(0xFF0000,1)
blue = Color(0x0000FF,1)

blackOutline = LineStyle(20, black)
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

def fullBoard():
    if data['square1'] and data['square2'] and data['square3'] and data['square4'] and data['square5'] and data['square6'] and data['square7'] and data['square8'] and data['square9'] == O or X:
        return True
    else:
        return False
    
#def winner():

#def computerTurn():

#click that sprites X when it is player turn
def mouseClick(Event):
    if data['square1']:
        
    if data['square2']:
        X = Sprite(blackLine1,(640,30)) and Sprite(blackLine2,(640,180))
    
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
    data['player1'] = ''
    
    
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
    blackLine1 = LineAsset(120, 150, blackOutline)
    blackLine2 = LineAsset(120, -150, blackOutline)
    
    O = Sprite(redCircle, (200,200))
    X = Sprite(blackLine1,(640,30)) and Sprite(blackLine2,(640,180))
    
App().listenMouseEvent('click',mouseClick)
App().run()