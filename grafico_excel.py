from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt

<<<<<<< HEAD
=======
ruta = "./pacientes.xlsx" 
workbook1 = pd.ExcelFile(ruta)
>>>>>>> f3ee415dbcd2e143b8e5e46fc7cce82b57166ea5

def grafico_excel(ruta=r'C:\Users\Luis\Desktop\5to semestre\Progra III\client_app\pacientes.xlsx'):
    workbook1 = pd.ExcelFile(ruta)
    df= pd.read_excel(workbook1)
    valores= df[['Nombre', 'Pulso']]
    valores.plot( y=['Pulso'], kind='line')
    plt.show()

grafico_excel()