#!/usr/bin/env python
# coding: utf-8

# # Step 0: Imports and Reading Data
# 

# In[116]:


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
#pd.set_option('max_columns', 150)


# In[117]:


#read the data file
df= pd.read_csv('/Users/taghridyassergomaa/Downloads/archive/coaster_db.csv')
df


# # Step 1: Data Understanding

# In[118]:


df.shape


# In[119]:


df.head()


# In[120]:


df.columns


# In[121]:


df.dtypes


# In[122]:


df.describe()


# # Step 2: Data Preperation

# In[123]:


df[['coaster_name',
    #'Length', 'Speed',
    'Location', 'Status',
    #'Opening date',
    
    #   'Type',
    'Manufacturer',
    #'Height restriction', 'Model', 'Height',
       #'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
       #'Duration', 'Capacity', 'G-force', 'Designer', 'Max vertical angle',
       #'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
       #'Track layout', 'Fastrack available', 'Soft opening date.1',
      # 'Closing date', 
    #'Opened',
    #'Replaced by', 'Website',
       #'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
       #'Single rider line available', 'Restraint Style',
       #'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
       'year_introduced', 'latitude', 'longitude', 'Type_Main',
       'opening_date_clean',
    #'speed1', 'speed2', 'speed1_value', 'speed1_unit',
       'speed_mph',
    #'height_value', 'height_unit', 
    'height_ft','Inversions_clean', 'Gforce_clean']]


# In[124]:


#example of dropping
#df.drop(['Opening date'], axis = 1)


# In[125]:


df=df[['coaster_name',
    #'Length', 'Speed',
    'Location', 'Status',
    #'Opening date',
    
    #   'Type',
    'Manufacturer',
    #'Height restriction', 'Model', 'Height',
       #'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
       #'Duration', 'Capacity', 'G-force', 'Designer', 'Max vertical angle',
       #'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
       #'Track layout', 'Fastrack available', 'Soft opening date.1',
      # 'Closing date', 
    #'Opened',
    #'Replaced by', 'Website',
       #'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
       #'Single rider line available', 'Restraint Style',
       #'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
       'year_introduced', 'latitude', 'longitude', 'Type_Main',
       'opening_date_clean',
    #'speed1', 'speed2', 'speed1_value', 'speed1_unit',
       'speed_mph',
    #'height_value', 'height_unit', 
    'height_ft','Inversions_clean', 'Gforce_clean']].copy()


# In[126]:


df.shape


# In[127]:


df.dtypes


# In[128]:


pd.to_datetime(df['opening_date_clean'])


# In[129]:


df['opening_date_clean'] = pd.to_datetime(df['opening_date_clean'])


# In[130]:


pd.to_numeric(df['year_introduced'])


# # #rename our columns
# 

# In[131]:


df= df.rename(columns={'coaster_name':'Coaster_Name','year_introduced':'Year_Introduced','opening_date_clean':'Opening_Date'})


# In[132]:


df.head()


# In[133]:


df.isna().sum()


# In[134]:


df.duplicated()


# In[135]:


df.loc[df.duplicated()]


# In[136]:


# Check for duplicate coaster name
df.loc[df.duplicated(subset=['Coaster_Name'])].head(5)


# In[137]:


# Checking an example duplicate
df.query('Coaster_Name == "Crystal Beach Cyclone"')


# In[138]:


df.columns


# In[139]:


df= df.loc[~df.duplicated(subset=['Coaster_Name','Location','Opening_Date'])]     .reset_index(drop=True).copy()


# In[140]:


df.shape


# # Step 3: Feature Understanding
# Histogram
# KDE
# Boxplot

# In[141]:


df['Year_Introduced'].value_counts()


# In[142]:


ax = df['Year_Introduced'].value_counts().head(10).plot(kind='bar', title='Top Years Coasters Introduced')
ax.set_xlabel('Year_Introduced')
ax.set_ylabel('Count')


# In[143]:


ax = df['speed_mph'].plot(kind='hist',bins=20,title='Coaster Speed (mph)')
ax.set_xlabel('Speed(mph)')


# In[144]:


ax = df['speed_mph'].plot(kind='kde',title='Coaster Speed (mph)')
ax.set_xlabel('Speed(mph)')


# # Step 4: Feature Relationships
# ##Scatterplot
# Heatmap Correlation
# Pairplot
# Groupby comparisons

# In[145]:


df.plot(kind='scatter',x='speed_mph',y='height_ft',title='coaster Speed VS Height')
plt.show()


# In[146]:


ax = sns.scatterplot(x='speed_mph',
                y='height_ft',
                hue='Year_Introduced',
                data=df)
ax.set_title('Coaster Speed vs. Height')
plt.show()


# In[147]:


sns.pairplot(df,vars=['Year_Introduced','speed_mph',
                   'height_ft','Inversions_clean', 'Gforce_clean'] ,hue='Type_Main')
plt.show()


# In[148]:


df_corr = df[['Year_Introduced','speed_mph',
                   'height_ft','Inversions_clean', 'Gforce_clean']].dropna().corr()
df_corr


# In[149]:


sns.heatmap(df_corr, annot= True)


# # Step 5: Ask a Question about the data using a plot or statistic

# Try to answer a question you have about the data using a plot or statistic.
# What are the locations with the fastest roller coasters (minimum of 10)?

# In[150]:


ax = df.query('Location != "Other"')     .groupby('Location')['speed_mph']     .agg(['mean','count'])     .query('count >= 10')     .sort_values('mean')['mean']     .plot(kind='barh', figsize=(12, 5), title='Average Coast Speed by Location')
ax.set_xlabel('Average Coaster Speed')
plt.show()


# In[ ]:





# In[ ]:




