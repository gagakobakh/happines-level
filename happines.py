#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import matplotlib.pyplot as pt
import seaborn as se


# In[10]:


df=pd.read_csv("./years/2019.csv")
df


# In[11]:


correlations=df.corr()


# In[12]:


cols = ['GDP per capita',
       'Social support', 'Healthy life expectancy',
       'Freedom to make life choices', 'Generosity',
       'Perceptions of corruption',]

# Unpivot or melt the dataframe
df_melt = pd.melt(df, id_vars=['Country or region'], 
                  value_vars=cols, 
                  var_name='variable', 
                  value_name='point')
df_melt


# In[13]:


pt.figure(figsize=(8,4))


# In[16]:


box=se.boxplot(x='point', y='variable', data=df_melt, linewidth=2, fliersize=6, palette='Set2')


# In[18]:


pt.figure(figsize=(8,6))


# In[26]:


distr=se.histplot(df["Score"],kde=True)
pt.title("histogram of scores ",fontsize=16,pad=10)


# In[42]:


mean=round(df["Score"].mean(),2)
median=round(df["Score"].median(),2)
print('mean  :{}\nmedian   : {}' .format(mean, median))


# In[43]:


corr=df.corr()


# In[45]:


pt.figure(figsize=(8,6))


# In[52]:


correlation=se.heatmap(corr,cbar=True,annot=True)
correlation
pt.title("heat map of correlation",fontsize=16)


# gdp, social support , healthy life expectancy ყველაზე დიდი კორელაცია აქვთ ბედნიერების მაჩვენებელთან, ყველა 0.75ზე მაღალია

# TOP 10 happiest countries 
# 

# In[71]:


happy_10=df[["Country or region","Score"]].head(10)


# In[72]:


pt.figure(figsize=(8,6))


# In[74]:


xo=se.barplot(x="Score",y="Country or region",data=happy_10)
se.despine()


# In[ ]:




