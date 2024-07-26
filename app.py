# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 21:10:07 2024

@author: Aditya
"""
import pandas as pd
import os
path = os.path.dirname(os.path.abspath(__file__))
path = path.replace("\\","/")
# print(path)
vegmealdf = pd.read_csv(f"{path}/vegmeal.csv")
nonvegmealdf = pd.read_csv(f"{path}/nonvegmeal.csv")
beveragesdf = pd.read_csv(f"{path}/beverages.csv")


print("**Restuarant Billing system**")
print("[1] Login")
login = ""
oid = 100
itemlst = []
pricelst = []
qtylst = []
# orderlist = {}
def neworder(same=0):
    global oid
    if same == 1:
        pass
    else:    
        oid += 1
    print(f"""
          --Select a option--
          
          [1] meals
          [2] beverages
          [3] view cart
          [0] Cancel this order
          
          orderid : {oid}
          """)
    norder = int(input("Select: "))
    if norder == 0:
        print("""
              
              Are You sure to cancel this order ?
              [0] YES
              [1] NO
              
              """)
        confirm = int(input("Select: "))
        if confirm == 0:
            main()
        else:    
            neworder(1)
    elif norder == 1:
        meals()
    elif norder == 2:
        beverages()
    else :
        viewcart()
    # orderlist[f"oid_{oid}"]={"items":("roti","rice","soda")}
    # print(orderlist)
    
def viewcart():
    # print(pd.DataFrame(orderlist))
    # print(itemlst)
    # print(pricelst)
    # print(qtylst)
    odrlst = {"item":itemlst,"price":pricelst,"qty":qtylst,"total":[qtylst[x]*pricelst[x] for x in range(len(qtylst))]}
    odrlstdf = pd.DataFrame(odrlst) 
    print(odrlstdf)
    # print(orderlst)
    total = sum(odrlst['total'])
    print(f"""
          your total billing amount is : $ {total}
          --Select a option--
          
          [1] Proceed to pay
          [0] back
          
          orderid : {oid}
          """)
    pay = int(input("Select: "))
    if pay==1:
        mop(oid,total,odrlstdf)
    else:
        neworder(1)

def mop(oid,total,odrlstdf):
    print("""
      ---payment made---- 
      
      generating bill...
      
      """)
    print(oid)
    print(total)
    file = open(f'{path}/order_{oid}.txt',"wt")

    file.writelines(f" Code Restaurant \n Welcome\n\n Order no: {oid} \n\n {odrlstdf}\n\n Your total billing amount is Rs. {total} \n\n Thank you happy eating, Visit again :) ")
    # print(file.read())  
    file.close()

    os.startfile(f"{path}/order_{oid}.txt")
    
def meals():
    print("""
      *Have a meal*
      
      [1] veg
      [2] non-veg
      [0] back
      
      """)
    cat = int(input("Select: "))
    if cat == 0:
        neworder(1)
    elif cat == 1:
        items.vegmeals()
    else:
        items.nvegmeals()

def beverages():
    print("""
      *Have a Drink*
      
      """)
    print(beveragesdf)
    print("[9] Back")
    no= int(input("Select item number: "))
    if no==9:
        neworder(1)
    else:
        item = beveragesdf.iloc[[no]]
        additem(item,"vegmeals")

class items: 
    def vegmeals():
        print("""
          *Veg meal menu*  
          """)
        print(vegmealdf)
        print("[9] Back")
        no= int(input("Select item number: "))
        if no==9:
            meals()
        else:
            item = vegmealdf.iloc[[no]]
            additem(item,"vegmeals")
    
    def nvegmeals():
        print("""
          *Non-Veg meal menu*  
          """)
        print(nonvegmealdf)
        print("[9] Back")
        no= int(input("Select item number: "))
        if no==9:
            meals()
        else:
            item = nonvegmealdf.iloc[[no]]
            additem(item,"nvegmeals")
            
def additem(item,fun):
    print(item)
    qty=1
    qty = input("Select Quantity (default 1):")
    if qty == "":
        qty = 1
    # update - add a input type check for interger if not empty
    print(item,f" x {qty} Qty")
    confirmitem = int(input("Add this item [yes= 1 | no = 0]: "))
    if confirmitem == 1:
        # orderlist[f"oid_{oid}"]={"items":item.iloc[0,0],"price":item.iloc[0,1],"qty":qty}
        itemlst.append(item.iloc[0,0])
        pricelst.append(item.iloc[0,1])
        # update checked
        qtylst.append(int(qty))
        # print(orderlist)
        print()
        print("item added successfully...")
        getattr(items,fun)()
    else:
        # print(fun)
        getattr(items,fun)()
          
def main():
    print("""
          --Select a option--
          
          [1] New order
          [2] view past order
          [0] logout
          
          """)
    command = int(input("Select: "))
    if command == 1:
        neworder()
        
    elif command == 2:
        print('past')
        main()
    else:
        print('logging out')
        print('--Have a nice day--  :)')
    
def log():
    login = int(input("select: "))
    if login == 1:
        print('user is logged in')
        print()
        main()
    else:
        print("login First...")
        log()
log()