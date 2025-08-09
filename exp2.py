import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [28, 22, 35, 30, 25],
    'Department': ['HR', 'Engineering', 'HR', 'Engineering', 'Finance'],
    'Salary': [50000, 60000, 55000, 62000, 45000]
}

df = pd.DataFrame(data)

print("Basic Information:")
print(df.info())
print()

average_salary = df['Salary'].mean()
print("Average Salary:", average_salary)
print()

max_age_engineering = df[df['Department'] == 'Engineering']['Age'].max()
print("Maximum Age in Engineering:", max_age_engineering)
print()

high_earners = df[df['Salary'] > 50000]['Name']
print("Employees with Salary > 50000:")
print(high_earners.to_string(index=False))
print()

new_employee = pd.DataFrame({
    'Name': ['Frank'],
    'Age': [40],
    'Department': ['Finance'],
    'Salary': [55000]
})
df = pd.concat([df, new_employee], ignore_index=True)
print("DataFrame after adding Frank:")
print(df)
print()

df = df[df['Name'] != 'Eve']
print("DataFrame after removing Eve:")
print(df)