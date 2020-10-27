##################################################
# Name:
# Collaborators:
# Est Time spent (hrs):
##################################################

"""
Code to create a representation of a standard deck of 52
playing cards with accompanying useful methods.
"""

import random
from Prob1 import Card


# And now your code!













if __name__ == '__main__':
    # Copy of testing code from homework but
    # again I encourage you to play around and
    # test it more yourself!
    D = Deck()
    print(D)
    D.shuffle()
    print(D)
    print(D.draw())
    print(D)
    print(len(D.get_deck()))
