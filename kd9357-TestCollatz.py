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

    def test_read(self):
        string = "1 10\n"
        beg, end = collatz_read(string)
        self.assertEqual(beg, 1)
        self.assertEqual(end, 10)

    # student added

    def test_read_1(self):
        string = "1 1\n"
        beg, end = collatz_read(string)
        self.assertEqual(beg, 1)
        self.assertEqual(end, 1)

    def test_read_2(self):
        string = "999999 500000\n"
        beg, end = collatz_read(string)
        self.assertEqual(beg, 999999)
        self.assertEqual(end, 500000)


    # ----
    # eval
    # ----

    def test_eval_1(self):
        length = collatz_eval(1, 10)
        self.assertEqual(length, 20)

    def test_eval_2(self):
        length = collatz_eval(100, 200)
        self.assertEqual(length, 125)

    def test_eval_3(self):
        length = collatz_eval(201, 210)
        self.assertEqual(length, 89)

    def test_eval_4(self):
        length = collatz_eval(900, 1000)
        self.assertEqual(length, 174)

    # student added

    def test_eval_5(self):
        length = collatz_eval(1, 1)
        self.assertEqual(length, 1)

    def test_eval_6(self):
        length = collatz_eval(1, 999999)
        self.assertEqual(length, 525)

    def test_eval_7(self):
        length = collatz_eval(360000, 360000)
        self.assertEqual(length, 167)

    def test_eval_8(self):
        length = collatz_eval(100, 210)
        self.assertEqual(length, 125)

    def test_eval_9(self):
        length = collatz_eval(23000, 42000)
        self.assertEqual(length, 324)

    def test_eval_10(self):
        length = collatz_eval(500, 16000)
        self.assertEqual(length, 276)

    # -----
    # print
    # -----

    def test_print(self):
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    # student added

    def test_print_1(self):
        writer = StringIO()
        collatz_print(writer, 100, 210, 125)
        self.assertEqual(writer.getvalue(), "100 210 125\n")

    def test_print_2(self):
        writer = StringIO()
        collatz_print(writer, 5, 5, 6)
        self.assertEqual(writer.getvalue(), "5 5 6\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # student added

    def test_solve_1(self):
        reader = StringIO("900 1000\n100 200\n1 10\n201 210\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "900 1000 174\n100 200 125\n1 10 20\n201 210 89\n")

    def test_solve_2(self):
        reader = StringIO("999999 999998\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "999999 999998 259\n")

    def test_solve_3(self):
        reader = StringIO("1 999999\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 999999 525\n")

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
