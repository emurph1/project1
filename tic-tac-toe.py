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

#creates the board
blackRect1 = RectangleAsset(900, 25, whiteOutline, black)
blackRect2 = RectangleAsset(900, 25, whiteOutline, black)
blackRect3 = RectangleAsset(25, 600, whiteOutline, black)
blackRect4 = RectangleAsset(25, 600, whiteOutline, black)

#Sprite(blackRect1, (0,200))
#Sprite(blackRect2, (0,400))
#Sprite(blackRect3, (250,10))
#Sprite(blackRect4, (600,10))

#pieces: cirlce and 'x'
redCircle = CircleAsset(75, whiteOutline, red)
whiteCircle = CircleAsset(60, whiteOutline, white)
blackLine1 = LineAsset(70, 100, blackOutline)
blackLine2 = LineAsset(70, -100, blackOutline)


Sprite(blackLine1,(600,50))
Sprite(blackLine2,(600,150))
Sprite(redCircle,(130, 100))
Sprite(whiteCircle,(130, 100))

#runs the game
#if __name__ == '__main__':




App().run()