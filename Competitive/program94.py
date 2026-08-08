import pandas as pd
import matplotlib.pyplot as plt

# histogram
df = pd.read_csv("student_performance_ml.csv")

print("-" * 50)
print("Question 6")
print("-" * 50)

plt.hist(df["StudyHours"], bins=10, edgecolor="black")
plt.xlabel("StudyHours")
plt.ylabel("Number of Students")
plt.title("Distribution of Study Hours")

plt.show()