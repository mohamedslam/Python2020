import pyodbc
import pandas as pd
from datetime import datetime, timedelta
from MyClass.ClsProductModel import ClsProductModel
import MyClass.ClsProductModel as ModelProduct

class ClsDataOperation(object):
    """description of class"""
 
server = 'CHL-WST1160' 
database = 'CSUTest' 
username = 'sa' 
password = 'Slam221980' 

 
def Condb(): 
 con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password) 
 return con
def GetData(sql):
  con=Condb()
  data = pd.read_sql(sql,con)
  del con 
  return data
def ExecuteData(sql):    
   con= Condb()
   cursor = con.cursor()
   cursor.execute(sql)
   con.commit()
   del con 
    
def GetAllProduct():     
  rst=print(GetData("Select * from Products"))
  return rst;
def GetProduct(Id):
   rst= print(GetData("Select * from Products where Id="+Id))
   return rst;
def GetByName(Value):
   rst= print(GetData("Select * from Products where ProductName='"+Value+"'"))
   return rst;
def Find(StrValue):
   rst= print(GetData("Select * from Products where ProductName like N'%"+StrValue+"%' or TradeMark like '%"+StrValue+"%'"))
   return rst;
def DeleteProduct(Id):
   rst= ExecuteData("Delete from Products where Id="+Id) 
   return rst;

def InsertProduct(model):
  model=ModelProduct
  Sql="Insert into Products (ProductName, ProductType, Price, Color, size, TradeMark) Values('"+model.ProductName    +"', '"+model.ProductType     +"', '"+model.Price    +"', '"+model.Color   +"', '"+ model.size     +"', '"+model.TradeMark+"')"  
  ExecuteData(Sql)

def UpdateProduct(model):
  model=ModelProduct
  Sql="Update Products Set " +"ProductName='"+model.ProductName +"', ProductType='"+model.ProductType +"', Price='"+model.Price +"', Color='"+model.Color +"', size='"+model.size +"', TradeMark='"+model.TradeMark +"'  where Id="+model.Id
  ExecuteData(Sql)


