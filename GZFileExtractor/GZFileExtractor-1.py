#!/usr/bin/env python
# coding: utf-8

# In[5]:


print("Enter the source folder name and destination folder name without / at the end. ")


# In[6]:


import gzip
import glob
import os
import os.path
import shutil


# In[10]:


filesRead = []
destinationFolder = 'destfolder' #Enter the destination folder here
folderToStartSearching = 'data' #Enter the folder to start searching from here


# In[24]:


folderToStartSearching = input ("Enter folder path to start searching from: ")


# In[31]:


destinationFolder = input("Enter destination folder: Note: Use . notation to traverse through directory: ")


# In[32]:


folderToStartSearching = os.path.abspath(folderToStartSearching)


# In[33]:


destinationFolder = os.path.abspath(destinationFolder)


# In[34]:


destinationFolder


# In[29]:


if not os.path.exists(destinationFolder):
    os.makedirs(destinationFolder)


# In[30]:


filesRead = []
for index, filename in enumerate(glob.iglob(folderToStartSearching+'/**', recursive = True)):
    print("Currently reading... ", filename)

            
            
            
    if (filename.endswith('.gz') and not any(filename in x for x in filesRead )):
        with gzip.open(filename, 'rb') as f_in:
            with open(destinationFolder+"/"+filename.split("/")[-1][:-3], 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
                
    filesRead.append(filename)


# In[ ]:


print("The files read are ", filesRead)

