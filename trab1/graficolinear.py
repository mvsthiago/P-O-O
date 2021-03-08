import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('graficolinear.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))



plt.plot(x,y, label='Gráfico de linear!')
plt.title('Gráfico linear carregado do excel')
plt.legend()
plt.show()