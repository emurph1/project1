#Emily Murphy
#2017-11-1
#tic-tac-toe.py - tic-tac-toe game
from ggame import *

black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

whiteOutine = LineStyle(1, white)

blackLine1 = LineStyle(1, black)
blackLine2 = LineStyle(1, black)
blackLine3 = LineStyle(1, black)
blackLine4 = LineStyle(1, black)


Sprite(blackLine1, (200,300))
Sprite(blackLine2, (200,300))
Sprite(blackLine3, (200,300))
Sprite(blackLine4, (200,300))

#runs the game
if __name__ == '__main__':
    