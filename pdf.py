from tkinter import font
from fpdf import FPDF
datos= ((12345, 54321, '85 BPM', '30/05/2022'),(13579, 246810, '75 BPM', '31/05/2022'),(98745, 54789, '105 BPM', '01/06/2022'),(11111, 22222, '95 BPM', '02/06/2022'))
pdf= FPDF(orientation='P',unit='mm',format='A4')
pdf.add_page()
pdf.set_font("Arial", size=12)
#encabezado de la tabla
pdf.cell(0,15,txt="Reporte de ritmo cardiaco",border=1,ln=3,align="C")
pdf.cell(40,15,txt="ID doctor",border=1,align="C",fill=0)
pdf.cell(40,15,txt="ID paciente",border=1,align="C",fill=0)
pdf.cell(45,15,txt="Pulso",border=1,align="C",fill=0)
pdf.multi_cell(0,15,txt="Fecha",border=1,align="C",fill=0) 

#Datos  de la tabla
for i in range(len(datos)):
    pdf.cell(40,15,txt=str(datos[i][0]),border=1,align="C",fill=0)
    pdf.cell(40,15,txt=str(datos[i][1]),border=1,align="C",fill=0)
    pdf.cell(45,15,txt=str(datos[i][2]),border=1,align="C",fill=0)
    pdf.cell(0,15,txt=str(datos[i][3]),border=1,align="C",fill=0)
    pdf.ln(15)

#metadata
pdf.set_title("MetaData report")
pdf.set_author("Dr. Strange")
pdf.set_creator("Clinica Santuario")
pdf.set_subject("Reporte de ritmo cardiaco")
pdf.set_keywords("Hoja, Reporte, PDF")

pdf.output("Reporte.pdf")
