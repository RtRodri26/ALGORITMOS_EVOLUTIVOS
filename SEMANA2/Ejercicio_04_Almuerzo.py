import pandas as pd

# Datos de los gastos de Ana en el comedor universitario
gastos = [4.0, 3.5, 5.0, 4.2, 3.8]
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']

# Crear el DataFrame
df = pd.DataFrame(gastos, columns=['Gasto'], index=dias)

# Calcular el gasto total y el gasto medio de la semana
gasto_total = df['Gasto'].sum()
gasto_medio = df['Gasto'].mean()

# Identificar los días en que gastó más que el promedio
dias_mas_que_promedio = df[df['Gasto'] > gasto_medio]

# Mostrar los resultados con una salida mejorada
print("="*50)
print("Resumen de los gastos de Ana en el comedor universitario:")
print("="*50)

print(f"Gasto total de la semana: {gasto_total} unidades monetarias")
print(f"Gasto medio de la semana: {gasto_medio:.2f} unidades monetarias")
print("-"*50)

print("Días en los que gastó más que el promedio:")
print("="*50)
print(dias_mas_que_promedio)
print("="*50)
