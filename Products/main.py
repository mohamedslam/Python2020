
import MyClass.ClsDataOperation as opr
import MyClass.ClsProductModel as ModelProduct

from enum import Enum, unique
 
@unique
class Operation(Enum):
    GetAll = 1
    ById = 2
    ByName = 3
    Find = 4
    Update= 5
    Delete=6
 
 
if __name__ == '__main__':
 model=ModelProduct

print("WellCome to CSU Shop")
print("<<1 GetAll>> <<2 GetById>> <<3 GetByName>> <<4 Find>> <<5 AddNew>> <<6 Update>> <<7 Delete>> EmptyLine To Close")

while True:
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
        model.Color=input("Color:")
        if line=="5":
            opr.InsertProduct(model)
        elif line=="6":
            opr.UpdateProduct(model) 
    elif line=="7":
       print("To DeletedProduct You Need To Insert Product Id First\n")
       id=input("Id:")
       opr.DeleteProduct(id)
    else:
        print("\n")
        print("Good Bay")
        break
 

 

 
 
 

 
 
   


     
   
