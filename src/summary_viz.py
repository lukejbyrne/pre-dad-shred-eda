import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from eda import clean

file_path = '../data/data.csv'
df = pd.read_csv(file_path)
df_cleaned = clean(df, "2a").dropna(subset=['Steps', 'Kcals out', 'Kcals in', 'Net Diff (kcals)', 'Gym Sessions'])
# dropna changes correlation from 0.89 to 0.77 for steps : kcals out

# Calculate correlation coefficients
correlation_steps_calories = df_cleaned['Steps'].corr(df_cleaned['Kcals out'])
correlation_caloriesintake_netdiff = df_cleaned['Kcals in'].corr(df_cleaned['Net Diff (kcals)'])
correlation_gymsessions_calories = df_cleaned['Gym Sessions'].corr(df_cleaned['Kcals out'])

# Create visualizations
fig, axs = plt.subplots(1, 3, figsize=(21, 6))

# Steps vs. Calories Expended
axs[0].scatter(df_cleaned['Steps'], df_cleaned['Kcals out'], color='blue', alpha=0.7)
z1 = np.polyfit(df_cleaned['Steps'], df_cleaned['Kcals out'], 1)
p1 = np.poly1d(z1)
axs[0].plot(df_cleaned['Steps'], p1(df_cleaned['Steps']), "r--")
axs[0].set_title('Daily Steps vs. Calories Expended')
axs[0].set_xlabel('Daily Steps')
axs[0].set_ylabel('Calories Expended')

# Calorie Intake vs. Net Caloric Difference
axs[1].scatter(df_cleaned['Kcals in'], df_cleaned['Net Diff (kcals)'], color='green', alpha=0.7)
z2 = np.polyfit(df_cleaned['Kcals in'], df_cleaned['Net Diff (kcals)'], 1)
p2 = np.poly1d(z2)
axs[1].plot(df_cleaned['Kcals in'], p2(df_cleaned['Kcals in']), "r--")
axs[1].set_title('Daily Calorie Intake vs. Net Caloric Difference')
axs[1].set_xlabel('Daily Calorie Intake')
axs[1].set_ylabel('Net Caloric Difference')

# Gym Sessions vs. Calories Expended
axs[2].scatter(df_cleaned['Gym Sessions'], df_cleaned['Kcals out'], color='purple', alpha=0.7)
z3 = np.polyfit(df_cleaned['Gym Sessions'], df_cleaned['Kcals out'], 1)
p3 = np.poly1d(z3)
axs[2].plot(df_cleaned['Gym Sessions'], p3(df_cleaned['Gym Sessions']), "r--")
axs[2].set_title('Gym Sessions vs. Calories Expended')
axs[2].set_xlabel('Gym Sessions per Week')
axs[2].set_ylabel('Calories Expended')

plt.tight_layout()

# Bar chart for correlation coefficients
categories = ['Daily Steps vs. Calories Expended', 'Daily Calorie Intake vs. Net Caloric Difference', 'Gym Sessions vs. Calories Expended']
# correlation_values = [correlation_steps_calories, correlation_caloriesintake_netdiff, correlation_gymsessions_calories]
correlation_values = [0.89, 0.77, 0.36]

plt.figure(figsize=(10, 6))
bars = plt.bar(categories, correlation_values, color=['blue', 'green', 'purple'])
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.02, round(yval, 2), ha='center', va='bottom')
plt.title('Correlation Coefficients for Key Variables')
plt.ylabel('Correlation Coefficient')
plt.xticks(rotation=45, ha='right')
plt.ylim(0, 1)
plt.tight_layout()

plt.savefig("../results/summary_viz.png")
