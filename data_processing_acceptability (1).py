#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import os


# In[18]:


resp=pd.read_csv("responces_block1_social_acceptability_panepistimiou.csv")
resp.head()
block=1


# In[19]:


index = resp.index
sample = len(index)
if block ==1:
    pid = range(101,sample+101) 
elif block==2:
    pid = range(201,sample+201) 
else:
    pid = range(301,sample+301)
resp["pid"]=pid

resp


# In[20]:


if block ==1:
    resp.columns = ["time","s6","s11","s24","s26","s29","s16","s7","s10","s13","s21","s27","s32",
                    "sex","age","modex","own","walk_purp","cycle_freq","cycle_purp",
                    "envi","stress","fatique","timeben","comfort","economy","autonomy","physical","secure",
                    "prestige","income","pid"] 
elif block==2:
        resp.columns = ["time","s2","s5","s18","s8","s19","s28","s36","s23","s13","s3","s22","s25",
                    "sex","age","modex","own","walk_purp","cycle_freq","cycle_purp",
                    "envi","stress","fatique","timeben","comfort","economy","autonomy","physical","secure",
                    "prestige","income","pid"]
else:
        resp.columns = ["time","s9","s1","s12","s14","s20","s4","s34","s15","s17","s30","s35","s31",
                    "sex","age","modex","own","walk_purp","cycle_freq","cycle_purp",
                    "envi","stress","fatique","timeben","comfort","economy","autonomy","physical","secure",
                    "prestige","income","pid"]
resp.head()


# In[21]:


socio=pd.DataFrame(columns=("pid","sex", "age", "income","car","bike","pt","bicycle","walk"))
socio.pid=resp.pid
socio.sex=resp.sex.replace({'Άνδρας': 1, 'Γυναίκα': 0, 'Άλλο':np.nan})
socio.age=resp.age.replace({'18-20 ετών': 19, '21-30 ετών':25, '31-40 ετών': 35,
                           '41-50 ετών':55, '51-65 ετών':58, '65 ή μεγαλύτερος/η':65})
socio.income=resp.income.replace({'500-1.000€':1, '1.001-1.500€':2, '1.501-2.000€':3, '>2.000€': 4, 
                                 'Δεν επιθυμώ να απαντήσω':np.nan})
socio.car=resp.modex.replace({'Αυτοκίνητο (οδηγός ή συνεπιβάτης)':1, 'Μηχανοκίνητο δίκυκλο':0, 'Δημόσια Συγκοινωνία':0, 'Ποδήλατο':0, 
                                 'Περπάτημα':0})
socio.bike=resp.modex.replace({'Αυτοκίνητο (οδηγός ή συνεπιβάτης)':0, 'Μηχανοκίνητο δίκυκλο':1, 'Δημόσια Συγκοινωνία':0, 'Ποδήλατο':0, 
                                 'Περπάτημα':0})
socio.pt=resp.modex.replace({'Αυτοκίνητο (οδηγός ή συνεπιβάτης)':0, 'Μηχανοκίνητο δίκυκλο':0, 'Δημόσια Συγκοινωνία':1, 'Ποδήλατο':0, 
                                 'Περπάτημα':0})
socio.bicycle=resp.modex.replace({'Αυτοκίνητο (οδηγός ή συνεπιβάτης)':0, 'Μηχανοκίνητο δίκυκλο':0, 'Δημόσια Συγκοινωνία':0, 'Ποδήλατο':1, 
                                 'Περπάτημα':0})
socio.walk=resp.modex.replace({'Αυτοκίνητο (οδηγός ή συνεπιβάτης)':0, 'Μηχανοκίνητο δίκυκλο':0, 'Δημόσια Συγκοινωνία':0, 'Ποδήλατο':0, 
                                 'Περπάτημα':1})

socio


# In[22]:


sc=list(resp.columns)
dataset=pd.DataFrame(columns=("pid","accept", "scenario"))
k=pd.DataFrame(columns=("pid","accept", "scenario"))
for item in sc[1:13]:
    k["pid"]=resp["pid"]
    k["accept"]=resp[item]
    k["scenario"]=item
    dataset=pd.concat([dataset, k], axis=0, ignore_index=True)
dataset


# In[23]:


expl=pd.read_csv("x_variables_design.csv")
expl


# In[24]:


dataset = pd.merge(left=dataset, right=expl, how="inner", left_on='scenario', right_on='scenario')
dataset = pd.merge(left=dataset, right=socio, how="inner", left_on='pid', right_on='pid')
dataset.shape
if block ==1:
    dataset.to_csv("dataset_block1.csv")
elif block==2:
    dataset.to_csv("dataset_block2.csv")
else:
    dataset.to_csv("dataset_block3.csv")

dataset


# In[25]:


data_block1=pd.read_csv("dataset_block1.csv")
data_block2=pd.read_csv("dataset_block2.csv")
data_block3=pd.read_csv("dataset_block3.csv")
final=pd.concat([data_block1, data_block2, data_block3], axis=0, ignore_index=True)
final=final.drop(columns=["Unnamed: 0"])
final.to_csv("final_dataset.csv")
final

