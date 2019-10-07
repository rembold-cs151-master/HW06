# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import mock
import pytest
import os

import Prob2
import Prob3

def numcheck(num, ans, tol=0.02):
    return (ans*(1-tol) < num < ans*(1+tol))

class Test_Prob1:
    def test_pdf_present(self):
        assert os.path.isfile('HW6.pdf') == True


class Test_Prob2:
    # ep = 0.001
    def report(self,args):
        return f"\nProgram fails to get the correct value with parameters of {args}."

    def test_is_prime(self):
        args = [3,7,12,19,25,37]
        sols = [True, True, False, True, False, True]
        for i,a in enumerate(args):
            student = Prob2.is_prime(a)
            assert student == sols[i], self.report(a)

    def test_prime_factors(self):
        args = [10,12,17,124,12252352]
        sols = [(2,5), (2,2,3), (17,), (2,2,31), (2,2,2,2,2,2,7,7,3907)]
        for i,a in enumerate(args):
            student = Prob2.prime_factors(a)
            assert student == sols[i], self.report(a)

class Test_Prob3:
    def report(self,args):
        return f"\nProgram fails to get the correct value with parameters of {args}."

    def test_get_potential_word(self):
        S = Prob3.import_search('Search.txt')
        args = [
                ((0,0), 'F', 4, S),
                ((2,0), 'D', 3, S),
                ((10,7), 'B', 6, S),
                ((17,4), 'U', 5, S),
                ((4,12), 'U', 7, S),
                ]
        sols = ['mran', 'our', 'zfbplo', 'pxbwr', None]
        for i,a in enumerate(args):
            student = Prob3.get_potential_word(*a)
            assert student == sols[i], self.report(a[0:3])

    def test_locate_word(self):
        S = Prob3.import_search('Search.txt')
        args = [
                (S, 'python'),
                (S, 'list'),
                (S, 'global'),
                (S, 'tuple'),
                ]
        sols = [
                ((3,16),'backwards'), 
                ((2,1),'down'),
                ((6,10), 'forwards'),
                ((6,18), 'down'),
                ]
        for i,a in enumerate(args):
            student = Prob3.locate_word(*a)
            assert student == sols[i], self.report(a[1])


    def test_count_main_size(self):
        wordlist = ('python', 'list', 'tuple', 'global', 'import', 'range')
        Prob3.main(wordlist)
        with open('words.txt', 'r') as f:
            lines = f.readlines()
        assert len(lines) == 6, 'Incorrect number of lines in the output file'

