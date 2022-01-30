from game import *
from Views.GameView import GameView
from GameController import *


gc = GameController()

if GRAPHIC_MODE:
    gv = GameView(gc)
    sys.exit(0)
else:
    text_mode(gc)
    sys.exit(0)

