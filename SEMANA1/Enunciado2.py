#TREJO OBREGON RODRIGO EMILIO   ----  0202114056

# 1. Importamos la biblioteca pandas con el alias pd
import pandas as pd

# 2. Creamos un diccionario con los datos
datos = {
    'Estudiante': ['Ana', 'Luis', 'María', 'Juan', 'Carla'],
    'Horas_usadas': [3, 5, 2, 4, 1]
}

# 3. Creamos un DataFrame a partir del diccionario
df = pd.DataFrame(datos)

# 4. Añadimos la columna 'Costo_total' multiplicando las horas por S/2.00
df['Costo_total'] = df['Horas_usadas'] * 2.00

# 5. Mostramos el DataFrame completo
print("=" * 60)
print("CONTROL DE HORAS DE LABORATORIO - USO SEMANAL")
print("=" * 60)
print(df.head())  # Mostramos las primeras filas (todo el DataFrame en este caso)
print("=" * 60)

# 6. Calculamos estadísticas descriptivas del gasto
print("ESTADÍSTICAS DESCRIPTIVAS DEL GASTO")
print("-" * 60)
print(df['Costo_total'].describe())
print("=" * 60)

# 7. Filtramos estudiantes que gastaron más de S/6.00
gasto_mayor_6 = df[df['Costo_total'] > 6.00]

print("ESTUDIANTES QUE GASTARON MÁS DE S/6.00 EN LA SEMANA")
print("-" * 60)
print(gasto_mayor_6[['Estudiante', 'Costo_total']])
print("=" * 60)

# 8. Mostramos el gasto promedio
gasto_promedio = df['Costo_total'].mean()

# 9. Mostramos el resumen final
estudiantes_mayor_6 = gasto_mayor_6['Estudiante'].tolist()
print("RESUMEN FINAL")
print("-" * 60)
print(f"El gasto promedio fue de S/ {gasto_promedio:.2f}")
print(f"Los estudiantes que gastaron más de S/6.00 son: {estudiantes_mayor_6}")
print("=" * 60)
