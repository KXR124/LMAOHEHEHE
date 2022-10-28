import mysql.connector
from tabulate import tabulate
import time
from mysql.connector import Error
import datetime
db=mysql.connector.connect(host="localhost",user="Kirthi",password="Chimkin#12",database="sneakeroo")
print("\t\t\tConnected to the server!")
print("\n\t\t\tLoading... :)")
time.sleep(3)
mycur=db.cursor()

def Addproduct():
    p=input("Enter the product ID: ")
    Pname=input("Enter the Product Name: ")
    bnd=input("Enter the Brand: ")
    sex=input("Enter the Gender (Male/female): ")
    rate=int(input("Enter the price: "))
    
    data=(p,Pname,bnd,sex,rate)
    
    sql="""Insert into product(product_id,Pname,bnd,sex,rate)values(%s,%s,%s,%s,%s)"""
    mycur.execute(sql,data)
    db.commit()
    s=(p,0,"No")
    sql="""Insert into stock(item_id,Instock,status)values(%s,%s,%s)"""
    mycur.execute(sql,s)
    db.commit()
    print("One Product Successfully Inserted :D")
    return

def EditProduct():
    p_id=input("Enter the Product ID to be edited: ")
    sql="select * from product where product_id=%s"
    e=(p_id,)
    mycur.execute(sql,e)
    re=mycur.fetchall()
    print(tabulate(re,tablefmt='grid'))

    print()
    f=input("Enter the field which you want to edit: ")
    val=input("Enter the value which you want to set: ")
    sql="Update product set " + f +"='" + val + "' where product_id='" + p_id + "'"
    sq=sql
    mycur.execute(sql)
    print("Edit is complete")
    print("After correction the record is: ")
    sql="select * from product where product_id=%s"
    e=(p_id,)
    mycur.execute(sql,e)
    re=mycur.fetchall()
    print(tabulate(re,tablefmt='grid'))

    db.commit()

def EditStock():
    item=input("Enter Product Name : ")
    e=int(input("Enter the amount of stock: "))
    sql="select product.product_id,product.PName,stock.Instock,\
    stock.status from stock, product where \
    product.product_id=stock.item_id and product.PName=%s"
    itm=(item,)
    er=(e,)
    sql_1= "Update stock set Instock=Instock +(Instock +%s)"
    mycur.execute(sql_1,er)
    print("The Stock is updated")
    res=mycur.fetchall()
    print(tabulate(res,tablefmt='grid'))



def DelProduct():
    p_id=input("Enter the Product)id to be deleted : ")
    sql="delete from sales where item_id=%s"
    id=(p_id,)
    mycur.execute(sql,id)
    db.commit()
    sql="delete from purchase where item_id=%s"
    mycur.execute(sql,id)
    db.commit()
    sql="delete from stock where item_id=%s"
    mycur.execute(sql,id)
    db.commit()
    sql="delete from product where product_id=%s"
    mycur.execute(sql,id)
    db.commit()
    print("\t\t\nOne Item Deleted")

def ViewStock():
    item=input("Enter Product Name : ")
    sql="select product.product_id,product.PName,stock.Instock,\
    stock.status from stock, product where \
    product.product_id=stock.item_id and product.PName=%s"
    itm=(item,)
    mycur.execute(sql,itm)
    res=mycur.fetchall()
    print(tabulate(res,tablefmt='grid'))


def ViewProduct():
    sql="select * from product"
    mycur.execute(sql)
    res=mycur.fetchall()
    print(tabulate(res,tablefmt='grid'))

def PurchaseProduct():
    mn=""
    dy=""
    now=datetime.datetime.now()
    purchaseID="P"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)
    L=[]
    Lst=[]
    L.append(purchaseID)
    itemId=input("Enter Product ID : ")
    L.append(itemId)
    itemNo=int(input("Enter the number of Items : "))
    L.append(itemNo)
    sql="select rate from product where product_id=%s"
    pid=(itemId,)
    mycur.execute(sql,pid)
    res=mycur.fetchone()
    for x in res:
        print("rate is : ", x)
    amount=res[0]*itemNo
    print("Amount is :", amount)
    L.append(amount)
    mnth=now.month
    if mnth<=9:
        mn="0"+str(mnth)
    else:
        mn=str(mnth)
    day=now.day
    if day<=9:
        dy="0"+str(day)
    else:
        dy=str(day)
    dt=str(now.year)+"-"+mn+"-"+dy
    L.append(dt)
    tp=(L)
    sql="insert into purchase(purchase_id,item_id,no_of_items,amount,Purchase_date)values(%s,%s,%s,%s,%s)"
    mycur.execute(sql,tp)
    db.commit()
    sql="Select Instock from stock where item_id=%s"
    mycur.execute(sql,pid)
    res=mycur.fetchone()
    status="No"
    instock=res[0]-itemNo
    if instock>0:
        status="Yes"
    Lst.append(instock)
    Lst.append(status)
    Lst.append(itemId)
    tp=(Lst)
    sql="update stock set instock=%s,status=%s where item_id=%s"
    mycur.execute(sql,tp)
    db.commit()
    print("THANK YOU FOR YOUR PURCHASE X), ITEMS WILL BE DELIEVERD TO YOUR DOORSTEP WITHING 4 BUSINESS DAYS.\nDo shop with us again :D")
    print("\n\t\t\t")
    print("""$$$$$$$$\ $$\                           $$\                                                 
            \__$$  __|$$ |                          $$ |                                                
             $$ |   $$$$$$$\   $$$$$$\  $$$$$$$\  $$ |  $$\       $$\   $$\  $$$$$$\  $$\   $$\       
             $$ |   $$  __$$\  \____$$\ $$  __$$\ $$ | $$  |      $$ |  $$ |$$  __$$\ $$ |  $$ |      
            $$ |   $$ |  $$ | $$$$$$$ |$$ |  $$ |$$$$$$  /       $$ |  $$ |$$ /  $$ |$$ |  $$ |      
            $$ |   $$ |  $$ |$$  __$$ |$$ |  $$ |$$  _$$<        $$ |  $$ |$$ |  $$ |$$ |  $$ |      
            $$ |   $$ |  $$ |\$$$$$$$ |$$ |  $$ |$$ | \$$\       \$$$$$$$ |\$$$$$$  |\$$$$$$  |      
            \__|   \__|  \__| \_______|\__|  \__|\__|  \__|       \____$$ | \______/  \______/       
                                                                 $$\   $$ |                          
                                                                 \$$$$$$  |                          
                                                                 \______/                          """)



