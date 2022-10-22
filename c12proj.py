import os
import mysql.connector
import datetime
import pandas as pd
import platform
from mysql.connector import Error
try:
    db=mysql.connector.connect(host="localhost",user="yourusername",password="yourpassword",database="sneakeroo")

    if db.is_connected():
        print("Connected to the server!")
        mycur=db.cursor()
except Error as e:
    print("Error while connecting to the MySQL Server, The Error occured is = ",e)

def Admin():
    datab={"Kirthi":"1234","Jaik":"2345","Abu":"3456"}
    ask=input("\t\t\t     *****Welcome!*****\n\t\t\t\t1.Admin\n\t\t\t\t2.Customer\n\t\t\t\tChoose an option: ")
    if ask=="1":
        user=input("Enter the Username: ")
        password=input("Enter the Password: ")
        try:
            if password in datab[user]:
                print("Welcome,",user)
            else:
                print("Invalid Code")
        except KeyError:
            print("Invalid Username")
    else:
        exit()
Admin()
        
'''

    def Addproduct():
    def EditProduct():
    def DelProduct():
    def ViewStock():
    

def ViewProduct():

def PurchaseProduct():

def ViewPurchases():

def Saleproduct():

def Menu():

print("""
     _______..__   __.  _______     ___       __  ___  _______ .______        ______     ______   
    /       ||  \ |  | |   ____|   /   \     |  |/  / |   ____||   _  \      /  __  \   /  __  \  
   |   (----`|   \|  | |  |__     /  ^  \    |  '  /  |  |__   |  |_)  |    |  |  |  | |  |  |  | 
    \   \    |  . `  | |   __|   /  /_\  \   |    <   |   __|  |      /     |  |  |  | |  |  |  | 
.----)   |   |  |\   | |  |____ /  _____  \  |  .  \  |  |____ |  |\  \----.|  `--'  | |  `--'  | 
|_______/    |__| \__| |_______/__/     \__\ |__|\__\ |_______|| _| `._____| \______/   \______/
""")
'''





