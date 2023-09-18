#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #Datafrome
import numpy as np #Array(mathematical work)
import matplotlib.pyplot as plt #Graphs or Visualization
import seaborn as sns


# In[2]:


df = pd.read_csv("D:/mummy/pandas/Diwali Sales Data.csv", encoding = "unicode_escape")


# In[3]:


df


# In[4]:


df.shape


# In[5]:


df.columns


# In[6]:


df.head()


# In[7]:


df.tail()


# In[8]:


df.info()


# In[9]:


df.drop(["Status" , "unnamed1"], axis = 1, inplace = True)


# In[10]:


df.info()


# In[11]:


df.isnull()


# In[12]:


df.isnull().sum()


# In[13]:


df.shape


# In[14]:


df.dropna(inplace = True)


# In[15]:


df["Amount"] = df["Amount"].astype("int")


# In[16]:


df["Amount"].dtypes


# In[17]:


#Rename column
df.rename(columns={"Marital_Status":"Shaadi"})


# In[18]:


#describe()=this method is used to description of the dataframe(i.e count,std,mean etc)
df.describe()


# In[19]:


#use describe for specific column
df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis
# 
# Gender

# In[20]:


df.columns


# In[21]:


ax = sns.countplot(x = "Gender",data = df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[22]:


df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[23]:


sales_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Gender',y='Amount',data=sales_gen)


# # From the above Graphs we can see that the most of the buyers are females and even the puchasing power of  females are greater than men

# # Age

# In[24]:


ax = sns.countplot(data = df, x = 'Age Group', hue ='Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[25]:


#Total amount vs Age group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x="Age Group",y="Amount",data=sales_age)


# # From the above Graphs we can see that the most of the buyers are age group between 26-35years females

# # States

# In[26]:


# Total number of order from top 10 states
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state, x='State',y='Orders')


# In[27]:


sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state, x='State',y='Amount')


# # From the above Graph we can see that the order and total sales/amount are from Uttar pradesh, Maharashtra and Karnataka

# #Marital Status

# In[28]:


ax = sns.countplot(x="Marital_Status", data = df)
sns.set(rc={'figure.figsize':(5,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[29]:


sales_state=df.groupby(['Marital_Status','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(5,5)})
sns.barplot(data=sales_state, x = 'Marital_Status', y = 'Amount', hue='Gender')


# # From the above Graph we can see that the most of the buyers are married(women) and they have more purchasing power.

# Occupation

# In[30]:


ax=sns.countplot(x='Occupation', data = df)
sns.set(rc={'figure.figsize':(20,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[31]:


sales_state=df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x = 'Occupation', y = 'Amount')


# # From the above Graph we can see that the most of the buyers are working in IT sector, Healthcare and Aviation

# In[32]:


df.columns


# In[33]:


ax = sns.countplot(x='Product_Category',data= df)
sns.set(rc={'figure.figsize':(10,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[34]:


sales_state=df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head()
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x = 'Product_Category', y = 'Amount')


# #  From the above Graph we can see that the most sold products are from Food Clothing, footwears and Electronics category

# In[35]:


sales_state=df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x = 'Product_ID', y = 'Orders')


# # Married women age group 26-36years from Uttar Pradesh, Maharashtra and Karnataka working in IT Sector, Healthcare and Aviation are more likely to buy_Products from Food, Clothing and Electronics Category
