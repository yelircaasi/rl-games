"""
Creates environment for the game Lucky Numbers.
Author: Isaac Riley
Date:   November 2020
"""


import numpy as np
from itertools import product
from player import Player

class LuckyNumbers(object):
    """Creates game of Lucky Numbers"""
    def __init__(self, nplayers=2, policydict=None):
        self.nplayers = nplayers
        simple_deck = np.array(range(1, 21))
        self.deck = np.array(range(1, 21))
        for i in range(self.nplayers-2):
            self.deck = np.concatenate((self.deck, simple_deck))
        np.random.shuffle(self.deck)
        square_inds = list(product(range(4), range(4)))

        # create players
        self.players = {n: Player() for n in range(self.nplayers)}

        # define a policy for each player
        if policydict is None:
            policydict = {n: self.standard for n in range(1,self.nplayers)}
            policydict[0] = self.input
        for n in self.nplayers:
            setattr(self.players[n], "policy", policydict[n])
        self.table = []
        self.winner = None

    def play(self):
        """Runs the game from start to finish"""
        self.deal()
        player = 0

        while self.winner is None:
            self.turn(player)
            self.display()
            if self.square_finished(player):
                self.winner = player
            player = (player + 1) % self.nplayers

        print("Player {} wins.".format("ABCD"[self.winner]))

    def turn(self, pnum):
        # policy a function of squares and table
        if not self.table:
            draw = ("deck", None)
        else:
            draw = self.players[pnum].draw_policy(self.players, self.table)
        if draw[0] == "deck":
            self.deck, self.players[pnum].drawn = self.deck[:-1], self.deck[-1]
            location = self.players[pnum].loc_policy(self.players, self.deck, self.players[pnum].drawn)
            if location is None:
                self.table.append(self.players[pnum].drawn)
                self.players[pnum].drawn = None
            if not np.isnan(self.players[pnum].square[location]):
                self.table.append(self.players[pnum].square[location])
            self.players[pnum].square[location] = self.players[pnum].drawn
            self.players[pnum].drawn = None
        elif draw[0] == "table":
            self.players[pnum].drawn = self.table.pop(draw[1])
            location = self.players[pnum].loc_policy(self.players, self.deck, self.players[pnum].drawn)
            if not np.isnan(self.players[pnum].square[location]):
                self.table.append(self.players[pnum].square[location])
            self.players[pnum].square[location] = self.players[pnum].drawn
            self.players[pnum].drawn = None

    def square_finished(self, pnum):
        finished = sum(sum(np.isnan(self.players.square))) > 0
        return finished

    def deal(self):
        """
        Sets up each player' board with a number on each diagonal square.
        :return:
        """


    def display(self):
        pass

    def input(self):
        print("Please choose a move from the following options:")
        print("\tdeck  (draw from the deck)")
        print("\ttable (draw from the table)")

