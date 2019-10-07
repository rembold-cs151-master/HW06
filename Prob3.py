##################################################
# Name:
# Collaborators:
# Est Time Spent (hrs):
##################################################


def import_search(file_name):
    """
    Function which reads in a space delimited block of letters
    and saves them in a tuple of tuples.

    Inputs:
        - file_name (str): filename to be read
    Outputs:
        - (tuple): tuple of tuples, where the inner tuples are lists
                   of the values in each row

    YOU DON'T NEED TO TOUCH THIS FUNCTION
    """
    search = []
    f = open(file_name, 'r')
    for line in f:
        line_tuple = tuple(line.strip().split(' '))
        search.append(line_tuple)
    return tuple(search)



def get_potential_word(start_loc, direction, length, search_tuple):
    """
    Helper function to return the sequence of letters in the wordsearch
    starting at a particular point and extending for some length in some
    specified direction.

    Inputs:
        - start_loc (tuple of 2 ints): row and column index where the word starts
        - direction (str): Capitalized first letter corresponding to forward,
                           backward, up, or down
        - length (int): length of the potential word to be searched
        - search_tuple (tuple of (tuple of str)): the data that makes up the word
                                                  search area.
    Outputs:
        - (str): the word starting at the desired point and extending for length
                 in the direction requested. If close to the borders so that the
                 desired word goes out-of-bounds, None should be returned.

    Usage:
        >>> get_potential_word((0,0), 'F', 4, S)
        'mran'
        >>> get_potential_word((2,0), 'D', 3, S)
        'our'
    """
    pass # <-- comment out and add your code below!


def locate_word(search_tuple, word):
    """
    Helper function to search the tuple systematically for the presence to the
    desired word. Can use nested for loops to loop through row and columns, and
    in starting point check using `get_potential_word` if the words extending
    forwards, backwords, up or down from that starting point match the desired
    word.

    Inputs:
        - search_tuple (tuple of (tuple of str)): the word search data
        - word (str): the word to be searched for
    Outputs:
        - location (tuple of 2 int): the row and column of the found word
        - direction (str): the direction of the found word ('forwards', 'backwards',
                           'up' or 'down')

    Usage:
        >>> locate_word(S, 'python')
        ((3,16), 'backwards')
    """
    pass # <-- comment out and add your code below!


def main(wordlist, file_name = 'Search.txt'):
    """
    Function to search the text of Search.txt for words contained within the
    desired wordlist. Writes words, their found starting location, and direction
    to the text file 'words.txt'. If the above helper functions have gone well, this
    should be a simple matter of looping through the desired words, finding each
    with the previously defined functions, and then writing the results to a file.
    
    Inputs:
        - file_name (str): Filename of txt file containing wordsearch letters.
                           Defaults to 'Search.txt'
        - wordlist (tuple of strings): Tuple of the words that the user wishes
                                       to find within the wordsearch.

    Outputs:
        - Results should be written to the file 'words.txt'
    """

    S = import_search(file_name)






if __name__ == '__main__':
    wordlist = ('python', 'list', 'tuple', 'global', 'import', 'range')
    main(wordlist)
