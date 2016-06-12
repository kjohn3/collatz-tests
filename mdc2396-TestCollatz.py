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

    def test_read1(self):
        readval = "1 10\n"
        i, j = collatz_read(readval)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read2(self):
        readval = "3 6\n"
        i, j = collatz_read(readval)
        self.assertEqual(i,  3)
        self.assertEqual(j, 6)

    def test_read3(self):
        readval = "100 200\n"
        i, j = collatz_read(readval)
        self.assertEqual(i,  100)
        self.assertEqual(j, 200)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        value = collatz_eval(1, 10)
        self.assertEqual(value, 20)

    def test_eval_2(self):
        value = collatz_eval(100, 200)
        self.assertEqual(value, 125)

    def test_eval_3(self):
        value = collatz_eval(201, 210)
        self.assertEqual(value, 89)

    def test_eval_4(self):
        value = collatz_eval(900, 1000)
        self.assertEqual(value, 174)


    def test_eval_5(self):
        value = collatz_eval(2, 1)
        self.assertEqual(value, 2)

    # -----
    # print
    # -----

    def test_print1(self):
        pnt = StringIO()
        collatz_print(pnt, 1, 10, 20)
        self.assertEqual(pnt.getvalue(), "1 10 20\n")

    def test_print2(self):
        pnt = StringIO()
        collatz_print(pnt, 1, 6, 9)
        self.assertEqual(pnt.getvalue(), "1 6 9\n")

    def test_print3(self):
        pnt = StringIO()
        collatz_print(pnt, 900, 1000, 174)
        self.assertEqual(pnt.getvalue(), "900 1000 174\n")

    # -----
    # solve
    # -----

    def test_solve1(self):
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2(self):
        reader = StringIO("1 3\n4 6\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 3 8\n4 6 9\n")

    def test_solve3(self):
        reader = StringIO("1 6\n4 10\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 6 9\n4 10 20\n")

    def test_solve4(self):
        reader = StringIO("2 1\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "2 1 2\n")

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