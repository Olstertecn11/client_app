import pandas as pd
import matplotlib.pyplot as plt

ruta = "./pacientes.xlsx" 
workbook1 = pd.ExcelFile(ruta)

df= pd.read_excel(workbook1)

valores= df[['Nombre', 'Edad', 'Pulso', 'Altura', 'Peso']]
x= valores['Nombre']
y1= valores['Edad']
y2= valores['Pulso']
y3= valores['Altura']
y4= valores['Peso']
figure, axis = plt.subplots(2, 2)
plt.xlabel('Nombre')
plt.xlabel('Nombre')
plt.xlabel('Nombre')
plt.xlabel('Nombre')
figure.suptitle('Datos de pacientes')
axis[0, 0].plot(x, y1)
axis[0, 0].set_title("Nombre x Edad")
axis[0,1].plot(x, y2)
axis[0,1].set_title("Nombre x Pulso")
axis[1,0].plot(x, y3)
axis[1,0].set_title("Nombre x Altura")
axis[1,1].plot(x, y4)
axis[1,1].set_title("Nombre x Peso")
plt.show()
