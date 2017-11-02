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

#def isEmpty:
    

#runs the game
if __name__ == '__main__':
#creates the board
    blackRect1 = RectangleAsset(900, 25, whiteOutline, black)
    blackRect2 = RectangleAsset(900, 25, whiteOutline, black)
    blackRect3 = RectangleAsset(25, 600, whiteOutline, black)
    blackRect4 = RectangleAsset(25, 600, whiteOutline, black)
    sideSquare1 = RectangleAsset(250, 200, whiteOutline, red)
    sideSquare2 = RectangleAsset(250, 175, whiteOutline, red)
    sideSquare3 = RectangleAsset(250, 175, whiteOutline, red)
    middleSquare1 = RectangleAsset(275, 200, whiteOutline, red)
    middleSquare2 = RectangleAsset(275, 180, whiteOutline, red)
    middleSquare3 = RectangleAsset(275, 175, whiteOutline, red)
    

    Sprite(blackRect1, (0,200))#TOP HORIZONTAL LINE
    Sprite(blackRect2, (0,400))#BOTTOM HORIZONAL LINE
    Sprite(blackRect3, (250,0))#THE LEFT VERITCAL LINE
    Sprite(blackRect4, (550,0)) #THE RIGHT VERTICAL LINE
    Sprite(sideSquare1,)
    Sprite(sideSquare2,(0,225))
    Sprite(sideSquare3,(0,425))
    Sprite(middleSquare1, (275,0))
    Sprite(middleSquare2, (275,220))
    Sprite(middleSquare3, (275,425))


#pieces: cirlce and 'x'
    redCircle = CircleAsset(75, whiteOutline, red)
    whiteCircle = CircleAsset(60, whiteOutline, white)
    blackLine1 = LineAsset(120, 150, blackOutline)
    blackLine2 = LineAsset(120, -150, blackOutline)

    Sprite(blackLine1,(700,30))
    Sprite(blackLine2,(700,180))
    Sprite(redCircle,(130, 100))
    Sprite(whiteCircle,(130, 100))

#App().listenMouseEvent('click',mouseClick)
App().run()