#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1. Write a Python program to print the number 10.
a=10
a


# In[47]:


#Q2. Write a program to print the numbers 5, 10, and 15 in a single line separated by spaces.
a,b,c=5,10,15
print(a, b, c)


# In[45]:


#Q3. Store your name in a variable and print it.
name="venky"
print(name,type(name))


# In[2]:


#Q4. Store your first name and last name in two variables and print both.
first="Bommideni"
last="Venkateshwar"
complete=first+last
print(complete,type(complete))


# In[3]:


#Q5. Store your age in a variable and print: I am 25 years old.
age=21
print("i am ",age,"years old")


# In[20]:


#Q6. Store your name and city in variables and print the message: My name is Ravi and I live in Mumbai.
         #using the format() method.
name="venky"
city="hyd"
message="My name is{} and i live in {}".format(name,city)
print(message)


# In[5]:


#Q7. Print variables a = 10, b = 20, c = 30 separated by |.
a=10
b=20
c=30
print(a,b,c,sep='|')


# In[7]:


#Q8. Print Python and Rocks! on the same line without using two print() statements.
one='Python'
two='Rocks'
print(one," ",two)


# In[8]:


#Q9. Store two numbers 5 & 8 and print their sum using an f-string.
a=5
b=8
sum=a+b
print(f"sum of {a} and {b} is {sum}")


# In[10]:


#Q10. Ask the user to enter their name and print: Hello, SHNA(SRK
name=input("Enter your name")
print('hello',name)


# In[12]:


#Q11. Create a variable named city and assign your favourite city name to it. Print teh variable
fevcity='hyd'
print(fevcity)


# In[14]:


#Q12. Assign the value 10 to variable a and the value 20 to variable b. Swap the values of a and b and print them.
a=10
b=20
a,b=b,a
print(a,b)
print(b,a)


# In[15]:


#Q13. Create three variables in one line and assign them the values 5, 10, and "Python".
a,b,c=5,10,"Python"
print(a,b,c)


# In[17]:


#Q14. Assign the same value "Red" to three variables color1, color2, and color3.
color1=color2=color3="Red"
print(f"color1 :{color1}")
print(f"color2 :{color2}")
print(f"color3 :{color3}")


# In[19]:


#Q15. Check the type of variable num that has value 3.14 and print it.
num=3.14
print(num,type(num))


# In[21]:


#Q16. Create a variable name with your name, and another variable age with your age. Print a sentence like:"My name is John and I am 25 years old."
name='Venky'
age=22
sentence="My name is {} and i am {} years old".format(name,age)
print(sentence)


# In[22]:


#Q17. What will be the output of the following code?
       # a= "5"
       # b=3
        #print(a * b)
a= "5"
b=3
print(a * b)


# In[28]:


#Q18. Create a variable is_python_fun and assign it the boolean value True. Print it.
is_python_fun=True
print(is_python_fun)


# In[43]:


#Q19. What is the output of the x?
           #x = 10, x +=5
x=10
x+=5
print(x)


# In[42]:


#Q20. Can you assign the value 5 to three variables a, b, and c in one line? Then, modify only b to 10 withoutchanging a and c.
a=b=c=5
d=10
b=d
print(f"a:{a}")
print(f"b:{b}")
print(f"c:{c}")


# In[48]:


#Q21. Assign 0 to five variables in one line, then update the second.
a=b=c=d=e=0
g=2
b=g
print(a,b,c,d,e)


# In[57]:


#Q22. Delete the variable x. where x = 10.
x=10
print('Before deletion',x)
del x


# In[58]:


#Q23. Create two variables x = 5 and y = 7, and print their sum.
x=5
y=7
print('sum',x+y)


# In[65]:


#Q24. Swap the values of two variables.
x=5
y=7
x,y=y,x
print('Before swap x y===>',x,y)
print('After swap x y===>',y,x)


# In[66]:


#Q25. Create a variable greeting with value "Hello" and print it.
greeting="Hello"
greeting


# In[68]:


#Q26. Assign the result of 5 * 8 to a variable result and print it.
va=40
va


# In[69]:


#Q27. Assign two values to two variables in one line.
a,b=4,5
print(a,b)


# In[78]:


#Q28. Assign your first name and last name to two variables, then print them in one line.
first='Bommideni'
last='Venky'
print(first ,last)


# In[86]:


#Q29. Create a variable message and assign it "Good Morning". Now delete message. Try to print it after deletion.
message='Good morning'
print('Before deletion :',message)
del message
message


# In[88]:


#Q30. Assign a number to a variable num. Now, update num by adding 5 to it. Print the new value of num.
num=13
num+=5
print('After adding 5 :',num)


# In[ ]:





# In[ ]:




