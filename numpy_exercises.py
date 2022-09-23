#!/usr/bin/env python
# coding: utf-8




#a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])*/

#1 How many negative numbers are there?

#2 How many positive numbers are there?

#3 How many even positive numbers are there?

#4 If you were to add 3 to each data point, how many positive numbers would there be?

#5 If you squared each number, what would the new mean and standard deviation be?

#6 A common statistical operation on a dataset is centering. This means to adjust the data such that 
# the mean of the data is 0. This is done by subtracting the mean from each data point. 
# Center the data set. See this link for more on centering.

#7 Calculate the z-score for each data point. Recall that the z-score is given by:

# Z =x−μ/σ

#8 Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add 
# your solutions.

#Awesome Bonus For much more practice with numpy, Go to https://github.com/rougier/numpy-100 and clone 
# the repo down to your laptop. To clone a repository: - Copy the SSH address of the repository - 
# cd ~/codeup-data-science - Then type git clone git@github.com:rougier/numpy-100.git - 
# Now do cd numpy-100 on your terminal. - Type git remote remove origin, so you won't accidentally try to 
# push your work to Rougier's repo.

#Congratulations! You have cloned Rougier's 100 numpy exercises to your computer. Now you need to make a new, 
#blank, repository on GitHub.

#Go to https://github.com/new to make a new repo. Name it numpy-100.
#DO NOT check any check boxes. We need a blank, empty repo.
#Finally, follow the directions to "push an existing repository from the command line" so that you can push up your changes to your own account.
#Now do work, add it, commit it, and push it!


# In[1]:


import numpy as np


# In[2]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[3]:


#1 How many negative numbers are there?
np.sum(np.array(a) < 0, axis=0)


# In[4]:


a < 0


# In[5]:


#andrews example
a<0
a


# In[6]:


a[a<0]


# In[7]:


len(a[a<0])


# In[8]:


#2 How many positive numbers are there?

import numpy as np

np.sum(np.array(a) > 0, axis=0)


# In[9]:


#andrews ex
pos_num = a[a>0]
pos_num = [pos_num %2. ==  0]
len(a[a>0])


# In[10]:


#3 How many even positive numbers are there?
#np.count_nonzero(a % 2 == 0) 
pos_a = a[a > 0]
pos_a[pos_a % 2 == 0]
len(pos_a[pos_a % 2 == 0])


# In[11]:


#4 If you were to add 3 to each data point, how many positive numbers would there be?
add_3 = a + 3
add_3[add_3 > 0].size


# In[12]:


len(a[(a+3)>0])


# In[13]:


#5 If you squared each number, what would the new mean and standard deviation be?
a_square = a**2
a_square.mean()


# In[14]:


a_square.std()


# In[15]:


#6 A common statistical operation on a dataset is centering. This means to adjust the data such that 
# the mean of the data is 0. This is done by subtracting the mean from each data point. 
# Center the data set. See this link for more on centering.

a.mean()
center_array = a - a.mean()
center_array
center_array.mean()


# In[16]:


center_array.mean()


# In[17]:


#7 Calculate the z-score for each data point. Recall that the z-score is given by:

# Z =x−μ/σ
(a - a.mean()) / a.std()


# In[18]:


z_score = centered_a / a.std()


# In[ ]:


#8 Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add 
# your solutions.


# In[ ]:


import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = np.array(a)

# Use python's built in functionality/operators to determine the following:


# In[ ]:


# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

sum_of_a = np.sum(a)
sum_of_a
#sum(a)


# In[ ]:





# In[ ]:


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = a.min()
min_of_a
#min(a)


# In[ ]:


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = a.max()
max_of_a
#max(a)


# In[ ]:


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = a.mean()
mean_of_a
#mean(a)


# In[ ]:


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the 
#above list together
product_of_a = np.prod(a)
product_of_a


# In[ ]:


product_of_a = 1
for n in a:
    product_of_a *= n


# In[ ]:


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = np.square(a)
squares_of_a


# In[ ]:


[n**2 for n in a]


# In[ ]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = a[a % 2 != 0].size
odds_in_a


# In[ ]:


2 !=0][n for n in a if n %]


# In[ ]:


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = a[a % 2 == 0].size
evens_in_a


# In[ ]:


n for n


# In[ ]:


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares 
#for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

b2 = np.array(b)


# In[ ]:


#sum
sum_of_b2 = np.sum(b)
sum_of_b2


# In[ ]:


#min
b2.min()


# In[ ]:


#max
b2.max()


# In[ ]:


#mean
b2.mean()


# In[ ]:


#product
product_of_b2 = np.prod(b2)
product_of_b2


# In[ ]:


#list of squares 
squares_of_b2 = np.square(b2)
squares_of_b2


# In[ ]:


# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
#**Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b2 = 0
for row in b2:
    sum_of_b2 += sum(row)
b2.sum()


# In[ ]:


# Exercise 2 - refactor the following to use numpy. 
min_of_b2 = min(b2[0]) if min(b2[0]) <= min(b2[1]) else min(b2[1]) 
min_of_b2


# In[ ]:


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b2 = max(b2[0]) if max(b2[0]) >= max(b2[1]) else max(b2[1])
max_of_b2


# In[ ]:



# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b2 = (sum(b2[0]) + sum(b2[1])) / (len(b2[0]) + len(b2[1]))
mean_of_b2


# In[ ]:


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b2 = 1
for row in b2:
    for number in row:
        product_of_b2 *= number


# In[ ]:


np.prod(b2)


# In[ ]:


# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b2 = []
for row in b2:
    for number in row:
        squares_of_b2.append(number**2)


squares_of_b2


# In[ ]:


np.square(b2)


# In[ ]:


b2**2


# In[ ]:


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b2 = []
for row in b2:
    for number in row:
        if(number % 2 != 0):
            odds_in_b2.append(number)


odds_in_b2


# In[ ]:


b2[b2% 2 != 0]


# In[ ]:


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)


# In[ ]:





# In[ ]:


# Exercise 9 - print out the shape of the array b.

b2.shape


# In[ ]:


# Exercise 10 - transpose the array b.

b2


# In[ ]:


b2.transpose()


# In[ ]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

b2.reshape(1,6)


# In[ ]:





# In[ ]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

b2.reshape(6,1)


# In[ ]:


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

c= np.array(c)
c.min(), c


# In[ ]:


# Exercise 2 - Determine the standard deviation of c.

c.std()


# In[ ]:


# Exercise 3 - Determine the variance of c.

c.var()


# In[ ]:


# Exercise 4 - Print out the shape of the array c
c.shape


# In[ ]:


# Exercise 5 - Transpose c and print out transposed result.
c1 = c.transpose()
c.transpose()
c1


# In[ ]:


# Exercise 6 - Get the dot product of the array c with c. 
np.dot(c,c)


# In[ ]:


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
sum(c*c1)
np.sum(c * c.transpose())


# In[ ]:


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.



# In[ ]:


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]


d = np.array(d)


# In[ ]:


# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)


# In[ ]:


# Exercise 2 - Find the cosine of all the numbers in d

np.cos(d)


# In[ ]:


# Exercise 3 - Find the tangent of all the numbers in d

np.tan(d)


# In[ ]:


# Exercise 4 - Find all the negative numbers in d

d[d <0]


# In[ ]:


# Exercise 5 - Find all the positive numbers in d

d[d >0]


# In[ ]:


# Exercise 6 - Return an array of only the unique numbers in d.

np.uniques(d)


# In[ ]:


# Exercise 7 - Determine how many unique numbers there are in d.

len(np.uniques(d))


# In[ ]:


# Exercise 8 - Print out the shape of d.

d.shape


# In[ ]:


# Exercise 9 - Transpose and then print out the shape of d.

d.transpose().shape


# In[ ]:


# Exercise 10 - Reshape d into an array of 9 x 2
d.reshape(d (9,2))


# In[ ]:





# In[ ]:





# In[ ]:




