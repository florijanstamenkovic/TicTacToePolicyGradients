#!/usr/bin/python3

import argparse
import logging
from itertools import count

import board
import player


def main():
    """ A manual test of the Board logic. """

    parser = argparse.ArgumentParser(description='Five-in-a-row Board test')
    parser.add_argument('--board-side', type=int, default=3,
                        help='number of tiles on one side of the board')
    parser.add_argument('--win-row', type=int, default=3,
                        help='number of same-in-a-row for win')
    parser.add_argument('--player', default='random',
                        help='the player used during testing')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    b = board.Board(args.board_side)
    def print_board():
        def player_sym(ind):
            if ind == 0:
                return " "
            if ind == 1:
                return "X"
            if ind == 2:
                return "O"

        for row in range(b.side):
            if row != 0:
                print("-+" * (b.side - 1) + "-")
            print("|".join(player_sym(x) for x in b.board[row]))


    winner = None
    for move_ind in count():
        current = 1 + move_ind % 2
        move = player.for_name(args.player)(current, b)
        b.place_move(*move, current)
        logging.info("Board after move %d", move_ind)
        print_board()
        winner = b.check_winner(args.win_row, *move)
        if winner is None and len(b.available) == 0:
            winner = 0
        if winner is not None:
            print("Winner:", winner)
            break


if __name__ == '__main__':
    main()
