import pandas as pd
import matplotlib.pyplot as plt

workbook1 = pd.ExcelFile(r'C:\Users\Luis\Desktop\pacientes.xlsx')

df= pd.read_excel(workbook1)

valores= df[['Nombre', 'Edad', 'Pulso', 'Altura', 'Peso']]

ax= valores.plot.line( x='Nombre', y=['Edad','Pulso', 'Altura', 'Peso'])
plt.show()

