import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('graficobarra.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

#fig = plt.figure()
#ax = fig.add_axes([0,0,1,1])
#langs = ['C', 'C++', 'Java', 'Python', 'PHP']
#students = [23,17,35,29,12]
#ax.bar(langs,students)
#plt.show()

plt.bar(x,y, label='Gráfico de barra!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de barra carregado do excel')
plt.legend()
plt.show()