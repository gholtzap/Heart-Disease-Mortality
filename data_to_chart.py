import csv
import matplotlib.pyplot as plt

data = '''Stratification1,Stratification2,Heart Disease Mortality per 100k population
Female,Hispanic,221.8
Female,Hispanic,146.2
Female,Hispanic,123.4
Female,Hispanic,261.9
Female,Hispanic,68.6
Female,Hispanic,157.1
Female,Hispanic,137
Female,Hispanic,170.6
Female,Hispanic,54.1
Female,Hispanic,156.8
Female,Hispanic,222.3
Female,Hispanic,174.3
Female,Hispanic,278.9
Female,Hispanic,122.5
Female,Hispanic,190.3
Female,Hispanic,68.2
Female,Hispanic,203.5
Female,Hispanic,166.1
Female,Hispanic,226.8
Female,Hispanic,139.3
Female,Hispanic,97.7
Female,Hispanic,176
Female,Hispanic,140
Female,Hispanic,168.1
Female,Hispanic,49.1
Female,Hispanic,142.7
Female,Hispanic,196.3
Female,Hispanic,150
Female,Hispanic,134.9
Female,Hispanic,159.8
'''

rows = list(csv.reader(data.splitlines()))
header = rows.pop(0)

# Add row numbers to each row
numbered_rows = [[i+1] + row for i, row in enumerate(rows)]

# Create a new figure and axis
fig, ax = plt.subplots()
ax.axis('off')

# Create a table and display it in the new window
table = ax.table(cellText=numbered_rows, colLabels=["#"] + header, loc='center', cellLoc='center', colWidths=[0.1, 0.3, 0.3, 0.3])
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)

# Show the window with the table
plt.show()
