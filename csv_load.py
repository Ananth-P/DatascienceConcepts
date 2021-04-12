import pandas as pd

# Import the Pandas library
# Name the data frame as health_data.
# header=0 means that the headers for the variable names are to be found in the first row (note that 0 means the first row in Python)
# sep="," means that "," is used as the separator between the values. This is because we are using the file type .csv (comma separated values)

health_data = pd.read_csv('data.csv',header=0,sep=",")
#Note all blank cells can be converted into NaN as default by loading with Pandas
print(health_data)

# To display first 5 rows
print(health_data.head())

# cleaning dirty or wrongly or unregistered values
# Removing the NaN cells gives us a clean data set that can be analyzed. axis=0 means that we want to remove all rows that have a NaN value:
health_data.dropna(axis=0,inplace = True)
print(health_data)

#We can use the info() function to list the data types within our data set
print(health_data.info())

# We can use the astype() function to convert the data into anytype. 
health_data["Average_Pulse"] = health_data['Average_Pulse'].astype(float)
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)

print (health_data.info())

#analyzing data
print(health_data.describe())



