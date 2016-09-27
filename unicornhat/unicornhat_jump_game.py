"""
Lyle Scott, III
lyle@digitalfoo.net

pip install unicornhat readchar
"""
from datetime import datetime
from threading import Thread
import random
import sys
import time

import readchar
import unicornhat as uhat


N_DUDES = 3


def _draw_dudes():
    dudes = []
    while True:
        time.sleep(.29)
        print(dudes)
        for dude in list(dudes):
            uhat.set_pixel(dude, 2, 0, 0, 0)
            dudes.remove(dude)
            if dude != 7:
                dudes.append(dude + 1)
        uhat.show()

        for dude in dudes:
            uhat.set_pixel(dude, 2, 0, 0, 255)
        uhat.show()

        if (len(dudes) < N_DUDES and           # No more than N dudes.
            1 not in dudes and                 # Don't let them repeat.
            random.randint(1, 9) % 2 == 0 and  # Add variability to
            random.randint(1, 9) % 2 == 0):    # generating a dude.
            dudes.append(0)
            uhat.set_pixel(0, 2, 0, 0, 255)
        uhat.show()


class Player(object):

    def __init__(self):
        uhat.set_layout(uhat.AUTO)
        uhat.rotation(0)
        uhat.brightness(0.4)
        self.board_width, self.board_height = uhat.get_shape()
        self.board_width -= 1
        self.board_height -= 1

        self.draw_board()

        self.cur_pos_x = 0
        self.cur_pos_y = 2
        self.commit_move()

        thread = Thread(target=_draw_dudes)
        thread.start()

        self.read_moves()

    def draw_board():
        for w in range(0, self.board_width + 1):
            uhat.set_pixel(w, 0, 0, 255, 0)
            uhat.set_pixel(w, 1, 0, 255, 0)
            uhat.show()

    def read_moves(self):
        while True:
            key = readchar.readkey()
            if key == readchar.key.LEFT:
                print('left')
                self.move_left()
            elif key == readchar.key.RIGHT:
                print('right')
                self.move_right()
            elif key == readchar.key.UP:
                print('up')
                self.move_up()
            elif key == 'q':
                thread.join()
                thread.close()
                sys.exit()

    def commit_move(self, y=None):
        uhat.set_pixel(7 - self.cur_pos_x, self.cur_pos_y, 255, 0, 0)
        uhat.show()

    def uncommit_move(self):
        uhat.set_pixel(7 - self.cur_pos_x, self.cur_pos_y, 0, 0, 0)
        uhat.show()

    def move_left(self):
        if self.cur_pos_x == 0:
            return
        self.uncommit_move()
        self.cur_pos_x -= 1
        self.commit_move()

    def move_right(self):
        if self.cur_pos_x == self.board_width:
            return
        self.uncommit_move()
        self.cur_pos_x += 1
        self.commit_move()

    def move_up(self):
        moves = (
            (3, .02, 1),
            (3, .04, 1),
            (4, .09, 1),
            (4, .12, 1),
            (4, .15, -1),
            (None, .11, -1),
            (None, .06, -2),
        )

        for move, sleep, y_delta in moves:
            self.uncommit_move()
            self.cur_pos_y += y_delta
            self.commit_move(move)
            time.sleep(sleep)


if __name__ == '__main__':
    Player()
