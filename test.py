# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 16:19:12 2024

@author: Aditya
"""
import pandas as pd

itemlst = ["1","e","ww"]
pricelst = [200,300,200]
qtylst = [1,4,2]

odrlst = {"item":itemlst,"price":pricelst,"qty":qtylst,"total":[qtylst[x]*pricelst[x] for x in range(len(qtylst))]}
orderrecipt = pd.DataFrame(odrlst)
print(orderrecipt)
total = sum(odrlst['total'])
print(total)
# total = []
# for x in range(len(qtylst)):
#     t = qtylst[x]*pricelst[x]
#     total.append(t)

# print(total)

# tprice = [qtylst[x]*pricelst[x] for x in range(len(qtylst))]

import os
oid = 101
path = os.path.dirname(os.path.abspath(__file__))
path = path.replace("\\","/")
nonvegmealdf = pd.read_csv(f"{path}/nonvegmeal.csv")
print(nonvegmealdf)

# orderrecipt.to_csv(f"{path}/{oid}.csv")
file = open(f'{path}/order_{oid}.txt',"wt")

file.writelines(f" Code Restaurant \n Welcome\n\n Order no: {oid} \n\n {orderrecipt}\n\n Your total billing amount is Rs. {total} \n\n Thank you happy eating, Visit again :) ")
# print(file.read())  
file.close()

os.startfile(f"{path}/order_{oid}.txt")
# os.startfile(f"{path}/order_{oid}.txt","print")

