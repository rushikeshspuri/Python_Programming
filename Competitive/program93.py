import pandas as pd

df = pd.read_csv("student_performance_ml.csv")


print("-" * 50)
print("Question 5")
print("-" * 50)

study_analysis = df.groupby("FinalResult")["StudyHours"].mean()
attendance_analysis = df.groupby("FinalResult")["Attendance"].mean()

print("Average Study Hours by Result:")
print(study_analysis)

print("\nAverage Attendance by Result:")
print(attendance_analysis)