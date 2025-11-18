#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1. Qno 1: Creating and Accessing Dictionaries

#Create a dictionary with the first 10 positive integers as keys and their squares as values. Print the dictionary.
d1={x:x**2 for x in range(1,11)}
d1


# In[6]:


#Qno 2: Accessing Dictionary Elements

#Print the value of the key 5 and the keys of the dictionary created in Assignment 1
d1={x:x**2 for x in range(1,11)}
print(d1)
 #value of key 5
print('Keys :',d1.keys())
print('value of 5:',d1[5])
   


# In[7]:


#Qno 3: Dictionary Methods

#Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 and then remove the key-value pair with key 1. Print the modified dictionary.
d1={x:x**2 for x in range(1,11)}
print('Before any changes :',d1)
#adding new key value pair
d1.update({11:121})
print('After update :',d1)
#removing key value pair with key 1
d1.pop(1)
print('After popping :',d1)


# In[8]:


#Qno 4: Iterating Over Dictionaries

#Iterate over the dictionary created in Assignment 1 and print each key-value pair.
d1={x:x**2 for x in range(1,11)}
for k,v in d1.items():
    print(k,'==>',v)


# In[10]:


#Qno 5: Dictionary Comprehensions

#Create a new dictionary containing the cubes of the first 10 positive integers using a dictionary comprehension. Print the new dictionary.
d1={x:x**3 for x in range(1,11)}
print(d1)


# In[8]:


#Qno 6: Merging Dictionaries

#Create two dictionaries: one with keys as the first 5 positive integers and values as their squares, and another with keys as the next 5 positive integers and values as their squares. Merge these dictionaries into a single dictionary and print it.
d1={1:1,2:4,3:9,4:16,5:25}
d2={6:36,7:49,8:64,9:81,10:100}
print('Before merging: d1==>',d1)
print('Before merging: d2==>',d2)
d1.update(d2)
print('After merging d1 & d2 ==>',d1)


# In[14]:


#Qno 7: Nested Dictionaries

#Create a nested dictionary representing a student with keys 'name', 'age', 'grades', where 'grades' is another dictionary with keys 'math', 'science', and 'english'. Print the nested dictionary.
student={'name':'venky','age':13,"grade":{'math':'A','science':'B','english':'C'}}
for k,v in student["grade"].items():
    print(k,v)


# In[26]:


#Qno 8: Dictionary of Lists

#Create a dictionary where the keys are the first 5 positive integers and the values are lists containing the first 5 multiples of the key. Print the dictionary.
d1={x:[x*i for i in range(1,6)] for x in range(1,6)}
print(d1)


# In[24]:


#Qno 9: Dictionary of Tuples

#Create a dictionary where the keys are the first 5 positive integers and the values are tuples containing the key and its square. Print the dictionary.
d={x:(x,x**2) for x in range(1,6)}
print(d)


# In[37]:


#Qno 10: Dictionary and List Conversion

#Create a dictionary with the first 5 positive integers as keys and their squares as values. Convert the dictionary to a list of tuples and print it.
d={x:x**2 for x in range(1,6)}
print(d)
result=list(d.items())
result


# In[43]:


#Qno 11: Dictionary Filtering

#Create a dictionary with the first 10 positive integers as keys and their squares as values. Create a new dictionary containing only the key-value pairs where the key is even. Print the new dictionary.
d={x:x**2 for x in range(1,11) if x%2==0}
print(d)


# In[47]:


#Qno 12: Dictionary Key and Value Transformation

#Create a dictionary with the first 5 positive integers as keys and their squares as values. Create a new dictionary with keys and values swapped. Print the new dictionary.
d={x:x**2 for x in range(1,6)}
swapping=dict(zip(d.values(),d.keys()))
print('Befoe swapping :',d)
print('After swapping :',swapping)


# In[ ]:


#Qno 13: Default Dictionary

#Create a default dictionary where each key has a default value of an empty list. Add some elements to the lists and print the dictionary.


# In[50]:


#Qno 14: Counting with Dictionaries

#Write a function that takes a string and returns a dictionary with the count of each character in the string. Print the dictionary.
s=input("enter string :")
def deffun(s):
    d=dict()
    for i in s:
        d.update({i:s.count(i)})
    return d
print(deffun(s))        


# In[ ]:


#Qno 15: Dictionary and JSON

#Create a dictionary representing a book with keys 'title', 'author', 'year', and 'genre'. Convert the dictionary to a JSON string and print it.


