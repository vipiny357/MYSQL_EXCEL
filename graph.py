import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Reading excel file
df= pd.read_excel('HINDALCO_1D.xlsx',sheet_name='HINDALCO')
#  converting the dataframe to numpy array
data_array=np.array(df)
close=[]
# open=[]
datet=[]
len_of_array=len(df.index)
# creating a variable for each row and inserting it one by one
for i in range (0,len_of_array):
# for i in range (0,10):

    datetime1 = data_array[:,0][i]
    close1 = data_array[:,1][i]
#     high1 = data_array[:,2][i]
#     low1 = data_array[:,3][i]
    # open1 = data_array[:,4][i]
#     volume1 = data_array[:,5][i]
#     instrument1 = data_array[:,6][i]

    datet.append(datetime1)
    close.append(close1)
    # open.append(open1)


close_array_with_20=list(np.array(df['close'].rolling(window = 20, min_periods = 1).mean()))

close_array_with_50=list(np.array(df['close'].rolling(window = 50, min_periods = 1).mean()))

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(datet, close,label='close price')  # Plot the closing price on y axis and date on x axis on the axes.
ax.plot(datet, close_array_with_20, label='close rolling price with 20') # Plot the rolling price on y axis and date on x axis on the axes.

ax.plot(datet, close_array_with_50, label='close rolling price with 50') # Plot the rolling price on y axis and date on x axis on the axes.
ax.set_xlabel("date") # Setting up the date on x axis label
ax.set_ylabel("price") # setting up of price on y axis label
ax.legend()

plt.show()
