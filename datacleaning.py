# -*- coding: utf-8 -*-
"""Datacleaning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17FZ1kd8Rl9Xrpq7-7plyyjQ7REsbNR7L
"""

import pandas as pd
import numpy as np
import io

#Import the file from desktop
from google.colab import files
uploaded = files.upload()

df = pd.read_csv('fifa21_raw_data.csv')

#Examine the first few entries
df.head()

#Look at all the columns
pd.set_option('display.max_columns', None)
df.head()

'''
Dropping columns:
Decide which columns seem unnecessary to
the analysis. Columns such as photoUrl can be
taken out of the DataFrame.
To drop: photoUrl, playerUrl, ID, Hits
'''
to_drop = ['photoUrl',
           'playerUrl',
           'ID',
           'Hits']

#Drop them from the DataFrame
df.drop(to_drop, inplace=True, axis=1)

#Confirm that they columns are dropped
df.head()

#Explore columns
df.info()

df.shape

