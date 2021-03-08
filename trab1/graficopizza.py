import matplotlib.pyplot as plt
import csv
sizes = []
x = []
y = []
with open('graficopizza.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    for row in plots:
        sizes.append(float(row[0]))
        sizes.append(float(row[1]))

labels = 'ValorEx1', 'ValorEx2', 'ValorEx3', 'ValorEx4'
explode = (0, 0.1, 0, 0)
fig1, ax1 = plt.subplots()
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.show()
