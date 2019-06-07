#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas as pd

mdf = pd.read_excel('book1.xlsx', sheet_name="Sheet1")
menMeans = mdf['Mins']
menMeans = tuple(menMeans.values) # this produces a tuple from the mins column

quarters = mdf['Quarter']
quarters = tuple(quarters.values) # this produces a tuple from the quarter column

N = 4
#menMeans = (20, 35, 30, 35)
#menStd = (2, 3, 4, 1)
ind = np.arange(N)    # the x locations for the groups
width = 0.30       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width) # Blue Bottom Values

plt.ylabel('Outage Minutes')
plt.title('Outage Minutes by Quarter')
plt.xticks(ind, quarters) #xaxis data
plt.yticks(np.arange(0, 201, 15))
plt.legend((p1[0],), ('Minutes',))

now = datetime.datetime.now()
plt.savefig(now.strftime("%Y-%m-%d-outage.png"))
