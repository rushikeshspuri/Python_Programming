import pandas as pd #Imports the Pandas library to work with tables (DataFrames).

print("-"*50)
print("Question 1")
print("-"*50)

#=============================================================================================================
# Step 2: Load the Dataset
#=============================================================================================================

df = pd.read_csv("student_performance_ml.csv")

#=============================================================================================================
# Step 3: Understand the Dataset
#=============================================================================================================

print("-" * 50)
print("First 5 records")
print("-" * 50)
print(df.head())   # head() used to print first 5 records

print("-" * 50)
print("Last 5 records")
print("-" * 50)
print(df.tail())    # tail() used to print last 5 records

print("-" * 50)
print("Rows and Columns")
print("-" * 50)
print("Rows :",df.shape[0])
print("Columns :",df.shape[1])

print("-" * 50)
print("Column names")
print("-" * 50)
print(df.columns)

print("-" * 50)
print("Data Types")
print("-" * 50)
print(df.dtypes)