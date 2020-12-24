import pyodbc
import MyClass.ClsDataOperation as opr
import MyClass.ProductModel as ModelProduct
import MyClass.InvoiceDetailsModel as ModelItem
import MyClass.InvoiceSalesModel as ModelMain

from enum import Enum, unique
import numpy as np
@unique
class Operation(Enum):
    GetAll = 1
    ById = 2
    ByName = 3
    Find = 4
    Update= 5
    Delete=6
class Color(Enum):
    white=1, 
    red =2,
    green =3,
    yellow =4,
    blue =5,
    black =6,
    brown =7,
    grey =8,
    silver =9,
    golden =10,
    orange =11,
    pink =12,
    Milky=13,

if __name__ == '__main__':
 model=ModelProduct

print("----------------- *************** -------------------------------------")
print(" WellCome to CSU  | Shop Student|    мивт 101 Student :Sallam Mohamed |")
print("----------------- *************** -------------------------------------")
try:
 while True:
    print("=================================================================================================================")
    print("Press>> 1 GetAll | 2 GetById | 3 GetByName | 4 Find | 5 AddNew | 6 Update | 7 Delete | 8 Sales |9 SalesReport 11 ")
    print("-----------------------------------------------------------------------------------------------------------------\n\n")
    line = input()
    if line=="1":
       print("Get All Product In DataBase\n")    
       opr.GetAllProduct()
    elif line=="2":
       print("Get Product By ProductId\n")
       id=input("Id:")
       opr.GetProduct(id)
    elif line=="3":
       print("Get Product By Name\n")
       Pname=input("Product Name:")
       opr.GetByName(Pname)
    elif line=="4":
       print("Find by Any Part Of Name Or Tradmark\n")
       ValueSearch=input("Insert Value ToSearch:")
       opr.Find(ValueSearch)
    elif line=="5" or line=="6":
        if line=="6":
          print("To UpdateProduct You Need To Insert Product Id First\n")
          model.Id= input("Id:")
        elif line=="5":
          print("To Add New You Product Insert that Data\n")       
        model.ProductName=input("Product_Name:")
        model.ProductType=input("ProductType 1 for TShirt 2 for Shoes:")
        model.TradeMark=input("TradeMark:")
        model.Price= input("Price:")
        model.size=input("Size:")
        model.Color=input("white=1 Red =2 green =3 Blue =5 Black =6 Brown =7 Grey =8 silver =9 golden =10 orange =11,pink =12,Milky=13,\n Insert Color:")
        if line=="5":
            opr.InsertProduct(model)
        elif line=="6":
            opr.UpdateProduct(model) 
        print('Save Succefully')
    elif line=="7":
       print("To DeletedProduct You Need To Insert Product Id First\n")
       id=input("Id:")
       opr.DeleteProduct(id)
    elif line=="8":
       print("You are now in POS Point Of Sales Program \n")  
       modelitm=ModelItem.InvoiceDetailsModel
       NewIdInvoice= opr.CreateNewInvoice()
       if(NewIdInvoice>0):
          while True: 
            print("Press a if you Need to AddNew Item \n")  
            Line2=input()
            if Line2=="A" or Line2=="a":                        
                 modelitm.Sales_Id=int(NewIdInvoice)
                 modelitm.Id_Product=int( input("Product_Id:"))
                 modelitm.Price=int(input("Price:"))
                 modelitm.Amount= int(input("Amount:"))
                 opr.AddProductInInvoice(modelitm)
            else:
                modelmaim=ModelMain.Invoice_Main
                modelmaim.PaymentWay=int(input("Payment Way 1 for Cash 2 For Cart 3 For Bounce:"))
                modelmaim.ClientName=input("Insert Client Name Or Card No:")
                modelmaim.Sales_Id=int(NewIdInvoice)
                modelmaim.TotalCost=opr.GetSumInvoice(modelmaim.Sales_Id)
                opr.UpdateMainDataInvoice(modelmaim)
                break   
    elif line=="9":
      opr.GetAllInvoicsSales()
    elif line=="11":         
         import os
         os.system('cls||clear')
    else:        
        print("\nGood Bay")
        break 
except pyodbc.Error as ex:
        sqlstate = ex.args[0]       
        print(sqlstate)
 
 
 

 
 
   


     
   
