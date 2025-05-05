import numpy as np  # Importamos la librería NumPy

# Presupuesto de Martina
presupuesto = 8.0  

# Lista de precios por página en cada copistería
precios = np.array([0.10, 0.12, 0.08])

# Calculamos cuántas páginas puede fotocopiar en cada copistería
paginas = np.floor(presupuesto / precios)

# Mostrar encabezado
print("=" * 50)
print(" ANÁLISIS DE FOTOCOPIAS SEGÚN COPISTERÍAS ".center(50))
print("=" * 50)

# Mostramos la cantidad de páginas posibles en cada copistería
print("Cantidad de páginas que Martina puede fotocopiar:")
print("-" * 50)
for i, p in enumerate(paginas):
    print(f"| Copistería {i + 1:<2} | {int(p):>3} páginas".ljust(49) + "|")
print("-" * 50)

# Identificamos la copistería donde puede sacar más copias
mejor_opcion = np.argmax(paginas)

# Mostramos la mejor opción
print(f"\n>> Mejor opción:")
print("-" * 50)
print(f"Martina debería elegir la Copistería {mejor_opcion + 1},")
print(f"ya que puede realizar {int(paginas[mejor_opcion])} fotocopias")
print(f"con su presupuesto de S/.{presupuesto:.2f}.")
print("=" * 50)
