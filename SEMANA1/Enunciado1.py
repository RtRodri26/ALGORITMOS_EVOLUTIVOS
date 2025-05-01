#TREJO OBREGON RODRIGO EMILIO   ----  0202114056
import numpy as np

# Definición de colores ANSI
verde = "\033[92m"
azul = "\033[94m"
amarillo = "\033[93m"
negrita = "\033[1m"
reset = "\033[0m"

# Encabezado
print(azul + "="*60)
print(negrita + "         ANÁLISIS DE CAFETERÍAS - PRESUPUESTO S/10         " + reset)
print(azul + "="*60 + reset)

# Datos: nombres y precios por cafetería
nombres_cafeterias = ['A', 'B', 'C', 'D']
precios = np.array([2.50, 3.00, 1.75, 2.20])  # Precios de café

# Tabla de precios
print(f"\n{negrita}Tabla de Precios por Cafetería:{reset}")
print("-"*50)
for i, precio in enumerate(precios):
    print(f" Cafetería {nombres_cafeterias[i]}: S/{precio:.2f}")
print("-"*50)

# Cálculo del número de cafés posibles con S/10
max_cafes = np.floor(10 / precios).astype(int)

# Mostrar cuántos cafés puede comprar en cada cafetería
print(f"\n{negrita}Cantidad de cafés que se pueden comprar con S/10:{reset}")
for i, cantidad in enumerate(max_cafes):
    print(f" Cafetería {nombres_cafeterias[i]}: {cantidad} cafés")
print("-"*50)

# Análisis final
cantidad_maxima = max_cafes.max()
indice_maximo = max_cafes.argmax()
precio_minimo = precios.min()
indice_precio_minimo = precios.argmin()

# Resultados finales destacados
print(f"\n{negrita}RESULTADOS:{reset}")
print(f"{verde}Máxima cantidad de cafés: {cantidad_maxima} en la cafetería {nombres_cafeterias[indice_maximo]}{reset}")
print(f"{amarillo}Precio más bajo: S/{precio_minimo:.2f} en la cafetería {nombres_cafeterias[indice_precio_minimo]}{reset}")
print(azul + "="*60 + reset)
