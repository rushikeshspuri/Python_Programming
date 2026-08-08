import pandas as pd

print("-"*50)
print("Question 2")
print("-"*50)

df = pd.read_csv("student_performance_ml.csv")

print("-"*50)
print("Total Number of Students : ",len(df))
print("-"*50)

df[df["FinalResult"] == 1]
print("-"*50)
print("Passed Students : ",len(df[df["FinalResult"]==1]))
print("-"*50)

df[df["FinalResult"] == 0]
print("-"*50)
print("Failed Students : ",len(df[df["FinalResult"]==0]))
print("-"*50)