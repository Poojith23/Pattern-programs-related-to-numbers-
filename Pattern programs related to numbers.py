#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Simple Number Triangle Pattern

rows = 6
#rows=int(input("Enter the number of rows:"))
for num in range(rows):
    for i in range(num):
        print(num, end=" ") # print number
    # line after each row to display pattern correctly

    print(" ")


# In[5]:


#Inverted Pyramid of Numbers

rows = 5
#rows=int(input("Enter the number of rows:"))
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')


# In[6]:


#Half Pyramid Pattern of Numbers

rows=5
#rows=int(input("Enter the number of rows:"))
for row in range(1, rows+1):
    for column in range(1, row + 1):
        print(column, end=' ')
    print(" ")


# In[9]:


# Inverted Pyramid of Descending Numbers

rows = 5
#rows=int(input("Enter the number of rows:"))
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")


# In[ ]:




