import colorama1
import os
import math
import mmap
import keyboard1 
from colorama1 import Fore, Back, Style

def pos (x,y):
    return '\x1b[' + str(y) + ';' + str(x) + 'H'

up = colorama1.Cursor.UP
down = colorama1.Cursor.DOWN
forward = colorama1.Cursor.FORWARD
back = colorama1.Cursor.BACK

FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
STYLES = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]


def rgb_f(ls_rgb):
    ansi_fore_ground_rgb_str = f'\033[38;2;{str(ls_rgb[0])};{str(ls_rgb[1])};{str(ls_rgb[2])}m'
    return ansi_fore_ground_rgb_str



def rgb_b(ls_rgb):
    ansi_background_rgb_str = f'\033[48;2;{ls_rgb[0]};{ls_rgb[1]};{ls_rgb[2]}m'
    return ansi_background_rgb_str


colorama1.just_fix_windows_console()

os.system('cls')

ls_click_counter = [0]


def func_test(ls_click_counter):

    while True:

        event_ = keyboard1.read_event()

        if event_.event_type == keyboard1.KEY_DOWN:

            ls_click_counter[0] += 1
            print(pos(10,10) + str(ls_click_counter[0]))


while True:
    event_ = keyboard1.read_event()

    if event_.event_type == keyboard1.KEY_DOWN:
        
        ls_click_counter[0] += 1
        print(pos(10,10) + str(ls_click_counter[0]))

        func_test(ls_click_counter)

