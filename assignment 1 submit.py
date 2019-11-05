#!/usr/bin/env python
# coding: utf-8

# In[1]:


L1 = "Twinkle, twinkle, little star, "
L2 = "How I wonder what you are"
L3 = "Up above the world so high, "
L4 = "Like a diamond in the sky. "
print(L1 + "\n\t" + L2 + "! \n\t\t" + L3 + "\n\t\t" + L4 + "\n" + L1 + "\n\t" + L2)


# In[2]:


import sys
print("Python version which i am using is: ")
print(sys.version_info)


# In[3]:


from datetime import datetime
date_time = datetime.now()
var = date_time.strftime("%d/%m/%Y  %H:%M:%S")
print("Current date and time: " + var)


# In[4]:


radius = float(input("Enter radius: \n"))
area = 3.14159 * radius
print("Area of circle:")
print(area)


# In[5]:


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


# In[7]:


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2 
print(sum)

