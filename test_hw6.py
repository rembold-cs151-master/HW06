# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import mock
import pytest
import os

import Prob3

def numcheck(num, ans, tol=0.02):
    return (ans*(1-tol) < num < ans*(1+tol))

class Test_Prob1:
    def test_pdf_present(self):
        assert os.path.isfile('HW6.pdf') == True


class Test_Prob3:
    # ep = 0.001
    def report(self,args):
        return f"\nProgram fails to get the correct value with parameters of {args}."

    def test_is_prime(self):
        args = [3,7,12,19,25,37]
        sols = [True, True, False, True, False, True]
        for i,a in enumerate(args):
            student = Prob3.is_prime(a)
            assert student == sols[i], self.report(a)

    def test_returns_a_tuple(self):
        args = [7,10,12]
        for a in args:
            student = Prob3.prime_factors(a)
            assert type(student) == tuple, f"\nA tuple is not returned with prime_factors({a})!"

    def test_prime_factors(self):
        args = [10,12,17,124,12252352]
        sols = [(2,5), (2,2,3), (17,), (2,2,31), (2,2,2,2,2,2,7,7,3907)]
        for i,a in enumerate(args):
            student = Prob3.prime_factors(a)
            assert student == sols[i], self.report(a)

