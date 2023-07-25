#!/usr/bin/env python
# coding: utf-8

# * head() - It shows the first N rows in the data (by default, N=5).
# * shape - It shows the total no. of rows and no. of columns of the dataframe
# * index - This attribute provides the index of the dataframe
# * columns - It shows the name of each column
# * dtypes - It shows the data-type of each column
# * unique() - In a column, it shows all the unique values. It can be applied on a single column only, not on the whole dataframe.
# * nunique() - It shows the total no. of unique values in each column. It can be applied on a single column as well as on the whole dataframe.
# * count - It shows the total no. of non-null values in each column. It can be applied on a single column as well as on the whole dataframe.
# * value_counts - In a column, it shows all the unique values with their count. It can be applied on a single column only.
# * info() - Provides basic information about the dataframe.

# In[1]:


import pandas as pd
df = pd.read_csv(r"C:\Users\sonik\Downloads\1. Weather Data.csv")
df


# In[2]:


# pd.set_option('display.max_rows', None)
# df


# # Q. 1)  Find all the unique 'Wind Speed' values in the data.

# In[3]:


df['Wind Speed_km/h'].nunique()


# In[4]:


df['Wind Speed_km/h'].unique()


# # Q. 2) Find the number of times when the 'Weather is exactly Clear'.

# In[5]:


# value_count
df.Weather.value_counts()


# In[6]:


# filtering
df[df['Weather'] == 'Clear']


# In[7]:


# group_by
df.groupby('Weather').get_group('Clear')


# # Q. 3) Find the number of times when the 'Wind Speed was exactly 4 km/h'.

# In[8]:


df[df['Wind Speed_km/h'] == 4]


# In[9]:


df['Wind Speed_km/h'].value_counts().loc[4]


# # Q. 4) Find out all the Null Values in the data.

# In[10]:


df.isnull()


# In[11]:


df.isnull().sum()


# # Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

# In[12]:


df.columns


# In[13]:


df.columns = ['Date/Time', 'Temp_C', 'Dew Point Temp_C', 'Rel Hum_%',
       'Wind Speed_km/h', 'Visibility_km', 'Press_kPa', 'Weather Condition']


# In[14]:


df


# In[25]:


df1 = df.rename(columns={'Weather':'Weather Condition'}, inplace=True)
df1


# In[26]:


df


# # Q. 6) What is the mean 'Visibility' ?

# In[27]:


df['Visibility_km'].mean()


# # Q. 7) What is the Standard Deviation of 'Pressure'  in this data?

# In[18]:


df['Press_kPa'].std()


# # Q. 8) What is the Variance of 'Relative Humidity' in this data ?

# In[19]:


df['Rel Hum_%'].var()


# # Q. 9) Find all instances when 'Snow' was recorded.

# In[21]:


df['Weather Condition'].value_counts()


# In[31]:


df[df['Weather Condition'] == 'Snow']


# In[36]:


df[df['Weather Condition'].str.contains('Snow') ]


# # Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.

# In[40]:


df[(df['Wind Speed_km/h'] > 25 ) & (df['Visibility_km'] == 25)]


# # Q. 11) What is the Mean value of each column against each 'Weather Condition ?

# In[41]:


df.groupby('Weather Condition').mean()


# # Q. 12) What is the Minimum & Maximum value of each column against each 'Weather Condition ?

# In[43]:


df.groupby('Weather Condition').min()


# In[44]:


df.groupby('Weather Condition').max()


# # Q. 13) Show all the Records where Weather Condition is Fog.

# In[20]:


df[df['Weather Condition'] == 'Fog']


# # Q. 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.

# In[49]:


df[(df['Weather Condition'] == 'Clear') | (df['Visibility_km'] > 40)]


# # Q. 15) Find all instances when :
# A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
# or
# B. 'Visibility is above 40'
# 

# In[50]:


df[(df['Weather Condition'] == 'Clear') | (df['Rel Hum_%'] > 50)]


# In[ ]:




