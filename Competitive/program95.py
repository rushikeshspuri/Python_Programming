import matplotlib.pyplot as plt
import pandas as pd

print("-" * 50)
print("Question 7")
print("-" * 50)


df = pd.read_csv("student_performance_ml.csv")

plt.scatter(df["StudyHours"], df["FinalResult"])

plt.xlabel("Study Hours")
plt.ylabel("Final Result")
plt.title("Study Hours vs Final Result")

plt.show()