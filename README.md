# MYSQL_EXCEL
connecting MySQL and Excel to perform analysis

The Connection.py File uses mysql connector to connection python and Mysql
Pandas is used to parse the xlsx file into dataframe and then the data is pushed into tables using the mysql connector

The Graph.py file utilizes the matplotlib library to display a graph for rolling window from the excel file
* Working on implementing a solution to also be able read from mysql table and create a graph
