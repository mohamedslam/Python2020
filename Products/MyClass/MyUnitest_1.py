import unittest
import pytest
import requests

from unittest import TestCase

import MyClass.ClsDataOperation as opr
import MyClass.ClsProductModel as ModelProduct

class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)


class Test_MyUnitest_1(unittest.TestCase):
    def test_A(self):
        self.fail("Not implemented")

    def Add_Test():
        print("InsertProduct_Test")
        product=opr.InsertProduct(ProductName="tchirt",ProductType="1",Price="20",Color=1,size=40,tradeMark="Nike")
        p_type=product.gettype()
        #assert p_type==opr.
    


if __name__ == '__main__':
    unittest.main()
