import pandas as pd
import numpy as np
import mysql.connector

# MYSQL CONNECTION
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="investo1"
)
mycursor = mydb.cursor()

# dropping the exsisting table
mycursor.execute("Drop table IF EXISTS HINDALCO")
# creating the required table
mycursor.execute("CREATE TABLE HINDALCO(datetime datetime, close decimal(5,2), high decimal(5,2), low decimal(5,2), open decimal(5,2), volume int(15), instrument varchar(20))")

# insert statement
add_data = "INSERT INTO HINDALCO (datetime,close,high,low,open,volume,instrument) VALUES (%s,%s,%s,%s,%s,%s,%s)"

# Reading excel file
df= pd.read_excel('HINDALCO_1D.xlsx',sheet_name='HINDALCO')
#  converting the dataframe to numpy array
data_array=np.array(df)

# creating a variable for each row and inserting it one by one
for i in range (0,len(df.index)):
# for i in range (0,10):

    datetime1 = data_array[:,0][i]
    close1 = data_array[:,1][i]
    high1 = data_array[:,2][i]
    low1 = data_array[:,3][i]
    open1 = data_array[:,4][i]
    volume1 = data_array[:,5][i]
    instrument1 = data_array[:,6][i]
    
    data_hind=(datetime1,close1,high1,low1,open1,volume1,instrument1)
    # print(data_hind)
    mycursor.execute(add_data,data_hind)

mydb.commit()

mycursor.execute("select * from HINDALCO")
for x in mycursor:
    print(x)

mydb.close()