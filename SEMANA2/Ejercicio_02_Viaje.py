import numpy as np  # Importamos NumPy

# Presupuesto de Carlos
presupuesto = 15.0

# Lista de precios de pasajes por medio de transporte
precios = np.array([2.50, 3.00, 1.80])  # [Bus, Combi, Tren]
medios = ["Bus", "Combi", "Tren"]

# Calculamos la cantidad de viajes posibles con cada medio
viajes = np.floor(presupuesto / precios)

# Mostrar encabezado
print("=" * 60)
print(" ANÁLISIS DE VIAJES SEGÚN MEDIO DE TRANSPORTE ".center(60))
print("=" * 60)

# Mostrar resultados por medio de transporte
print("Cantidad de viajes que Carlos puede realizar con S/ 15.00:")
print("-" * 60)
for i, v in enumerate(viajes):
    print(f"| {medios[i]:<10} | Precio: S/ {precios[i]:<4.2f} | Viajes posibles: {int(v):>3} |")
print("-" * 60)

# Identificar el medio que permite más viajes
mejor_opcion = np.argmax(viajes)

# Mostrar la mejor opción
print("\n>> Mejor opción:")
print("-" * 60)
print(f"Carlos debería usar el {medios[mejor_opcion]} para transportarse,")
print(f"ya que podrá hacer {int(viajes[mejor_opcion])} viajes con S/ 15.00.")
print("=" * 60)
