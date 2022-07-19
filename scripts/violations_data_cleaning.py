#!/usr/bin/env python
# coding: utf-8

# In[124]:


import pandas as pd
from collections import Counter
import re


# In[125]:


CSV_INPUT_FILE = 'Food_Inspections.csv'
CSV_OUTPUT_FILE = 'Food_Inspections_violations_cleaned.csv'


# In[126]:



df = pd.read_csv('/Users/rtikes/university-illinois/cs513-data-cleaning/final-project/Chicago-Food-Inspection/'+CSV_INPUT_FILE, sep=',')
print(len(df))
violations = df["Violations"].fillna('')


# In[128]:


df['Violations_Numbers'] = df['Violations'].str.findall(r'^[1-9]\d{0,1}\.\s|\s[1-9]\d{0,1}\.\s').fillna('')


# In[129]:


df.head()


# In[130]:


def replace_period(value):
    if type(value) == str:
        res = value.replace('.', '')
        return res
    else:
        return sorted(int(x.replace('.', '').strip()) for x in value)


# In[131]:


a = list(df['Violations_Numbers'])


# In[132]:


new_arr = [replace_period(x) for x in a]

df['Violations_Numbers'] = pd.Series(new_arr , dtype='str')


# In[101]:


df.head()


# In[133]:


df[['Violations_Numbers']].to_csv(
        '/Users/rtikes/university-illinois/cs513-data-cleaning/final-project/cs513-final-project/scripts/violations.csv', index=False)


# In[134]:


df.to_csv("/Users/rtikes/university-illinois/cs513-data-cleaning/final-project/cs513-final-project/scripts/"+CSV_OUTPUT_FILE, index=False)

