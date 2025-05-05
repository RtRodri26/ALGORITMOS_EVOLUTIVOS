import pandas as pd

# Crear el DataFrame con los datos proporcionados
data = {
    'Estudiante': ['Rosa', 'David', 'Elena', 'Mario', 'Paula'],
    'Días_prestamo': [7, 10, 5, 12, 3]
}

df = pd.DataFrame(data)

# Calcular el promedio y el máximo de días de préstamo
promedio_dias = df['Días_prestamo'].mean()
maximo_dias = df['Días_prestamo'].max()

# Filtrar quiénes retuvieron el libro más de 8 días
filtro_mas_8_dias = df[df['Días_prestamo'] > 8]

# Mostrar los resultados con líneas de separación
print("="*50)
print("Resumen de los días de préstamo:")
print("="*50)

print(f"Promedio de días de préstamo: {promedio_dias:.2f}")
print(f"Máximo de días de préstamo: {maximo_dias}")
print("-"*50)

print("Estudiantes que retuvieron el libro más de 8 días:")
print("="*50)
print(filtro_mas_8_dias)
print("="*50)
