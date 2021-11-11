"""
Runs a complete Lucky Numbers game, with one active player and the rest automated.
"""

from game import LuckyNumbers

match = LuckyNumbers(3, {0: "input", 1: "standard", 2:"standard"})
match.play()