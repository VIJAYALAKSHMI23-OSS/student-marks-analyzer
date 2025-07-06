import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Input student data
students = []
n = int(input("Enter number of students: "))
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    marks = float(input(f"Enter marks for {name}: "))
    students.append({'Name': name, 'Marks': marks})

# Step 2: Create DataFrame
df = pd.DataFrame(students)

# Step 3: Basic Analysis
print("\n--- Class Statistics ---")
print(f"Average Marks: {df['Marks'].mean():.2f}")
print(f"Highest Marks: {df['Marks'].max()} ({df[df['Marks'] == df['Marks'].max()]['Name'].values[0]})")
print(f"Lowest Marks: {df['Marks'].min()} ({df[df['Marks'] == df['Marks'].min()]['Name'].values[0]})")

# Step 4: Top 3 Students
top_students = df.sort_values(by='Marks', ascending=False).head(3)
print("\nTop 3 Students:")
print(top_students)

# Step 5: Visualization
plt.figure(figsize=(8, 5))
plt.bar(df['Name'], df['Marks'], color='skyblue')
plt.xlabel('Student Name')
plt.ylabel('Marks')
plt.title('Student Marks Distribution')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('marks_chart.png')
plt.show()

# Step 6: Export
df.to_csv('student_marks_output.csv', index=False)
print("\nData exported to student_marks_output.csv and marks_chart.png")
