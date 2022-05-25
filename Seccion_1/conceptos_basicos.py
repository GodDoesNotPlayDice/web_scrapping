# Hacer archivos con with
with open("archivo.txt","w") as archivo:
    archivo.write("Data correctamente Extraida")


# Recordar que con la funcion open tenemos primero el nombre del archivo como paramentro
# y luego tenemos el parametro de creacion + escritura (+a) o lectura y escritura (r,w) 

import pandas as pd
paises = ["Mexico","Colombia","Peru","Argentina"]
poblacion = [132820000, 50882884, 33105273, 45195777]
dict_poblacion = {"Paises": paises, "Poblacion": poblacion} # Crear el diccionario
df_poblacion = pd.DataFrame.from_dict(dict_poblacion) 
print(dict_poblacion)

# Crear el data frame que el data frame mas o menos se representa como una tabla de base de datos con un ID, y las tablas que tiene el diccionario con sus valores en listas
""""
      Paises  Poblacion
0     Mexico  132820000
1   Colombia   50882884
2       Peru   33105273
3  Argentina   45195777


"""
# Con esto podemos transformar el dataframe a un csv (excel)
df_poblacion.to_csv("poblacion.csv",index=False) # Orden de cada elemento de las columnas (index) True/False
