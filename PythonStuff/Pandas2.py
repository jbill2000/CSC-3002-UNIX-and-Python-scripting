#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 10:02:55 2021

@author: jeremybill
"""

import pandas as pd

data = {'Name':["Jones","Garcia","Chen","Smith","Solo","Adams","Dreydel"],'Year':[1,1,1,2,3,4,3],'Gpa':[2.40,3.50,4.00,2.75,3.70,2.60,3.90]}

studentData= pd.DataFrame(data)

print (studentData.head(7))
print ("The mean of the gpas is ", studentData['Gpa'].mean())

studentData.plot(kind='bar',x='Name',y='Gpa')
studentData.plot(kind='scatter',x='Year',y='Gpa')