def Customer():
    print("""
     _______..__   __.  _______     ___       __  ___  _______ .______        ______     ______   
    /       ||  \ |  | |   ____|   /   \     |  |/  / |   ____||   _  \      /  __  \   /  __  \  
   |   (----`|   \|  | |  |__     /  ^  \    |  '  /  |  |__   |  |_)  |    |  |  |  | |  |  |  | 
    \   \    |  . `  | |   __|   /  /_\  \   |    <   |   __|  |      /     |  |  |  | |  |  |  | 
.----)   |   |  |\   | |  |____ /  _____  \  |  .  \  |  |____ |  |\  \----.|  `--'  | |  `--'  | 
|_______/    |__| \__| |_______/__/     \__\ |__|\__\ |_______|| _| `._____| \______/   \______/
""")
    name=input("Please input your name: ")
    print("Welcome!",name)
    while True:
        ask=input("What would you like to do?\n1.All Items\n2.Search by name\n3.Search by Brand\n4.Search by Gender\n5.Purchase a Product\n6.Exit store\nChoose your option: ")
        if ask == "1":
            ViewProduct()
        elif ask == "2":
            var='PName'
            val=input("Enter the name of Product : ")
            sql="select * from product where " + var + " = %s"
            sq=sql
            tp=(val,)
            mycur.execute(sq,tp)
            res=mycur.fetchall()
            print(tabulate(res,tablefmt='grid'))

        elif ask == "3":
            var='bnd'
            val=input("Enter the name of Brand : ")
            sql="select * from product where " + var + " = %s"
            sq=sql
            tp=(val,)
            mycur.execute(sq,tp)
            res=mycur.fetchall()
            print(tabulate(res,tablefmt='grid'))

        elif ask == "4":
            var='sex'
            val=input("Enter the Gender: ")
            sql="select * from product where " + var + " = %s"
            sq=sql
            tp=(val,)
            mycur.execute(sq,tp)
            res=mycur.fetchall()
            print(tabulate(res,tablefmt='grid'))

        elif ask == "5":
            PurchaseProduct()
        elif ask == "6":
            print("We Hope to see you again :)")
            x=input("Would you like to re-visit the store? (Just in case you misclicked to exit) (y/n): ")
            if x=="y":
                continue
            else:
                exit()



def Admin():
    datab={"Kirthi":"1234"}
    time.sleep(3)
    ask=input("\t\t\t     *****||Welcome!||*****\n\t\t\t\t1.Admin\n\t\t\t\t2.Customer\n\t\t\t\tChoose an option: ")
    if ask=="1":
        user=input("\nEnter the Username: ")
        password=input("\nEnter the Password: ")
        try:
            if password in datab[user]:
                print("\n\t\t\t\tLoading...")
                time.sleep(3)
                print("\nWelcome,",user)
                while True:
                    a=input("What would you like to do?:\n1.Add Product\n2.Edit Product\n3.Delete a Product\n4.View Stock\n5.Move to Customer Page\n6.Edit Stock\n7.View All Products\n8.Exit out of Program\nChoose your option: ")
                    if a=="1":
                        Addproduct()
                    elif a=="2":
                        EditProduct()
                    elif a=="3":
                        DelProduct()
                    elif a=="4":
                        ViewStock()
                    elif a=="5":
                        Customer()
                    elif a=="6":
                        EditStock()
                    elif a=="7":
                        ViewProduct()
                    elif a=="8":
                        exit()
                        

            else:
                print("\nInvalid Code")
        except KeyError:
            print("\nInvalid Username")
    else:
        Customer()
Admin()
    