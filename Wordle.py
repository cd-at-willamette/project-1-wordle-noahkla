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
        if w in ENGLISH_WORDS:
            gw.show_message('Valid word!')
        else:
            gw.show_message('Not a valid word')
        color_row(0, 'glass')
      

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)


    def color_row(r, a):
        a2 = a
        correct = []
        a = list(a)
        for i in range(len(a2)):
            l = gw.get_square_letter(r, i).lower()
            if l == a[i]:
                gw.set_square_color(r, i, CORRECT_COLOR)
             #   print(l, a[i])
                correct.append(i)
                a[i] = '0'
                a2 = ''
                for j in a:
                    a2 += j
        for i in range(len(a2)):
            l = gw.get_square_letter(r, i).lower()
            if i not in correct:
                if l in a:
                        gw.set_square_color(r, i, PRESENT_COLOR)
                        index = a2.rfind(l)
                        a[index] = '0'
                        a2 = ''
                        for j in a:
                            a2 += j
                       # print(l, a[i], index)
                else:
                    gw.set_square_color(r, i, MISSING_COLOR)
                  #  print(l, a[i])
      #  print(a)

# Startup boilerplate
if __name__ == "__main__":
    wordle()
