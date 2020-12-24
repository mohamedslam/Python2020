 
import pytest
import requests

from unittest import TestCase

import MyClass.ClsDataOperation as opr
import MyClass.ProductModel as ModelProduct

  
class Test_MyUnitest_1(unittest.TestCase):
      
    def test_InsertProduct():
      assert opr.InsertProduct(ProductName="tchirt",ProductType="1",Price="20",Color=1,size=40,tradeMark="Nike")
    
    def test_UpdateProduct():
      assert opr.UpdateProduct(ProductName="tchirt",ProductType="1",Price="20",Color=1,size=40,tradeMark="Nike")

    def test_DeleteProduct():
      assert opr.DeleteProduct(Id=3)    
    
    def test_GetAllProduct():
      assert opr.GetAllProduct()  

    def test_GetProduct():
      assert opr.GetProduct(Id=3)

    def test_GetByName():
      assert opr.GetByName("m")

    def test_Find():
      assert opr.Find("m")


     
 
