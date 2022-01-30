import sys
from game import *
from util import *
from consts import *
from Views.GameView import GameView
from GameController import *
from solver import *


gc = GameController()

if GRAPHIC_MODE:
    gv = GameView(gc)
    sys.exit(0)
else:
    text_mode(gc)
    sys.exit(0)

