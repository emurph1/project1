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


    #Sprite(redCircle,(130, 100))
    #Sprite(whiteCircle,(130, 100))
    

    #Sprite(blackLine1,(650,30))
    #Sprite(blackLine2,(650,180))
    
    
#runs the game
if __name__ == '__main__':
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

    square1 = RectangleAsset(250, 200, whiteOutline, red)
    square2 = RectangleAsset(250, 175, whiteOutline, white)
    square3 = RectangleAsset(250, 175, whiteOutline, white)
    square4 = RectangleAsset(275, 200, whiteOutline, white)
    square5 = RectangleAsset(275, 175, whiteOutline, white)
    square6 = RectangleAsset(250, 200, whiteOutline, red)
    square7 = RectangleAsset(275, 200, whiteOutline, red)
    square8 = RectangleAsset(250, 175, whiteOutline, red)
    square9 = RectangleAsset(250, 175, whiteOutline, red)
    
    Sprite(square1)
    Sprite(square2,(0,225))
    Sprite(square3,(0,425))
    Sprite(square4,(275,0))
    Sprite(square5, (275,425))
    Sprite(square6, (575,0))
    #Sprite(square7, (275,425))
    #Sprite(square8, (275,425))
    #Sprite(square9, (275,425))

#App().listenMouseEvent('click',mouseClick1)
App().run()