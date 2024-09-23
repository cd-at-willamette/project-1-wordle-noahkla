########################################
# Name:
# Collaborators (if any):
# GenAI Transcript (if any):
# Estimated time spent (hr):
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.

    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        w = ''
        for i in range(5):
            w += gw.get_square_letter(0, i)
        w = w.lower()
        print(w)
        if w in ENGLISH_WORDS:
            gw.show_message('Valid word!')
        else:
            gw.show_message('Not a valid word')
      

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    


# Startup boilerplate
if __name__ == "__main__":
    wordle()
