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
from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve  #, get_cycle_length, compare_max_to_current_CL


# --------------------
# Additional Functions
# --------------------


# ------------
# cycle_length
# ------------

def get_cycle_length(number):
    assert number > 0
    cycle_length = 1
    while number > 1 :
        if (number % 2) == 0 :
            number = (number // 2)
        else :
            number = (3 * number) + 1
        cycle_length += 1
    assert cycle_length > 0
    return cycle_length

# -------------------------
# compare_max_to_current_CL
# -------------------------

def compare_max_to_current_CL(current_max, current_CL):
    new_max = max(current_max, current_CL)
    assert new_max > 0
    return new_max


# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_collatz_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_collatz_read_2(self):
        s = "100 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(j, 200)

    def test_collatz_read_3(self):
        s = "201 210\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 201)
        self.assertEqual(j, 210)

    def test_collatz_read_4(self):
        s = "900 1000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 900)
        self.assertEqual(j, 1000)

    # ----
    # eval
    # ----

    def test_collatz_eval_1(self):
        max_cycle_length = collatz_eval(1, 10)
        self.assertEqual(max_cycle_length, 20)

    def test_collatz_eval_2(self):
        max_cycle_length = collatz_eval(100, 200)
        self.assertEqual(max_cycle_length,   125)

    def test_collatz_eval_3(self):
        max_cycle_length = collatz_eval(201, 210)
        self.assertEqual(max_cycle_length,    89)

    def test_collatz_eval_4(self):
        max_cycle_length = collatz_eval(900, 1000)
        self.assertEqual(max_cycle_length,    174)

    def test_collatz_eval_i_larger_j_1(self):
        max_cycle_length = collatz_eval(10, 1)
        self.assertEqual(max_cycle_length, 20)

    def test_collatz_eval_i_larger_j_2(self):
        max_cycle_length = collatz_eval(1000, 900)
        self.assertEqual(max_cycle_length,    174)

    def test_collatz_eval_i_equal_j_1(self):
        max_cycle_length = collatz_eval(10, 10)
        self.assertEqual(max_cycle_length,   7)

    def test_collatz_eval_i_equal_j_2(self):
        max_cycle_length = collatz_eval(300, 300)
        self.assertEqual(max_cycle_length,    17)

    def test_collatz_eval_i_equals_0(self):
        with self.assertRaises(AssertionError):
            max_cycle_length = collatz_eval(0,1)

    def test_collatz_eval_j_equals_0(self):
        with self.assertRaises(AssertionError):
            max_cycle_length = collatz_eval(1,0)

    # ----------------
    # get_cycle_length
    # ----------------

    def test_get_cycle_length_of_1(self):
        cycle_length = get_cycle_length(1)
        self.assertEqual(cycle_length,  1)

    def test_get_cycle_length_of_2(self):
        cycle_length = get_cycle_length(2)
        self.assertEqual(cycle_length,  2)

    def test_get_cycle_length_of_3(self):
        cycle_length = get_cycle_length(3)
        self.assertEqual(cycle_length,  8)

    def test_get_cycle_length_of_9(self):
        cycle_length = get_cycle_length(9)
        self.assertEqual(cycle_length, 20)

    def test_get_cycle_length_of_20(self):
        cycle_length = get_cycle_length(20)
        self.assertEqual(cycle_length, 8)

    def test_get_cycle_length_of_0(self):
        with self.assertRaises(AssertionError):
             cycle_length = get_cycle_length(0)

    # -------------------------
    # compare_max_to_current_CL
    # -------------------------

    def test_compare_max_to_current_CL_1_2(self):
        max_cycle_length = compare_max_to_current_CL(1,2)
        self.assertEqual(max_cycle_length, 2)
    
    def test_compare_max_to_current_CL_2_1(self):
        max_cycle_length = compare_max_to_current_CL(2,1)
        self.assertEqual(max_cycle_length, 2)

    def test_compare_max_to_current_CL_AssertionError(self):
        with self.assertRaises(AssertionError):
            max_cycle_length = compare_max_to_current_CL(0,0)

    # -----
    # print
    # -----

    def test_collatz_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_collatz_print_2(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_collatz_print_3(self):
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")

    def test_collatz_print_4(self):
        w = StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertEqual(w.getvalue(), "900 1000 174\n")

    # -----
    # solve
    # -----

    def test_collatz_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_collatz_solve_2(self):
        r = StringIO("42 59\n6 56\n3 5\n5 25\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "42 59 113\n6 56 113\n3 5 8\n5 25 21\n")

    def test_collatz_solve_3(self):
        r = StringIO("66 100\n48 200\n26 150\n487 500\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "66 100 119\n48 200 125\n26 150 122\n487 500 142\n")
    
    def test_collatz_solve_4(self):
        r = StringIO("60 52\n40 23\n40 40\n88 86\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "60 52 113\n40 23 112\n40 40 9\n88 86 31\n")

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
