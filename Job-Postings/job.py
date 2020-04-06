#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 08:04:44 2020

@author: deepak
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Dataframe (or Dataset)
ds = pd.read_csv('Data.csv')
ds = ds[['Title','JobDescription','JobRequirment','RequiredQual','IT']]

# dropped ALL 'nan' values
ds_filtered = ds.dropna()

record = ds_filtered.iloc[593, :]