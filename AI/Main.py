from State import *
from Player import * 
if __name__ == "__main__":
    p1 = Player()
    p2 = Player()
    state = State(p1, p2)
    state.play()