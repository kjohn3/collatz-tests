#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_for_num

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        given_input = "1 10\n"
        i, j = collatz_read(given_input)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    # The following are tests that I have added.

    # Ensures that only the first two numbers are read.
    def test_read_2(self):
        given_input = "391 200 800 500\n"
        i, j = collatz_read(given_input)
        self.assertEqual(i,  391)
        self.assertEqual(j, 200)

    # Ensures that other invalid tokens don't cause problems if
    # first two tokens are valid.
    def test_read_3(self):
        given_input = "1 999 abcd efg\n"
        i, j = collatz_read(given_input)
        self.assertEqual(i,  1)
        self.assertEqual(j, 999)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        test_result = collatz_eval(1, 10)
        self.assertEqual(test_result, 20)

    def test_eval_2(self):
        test_result = collatz_eval(100, 200)
        self.assertEqual(test_result, 125)

    def test_eval_3(self):
        test_result = collatz_eval(201, 210)
        self.assertEqual(test_result, 89)

    def test_eval_4(self):
        test_result = collatz_eval(900, 1000)
        self.assertEqual(test_result, 174)

    # The following are tests that I have added.

    # Tests repeated input.
    def test_eval_5(self):
        test_result = collatz_eval(8, 8)
        self.assertEqual(test_result, 4)

    # Tests for reversed ordering of input pair.
    def test_eval_6(self):
        test_result = collatz_eval(1000, 900)
        self.assertEqual(test_result, 174)

    # Tests whether double input 1 returns 1.
    def test_eval_7(self):
        test_result = collatz_eval(1, 1)
        self.assertEqual(test_result, 1)

    # These tests check the helper function
    def test_cycle_1(self):
        test_result = cycle_for_num(1)
        self.assertEqual(test_result, 1)

    def test_cycle_2(self):
        test_result = cycle_for_num(837799)
        self.assertEqual(test_result, 525)

    def test_cycle_3(self):
        test_result = cycle_for_num(500000)
        self.assertEqual(test_result, 152)

    # -----
    # print
    # -----

    def test_print(self):
        receiver = StringIO()
        collatz_print(receiver, 1, 10, 20)
        self.assertEqual(receiver.getvalue(), "1 10 20\n")

    # I have added the following tests.

    def test_print_2(self):
        receiver = StringIO()
        collatz_print(receiver, 999999, 999999, 999999)
        self.assertEqual(receiver.getvalue(), "999999 999999 999999\n")

    def test_print_3(self):
        receiver = StringIO()
        collatz_print(receiver, 111, 11, 1)
        self.assertEqual(receiver.getvalue(), "111 11 1\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        input_strings = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        output_strings = StringIO()
        collatz_solve(input_strings, output_strings)
        self.assertEqual(
            output_strings.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # I have added the following tests.

    def test_solve_2(self):
        input_strings = StringIO("8 8\n1000 900\n1 1\n")
        output_strings = StringIO()
        collatz_solve(input_strings, output_strings)
        self.assertEqual(
            output_strings.getvalue(), "8 8 4\n1000 900 174\n1 1 1\n")

    # Tests solve on only one line input.
    def test_solve_3(self):
        input_strings = StringIO("1 10\n")
        output_strings = StringIO()
        collatz_solve(input_strings, output_strings)
        self.assertEqual(
            output_strings.getvalue(), "1 10 20\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
