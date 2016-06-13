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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_single_eval

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        string = "1 10\n"
        i, j = collatz_read(string)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        string = "10 10"
        input1, input2 = collatz_read(string)
        self.assertEqual(input1, 10)
        self.assertEqual(input2, 10)
        self.assertEqual(input1, input2)

    def test_read_3(self):
        string = "1 999999"
        input1, input2 = collatz_read(string)
        self.assertEqual(input1, 1)
        self.assertEqual(input2, 999999)

    def test_read_4(self):
        string = "\n"
        input1, input2 = collatz_read(string)
        self.assertEqual(input1, 0)
        self.assertEqual(input2, 0)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        val = collatz_eval(999999, 999999)
        self.assertEqual(val, 259)

    def test_eval_2(self):
        val = collatz_eval(1, 10)
        self.assertEqual(val, 20)

    def test_eval_3(self):
        val = collatz_eval(100, 200)
        self.assertEqual(val, 125)

    def test_eval_4(self):
        val = collatz_eval(201, 210)
        self.assertEqual(val, 89)

    def test_eval_5(self):
        val = collatz_eval(900, 1000)
        self.assertEqual(val, 174)

    def test_eval_6(self):
        value = collatz_eval(2, 2)
        self.assertEqual(value, 2)

    def test_eval_7(self):
        value = collatz_eval(10, 10)
        self.assertEqual(value, 7)

    def test_eval_8(self):
        value = collatz_eval(1024, 1024)
        self.assertEqual(value, 11)

    def test_eval_9(self):
        self.assertRaises(AssertionError, collatz_eval, 0, 10)

    def test_eval_10(self):
        self.assertRaises(AssertionError, collatz_eval, -5, 20)

    def test_eval_11(self):
        val = collatz_eval(210, 200)
        self.assertEqual(val, 89)

    def test_eval_12(self):
        val = collatz_eval(1, 1)
        self.assertEqual(val, 1)

    def test_eval_13(self):
        val = collatz_eval(691, 707)
        self.assertEqual(val, 171)

    def test_eval_14(self):
        val = collatz_eval(596310, 596349)
        self.assertEqual(val, 98)

    def test_eval_15(self):
        val = collatz_eval(596309, 596349)
        self.assertEqual(val, 160)

    def test_eval_16(self):
        val = collatz_eval(596310, 596350)
        self.assertEqual(val, 266)

    def test_eval_17(self):
        val = collatz_eval(596309, 596350)
        self.assertEqual(val, 266)

    def test_eval_18(self):
        val = collatz_eval(8, 228366)
        self.assertEqual(val, 386)

    # -----------
    # single_eval
    # -----------

    def test_single_eval_1(self):
        val = collatz_single_eval(1)
        self.assertEqual(val, 1)

    def test_single_eval_2(self):
        val = collatz_single_eval(10)
        self.assertEqual(val, 7)

    def test_single_eval_3(self):
        val = collatz_single_eval(837799)
        self.assertEqual(val, 525)

    # -----
    # print
    # -----

    def test_print(self):
        write_to = StringIO()
        collatz_print(write_to, 1, 10, 20)
        self.assertEqual(write_to.getvalue(), "1 10 20\n")

    def test_print_2(self):
        write_to = StringIO()
        collatz_print(write_to, 100, 200, 125)
        self.assertEqual(write_to.getvalue(), "100 200 125\n")

    def test_print_3(self):
        write_to = StringIO()
        collatz_print(write_to, 900, 1000, 174)
        self.assertEqual(write_to.getvalue(), "900 1000 174\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        read = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(
            write.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        read = StringIO("4331 4370\n8454 8517\n1275 1335\n868 893\n"
                        "5674 5732\n6157 6232\n6649 6694\n5837 5857\n"
                        "5646 5696\n12 26\n6072 6165\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(
            write.getvalue(), "4331 4370 184\n8454 8517 203\n1275 1335 177\n868 893 179\n"
                              "5674 5732 174\n6157 6232 262\n6649 6694 182\n5837 5857 218\n"
                              "5646 5696 205\n12 26 24\n6072 6165 187\n")

    def test_solve_3(self):
        read = StringIO("176 240\n459 519\n889 981\n642 668\n230 305\n\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(
            write.getvalue(), "176 240 128\n459 519 142\n889 981 174\n642 668 145\n230 305 128\n")

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
