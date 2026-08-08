import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

print("-"*50)
print("Question 4")
print("-"*50)

print("-"*50)
print("Value count : ")
result_count = df["FinalResult"].value_counts()
print("-"*50)

print("-"*50)
print("Calculate pass percentage")
totalstudent = len(df)          #length of all rows / all students

pass_count = result_count[1]    # Give me the count associated with value 1. / 1 pass
fail_count = result_count[0]     # Give me the count associated with value 0. / 0 fail

pass_percentage = (pass_count/totalstudent) * 100
fail_percentage = (fail_count/totalstudent) * 100

print("Final Result Distribution:")
print(result_count)

print("Pass Percentage :", pass_percentage)
print("Fail Percentage :", fail_percentage)
