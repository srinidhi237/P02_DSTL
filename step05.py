import pandas as pd
import numpy as np

df = pd.read_csv('day02_usage.csv')

#Part A - Build the table
apps = ['Chat','Video','Study','Games'] # or apps = list(df.columns)- give all column names

arr = df[apps].to_numpy()  #or [df[f"{i}"].to_numpy() for i in apps] - but this gives array of array
print(arr)                   #here we are not considering 'Date' column

print("Size of arr: ",arr.shape)

''' line 9:
    [df[f"{i}"].to_numpy() for i in apps] - but this gives array of array
    Array of array - there will be no columns, only row wise elements

    arr = df[apps].to_numpy() - this gives a 2D array
    2D array - contains cols and rows (a table)

    df[apps] is ller to df[[]] - internal brackets will work as iterators,
     so each colname is picked and converted to numpy array

'''


#Part B
per_app = arr.sum(axis=0)
print("Per app sum(colsum):",per_app)

per_day = arr.sum(axis=1)
print("Per Day sum(rowsum):",per_day)

'''Why 0 - cols and 1 - rows???
    shape - gives a tuple : (rows,cols) ie, rows - 1st value in shape, cols-2nd value in shape
    axis=0 -> collapses 0 ie, rows (not consider rows)
    axis=1 -> collapses 1 ie, cols (don't consider cols)
'''

per_app_avg = np.round(arr.mean(axis=0),1)
print("Col Average:",per_app_avg)
per_day_avg = np.round(arr.mean(axis=1),1)
print("Row Average:",per_day_avg)

per_app_max = arr.max(axis=0)
print("Col max:",per_app_max)
per_day_max = arr.max(axis=1)
print("Row max:",per_day_max)

per_app_min = arr.min(axis=0)
print("Col min:",per_app_min)
per_day_min = arr.min(axis=1)
print("Row min:",per_day_min)




