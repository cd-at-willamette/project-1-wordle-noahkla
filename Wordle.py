########################################
# Name: Noah Klarreich
# Collaborators (if any): 
# GenAI Transcript (if any):
# Estimated time spent (hr): 1:30
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random
row_index = 0

def wordle():
    # The main function to play the Wordle game.
    random_word = random_five_letter_word()
    def enter_action():
        global row_index
        # What should happen when RETURN/ENTER is pressed.
        w = ''
        for i in range(5):
            w += gw.get_square_letter(row_index, i)
        w = w.lower()
        if w in ENGLISH_WORDS:
            gw.show_message('Valid word!')
            color_row(row_index, random_word)
        else:
            gw.show_message('Not a valid word')
        if w == random_word:
                gw.show_message('You Win!')
        elif gw.get_current_row() == N_ROWS-1:
            gw.show_message('You Lose! The word is: ' + random_word)
        row_index += 1
        gw.set_current_row(row_index)
      

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)


    def color_row(r, a):
        a2 = a
        correct = []
        a = list(a)
        for i in range(len(a2)):
            l = gw.get_square_letter(r, i).lower()
# If the letter is in the right spot, it collors it correct color, adds the
# index to the list of correct letter, and sets it to 0 in both a and a2
# in case there is a repeat of the letter
            if l == a[i]:
                gw.set_square_color(r, i, CORRECT_COLOR)
                gw.set_key_color(l, CORRECT_COLOR)	
             #   print(l, a[i])
                correct.append(i)
                a[i] = '0'
                a2 = ''
                for j in a:
                    a2 += j
# Then it does the for loop again, checks if each letter is in the wrong place,
# or is not in the word at all. If it is in the wrong place, it sets
# the letter to 0 in case of repeats.
        for i in range(len(a2)):
            l = gw.get_square_letter(r, i).lower()
            if i not in correct:
                if l in a:
                        gw.set_square_color(r, i, PRESENT_COLOR)
                        gw.set_key_color(l, PRESENT_COLOR)	
                        index = a2.rfind(l)
                        a[index] = '0'
                        a2 = ''
                        for j in a:
                            a2 += j
                       # print(l, a[i], index)
                else:
                    gw.set_square_color(r, i, MISSING_COLOR)
                    gw.set_key_color(l, MISSING_COLOR)
                  #  print(l, a[i])
      #  print(a)
def random_five_letter_word():
    random.shuffle(ENGLISH_WORDS)
    five_l_w = [w for w in ENGLISH_WORDS if len(w)==5]
    return five_l_w[0]
    

# Startup boilerplate
if __name__ == "__main__":
    wordle()
