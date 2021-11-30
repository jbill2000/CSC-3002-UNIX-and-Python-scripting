#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 08:25:21 2021

@author: jeremybill
"""
import pandas as pd
import random

def monthlyBonus(mon):
    if mon=='Nov' or mon=='Dec':
        choiceList=[100,100,100,100,200,200,200,200,100,50]
    elif mon=='Jan' or mon=='Feb':
        choiceList=[0,0,0,0,0,0,50,50,100,100]
    else:
        choiceList=[0,0,0,50,50,100,100,100,200,200]
    monthlist=[]
    #get data for each of 8 employees
    for i in range(8):
        monthlist.append(random.choice(choiceList))
    return monthlist

#build a dictionary containing 10 weeks of commission data
bonusDict={}
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for month in months:
    bonusDict[month]=monthlyBonus(month)

#create the DataFrame of data
SalesPeople = ['Jose','Yi','Jon','Oscar','Amanda','Bill','Alexa','Kim']
bonusData=pd.DataFrame(bonusDict,index=SalesPeople)

#add the calculated columns
bonusData['Total Bonus']=bonusData.sum(axis=1)
bonusData['Ave per Week']=bonusData['Total Bonus']/10.0

pd.set_option('display.max_columns', None)#this just forces all columns to print
print (bonusData)
#prints the values
print("For 12 months of bonuses next year you would need to budget ",bonusData['Total Bonus'].sum())
print("In April the minimum and maximum bonuses are projected to be:",bonusData['Apr'].min(), "and" ,bonusData['Apr'].max())
print("In April total bonuses should be ",bonusData['Apr'].sum(),"and in December they should be",bonusData['Dec'].sum())
#plots a bar and line graph
bonusData.plot(kind="line",y=['Dec','Jan'],color=['red','blue'],figsize=(10,10))
bonusData.plot(kind='bar',y=['Jan','Apr','Dec'],color=['red','blue','green'],title="Projected Bonuses for the months of Jan, Apr and Dec")

