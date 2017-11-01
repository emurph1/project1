#Emily Murphy
#2017-11-1
#tic-tac-toe.py - tic-tac-toe game
from ggame import *

black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

whiteOutine = LineStyle(1, white)

blackRect1 = RectangleAsset(800, 25, whiteOutine, black)
blackRect2 = RectangleAsset(800, 25, whiteOutine, black)
blackRect3 = RectangleAsset(25, 600, whiteOutine, black)
blackRect4 = RectangleAsset(25, 600, whiteOutine, black)


Sprite(blackRect1, (0,200))
Sprite(blackRect2, (0,400))
Sprite(blackRect3, (200,10))
Sprite(blackRect4, (400,10))


#runs the game
#if __name__ == '__main__':




App().run()