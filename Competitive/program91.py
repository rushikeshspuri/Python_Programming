import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

print("-"*50)
print("Question 3")
print("-"*50)

average_study_hours = df["StudyHours"].mean()
average_attendance = df["Attendance"].mean()
maximum_previous_score = df["PreviousScore"].max()
minimum_sleep_hours = df["SleepHours"].min()

print("-"*50)
print(f"Average Study hours : {average_study_hours}")
print(f"Average Attendance : {average_attendance}")
print(f"Maximum previous Score : {maximum_previous_score}")
print(f"Minimum sleep hours : {minimum_sleep_hours}")
print("-"*50)