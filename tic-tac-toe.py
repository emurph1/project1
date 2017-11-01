#Emily Murphy
#2017-11-1
#tic-tac-toe.py - tic-tac-toe game
from ggame import *

black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

whiteOutine = LineStyle(1, white)

blackRect1 = RectangleAsset(200, 100, whiteOutine, black)
blackRect2 = RectangleAsset(200, 100, whiteOutine, black)
blackRect3 = RectangleAsset(200, 100, whiteOutine, black)
blackRect4 = RectangleAsset(200, 100, whiteOutine, black)


Sprite(blackRect1, (200,300))
Sprite(blackRect2, (200,300))
Sprite(blackRect3, (200,300))
Sprite(blackRect4, (200,300))

#runs the game
#if __name__ == '__main__':




App().run()