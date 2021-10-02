from datetime import datetime #importar, aunque solo usare el split para formatear la fecha.
import os #importar para la creacion del segundo archivo


#funcion para darle el formato a la fecha
def inv_fecha(fecha):
    newFecha = datetime.strptime(fecha,'%d/%m/%Y')
    return datetime.strftime(newFecha,'%Y-%m-%d')

#funcion para calcular el sueldo+bono
def calcBono(sueldo,horas,porcentaje1,porcentaje2):
    #print(str(sueldo)+str(horas)+str(porcentaje1)+str(porcentaje2))
    if int(horas) <= 5:
        newSueldo= float(sueldo) + float(sueldo) / 100 * float(porcentaje1)
    else:
        newSueldo= float(sueldo) + float(sueldo) / 100 * float(porcentaje2)
    return float(newSueldo)

#datos a solicitar para calcular los bonos segun horas extras semanales

print("EMPRESA YABADABADU")
print("____________________________________________________________")
print("|                                                          |")

#aqui  juego con la validacion de los datos ingresados
while True:
    try:
        bono1 = int(input("Ingrese el nro correspondiente al % de bono General: "))
        bono2 = int(input("Ingrese el nro correspondiente al % de bono Eficiencia: "))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if bono1 < 0 and bono2 < 0 :
        print("Debes escribir un número positivo.")
        continue
    else:
        break

   
#para crear el segundo archivo con informacion nueva
file = open("pago_nomina_12sep2021.py", "w")

#proceso de lectura y escritura
with open("nomina.txt", "r") as nomina:
    for linea in nomina:

        #creamos la variable contenedora de los campos
        val = linea.split()

        #invertimos el formato de la fecha, debemos validar si es fecha
        #pero para el ejemplo solo validaremos si no es la fila que tiene titulo
        if val[0].isdigit():
            fecha = inv_fecha(val[1])
            sueldoE = calcBono(val[4].replace("$",""),val[5],bono1,bono2)
        else:
            fecha = val[1]
            sueldoE = val[3]

        #hacer el calculo para determinar el monto a pagar 

        #pasamos los valores al nuevo archivo
        file.write(val[0]+" ")
        file.write(fecha+" ")
        file.write(val[2]+" ")
        file.write(val[3]+" ")
        file.write(val[4]+" ")
        

        #validar si no es null o lo de arriba
        if val[0].isdigit():
            file.write(val[5]+" ")
            file.write(str(sueldoE))
            file.write(os.linesep)
        else:
            file.write(os.linesep)
           
        

    file.close()




#file.write
