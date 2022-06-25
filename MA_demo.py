import numpy as np
import csv
import datetime
from matplotlib import pyplot as plt




##Getting data in 
data = []
with open(r"\Electric_Production.csv",mode = 'r') as file:
    csvfile = csv.reader(file)

    for line in csvfile:
        data.append(line)
## Moving Data into columns and changing dtypes
columns = list(zip(*data))
dates = columns[0][1:]
dates = list((datetime.datetime.strptime(str(ele),'%m/%d/%Y') for ele in dates))
dates = list(ele.date() for ele in dates)
nums = columns[1][1:]
nums = list(float(ele) for ele in nums)

##Moving Avg
window_size = 3
i = 0
moving_avgs = []

while i < len(nums) - window_size +1 :
    window_avg = round(np.sum(nums[i:i+window_size])/window_size,2)
    moving_avgs.append(window_avg)
    i+=1
moving_avgs = moving_avgs + [None,None] ##Adding 2 data points to match dimensions of x cord




plt.plot(dates,nums)
plt.plot(dates,moving_avgs)
plt.show()








