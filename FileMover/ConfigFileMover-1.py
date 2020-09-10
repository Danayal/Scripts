#!/usr/bin/env python
# coding: utf-8

# In[1]:


import configparser, os
import os
import os.path
import shutil
import glob


# In[2]:


filesRead = []


# In[3]:


config = configparser.ConfigParser()
#config.sections


# In[4]:


confFile = input ("Enter folder path to the configuration file : ")


# In[5]:


config.read(confFile)


# In[6]:


for key in config.sections():
    print(key)
    if (key == "SOURCEFOLDERNAME"):
        source_dict = dict(config.items(key))
    elif(key == "DESTINATIONFOLDERNAME"):
        dest_dict = dict(config.items(key))

sourceFolder = source_dict["source"]
destFolder = dest_dict["destination"]


# In[7]:


if not os.path.exists(destFolder):
    os.makedirs(destFolder)


# In[8]:


for index, filename in enumerate(glob.iglob(sourceFolder +'/**', recursive = True)):
    print("Currently reading... ", filename)
    if (os.path.isfile(filename)):
        shutil.move(filename, destFolder)

    filesRead.append(filename)

print("Done")


# In[ ]:
