# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Create the dataset
data = {
    'Study Hours': [5, 15, 10, 20, 7, 8, 18, 12, 2, 6],
    'Attendance': [60, 90, 70, 95, 65, 75, 85, 80, 50, 55],
    'Pass': [0, 1, 0, 1, 0, 0, 1, 1, 0, 0]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Step 2: Explore the data
print("First few rows of the dataset:")
print(df.head())

# Check data types
print("\nDataset information:")
print(df.info())

# Check for outliers
print("\nSummary statistics:")
print(df.describe())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Step 3: Visualize the data
plt.figure(figsize=(10, 5))

# Scatter plot of Study Hours vs Attendance, colored by Pass
sns.scatterplot(data=df, x='Study Hours', y='Attendance', hue='Pass', palette='coolwarm')
plt.title('Study Hours vs Attendance (Pass/Fail)')
plt.xlabel('Study Hours')
plt.ylabel('Attendance (%)')
plt.legend(title='Pass (1) / Fail (0)', loc='upper left')
plt.grid(True)
plt.show()
