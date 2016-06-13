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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        sta = "1 10\n"
        iab, jab = collatz_read(sta)
        self.assertEqual(iab,  1)
        self.assertEqual(jab, 10)

    def test_read_2(self):
        sta = "1 1\n"
        iab, jab = collatz_read(sta)
        self.assertEqual(iab, 1)
        self.assertEqual(jab, 1)

    def test_read_3(self):
        sta = "9999 10000"
        iab, jab = collatz_read(sta)
        self.assertEqual(iab, 9999)
        self.assertEqual(jab, 10000)

    def test_read_4(self):
        sta = "6 6"
        iab, jab = collatz_read(sta)
        self.assertEqual(iab, 6)
        self.assertEqual(jab, 6)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        vab = collatz_eval(1, 10)
        self.assertEqual(vab, 20)

    def test_eval_2(self):
        vab = collatz_eval(100, 200)
        self.assertEqual(vab, 125)

    def test_eval_3(self):
        vab = collatz_eval(201, 210)
        self.assertEqual(vab, 89)

    def test_eval_4(self):
        vab = collatz_eval(900, 1000)
        self.assertEqual(vab, 174)

    def test_eval_5(self):
        vab = collatz_eval(9, 9)
        self.assertEqual(vab, 20)

    def test_eval_6(self):
        vab = collatz_eval(1, 1)
        self.assertEqual(vab, 1)

    def test_eval_7(self):
        vab = collatz_eval(10, 1)
        self.assertEqual(vab, 20)

    def test_eval_8(self):
        vab = collatz_eval(1, 999999)
        self.assertEqual(vab, 525)

    def test_eval_9(self):
        vab = collatz_eval(837800, 999999)
        self.assertEqual(vab, 507)

    # 993072df7411aa9f0d35aa65ce8545ccc271d -----
    # print
    # -----

    def test_print_1(self):
        wab = StringIO()
        collatz_print(wab, 1, 10, 20)
        self.assertEqual(wab.getvalue(), "1 10 20\n")

    def test_print_2(self):
        wab = StringIO()
        collatz_print(wab, 2, 10, 20)
        self.assertEqual(wab.getvalue(), "2 10 20\n")

    def test_print_3(self):
        wab = StringIO()
        collatz_print(wab, 100, 200, 20)
        self.assertEqual(wab.getvalue(), "100 200 20\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        rab = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        wab = StringIO()
        collatz_solve(rab, wab)
        self.assertEqual(
            wab.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        rab = StringIO("1 9\n100 199\n201 209\n900 999\n")
        wab = StringIO()
        collatz_solve(rab, wab)
        self.assertEqual(
            wab.getvalue(), "1 9 20\n100 199 125\n201 209 89\n900 999 174\n")

    def test_solve_3(self):
        rab = StringIO("2 10\n101 200\n202 210\n901 1000\n")
        wab = StringIO()
        collatz_solve(rab, wab)
        self.assertEqual(
            wab.getvalue(), "2 10 20\n101 200 125\n202 210 89\n901 1000 174\n")
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
