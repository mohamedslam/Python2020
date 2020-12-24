import pyodbc
import pandas as pd
import numpy as np
import numpy
from datetime import datetime, timedelta

import MyClass.ProductModel as ModelProduct
import MyClass.InvoiceDetailsModel as ModelInvoiceItem
class ClsDataOperation(object):
    """description of class"""
   ##############|MSSql Server 2019 Connection Data |####################.
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

##############| Product Methods |####################.
def GetAllProduct():     
  rst=print(GetData("Select * from Products"))
  return rst
def GetProduct(Id):
   rst= print(GetData("Select * from Products where Id="+Id))
   return rst
def GetByName(Value):
   rst= print(GetData("Select * from Products where ProductName='"+Value+"'"))
   return rst
def Find(StrValue):
   rst= print(GetData("Select * from Products where ProductName like N'%"+StrValue+"%' or TradeMark like '%"+StrValue+"%'"))
   return rst
def DeleteProduct(Id):
   rst= ExecuteData("Delete from Products where Id="+Id) 
   return rst
def InsertProduct(model):
  model=ModelProduct
  Sql="Insert into Products (ProductName, ProductType, Price, Color, size, TradeMark) Values('"+model.ProductName    +"', '"+model.ProductType     +"', '"+model.Price    +"', '"+model.Color   +"', '"+ model.size     +"', '"+model.TradeMark+"')"  
  ExecuteData(Sql)

def UpdateProduct(model):
  model=ModelProduct
  Sql="Update Products Set " +"ProductName='"+model.ProductName +"', ProductType='"+model.ProductType +"', Price='"+model.Price +"', Color='"+model.Color +"', size='"+model.size +"', TradeMark='"+model.TradeMark +"'  where Id="+model.Id
  ExecuteData(Sql)

  ##############| SallesMethods |####################.
def CreateNewInvoice():
   NewInvoice_Id=0
   model=ModelProduct
   ExecuteData("Insert into Invoice_Main (InDate) Values(Getdate())")  
   NewInvoice_Id  = GetData("Select Max(Sales_Id) Id from Invoice_Main").astype(int)  
   val= NewInvoice_Id["Id"][0]
   return val


def AddProductInInvoice(model):       
       Total=model.Amount*model.Price
       Sql="Insert into Invoice_Details(Sales_Id, Id_Product, Price, Amount, Total) Values("+ str( model.Sales_Id) +","+str(model.Id_Product)+","+str(model.Price )+", "+str(model.Amount)   +", "+str(Total) +")"
       ExecuteData(Sql)
def UpdateMainDataInvoice(model):     
       Sql="Update Invoice_Main Set  PaymentWay="+str(model.PaymentWay)+", ClientName='"+str(model.ClientName)+"', TotalCost="+str(model.TotalCost)+"  where Sales_Id="+str(model.Sales_Id)
       ExecuteData(Sql)
def GetSumInvoice(Sales_Id):
    Sum_Invoice=0
    Sum_Invoice  = GetData("Select Sum(Total) Sum from Invoice_Details where Sales_Id="+str(Sales_Id))  
    val= Sum_Invoice["Sum"][0]
    return val
def GetAllInvoicsSales():
  rst=print(GetData("select [Sales_Id] InoviceNum,case when PaymentWay=1 then 'Cash' when PaymentWay=2 then 'CardBank' when PaymentWay=3 then 'Bounce' end PaymentWay, [ClientName], [TotalCost], [InDate]  from [dbo].[Invoice_Main] "))
  return rst


  


