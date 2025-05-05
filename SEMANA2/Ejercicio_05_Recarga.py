import numpy as np 

# Datos de los paquetes
gb = np.array([1, 2, 5, 9, 20])         # Cantidad de GB
precios = np.array([5, 9, 10, 20, 35])  # Precios en soles

# Calcular el costo por GB
costo_por_gb = precios / gb

# Mostrar el costo por GB de cada paquete en formato tabla
print("============================================")
print("         COSTO POR GB DE CADA PAQUETE        ")
print("============================================")
print(f"{'Paquete (GB)':<15}{'Precio (S/)':<15}{'Costo por GB (S/)'}")
print("--------------------------------------------")
for i in range(len(gb)):
    print(f"{gb[i]:<15}{precios[i]:<15}{costo_por_gb[i]:.2f}")
print("============================================")

# Encontrar el paquete más económico por GB
min_costo = np.min(costo_por_gb)
indice_min = np.argmin(costo_por_gb)

# Mostrar el paquete más económico
print("\n>>> PAQUETE MÁS ECONÓMICO POR GB <<<")
print("--------------------------------------------")
print(f"Paquete: {gb[indice_min]} GB")
print(f"Precio: S/ {precios[indice_min]}")
print(f"Costo por GB: S/ {min_costo:.2f}")
print("============================================")
