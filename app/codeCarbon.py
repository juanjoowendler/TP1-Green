import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from codecarbon import EmissionsTracker

#Iniciar el rastreador de emisiones
tracker = EmissionsTracker()
tracker.start()

#Generar datos de ejemplo
np.random.seed(42)
X = np.random.rand(100, 5)
y = np.random.randint(0, 2, 100)

#Dividir en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Crear y entrenar el modelo KNN
knn = KNeighborsClassifier(n_neighbors=31)
knn.fit(X_train, y_train)

#Hacer predicciones y calcular precisión
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

#Ejecutar una función intensiva en CPU para aumentar emisiones
from llamarIA import get_llm_response
import time
start_time = time.time()

prompt = ""
while prompt != "exit":
    prompt = input("\nEscribe 'exit' para salir o cualquier otra cosa para continuar: ")
    if prompt != "exit":
        response = get_llm_response(prompt)
        print(f"Respuesta del modelo: {response}\n\n")

end_time = time.time()
tiempo_ejecucion = end_time - start_time  # Tiempo en segundos

#Detener el rastreador y obtener las emisiones de carbono
emissions = tracker.stop()

#Verificar si emissions es None
if emissions is None:
    emissions = 0.0

#Imprimir resultados
print('\n\n' + "-" * 50)
print(f'Precisión del modelo: {accuracy:.4f}')
print(f'Emisiones totales de carbono: {round(emissions, 7)} kg CO₂ en {tiempo_ejecucion:.2f} segundos')

factor_emision = 0.26 # kg CO2/kWh
emisiones = emissions * factor_emision

# Calcular las horas de procesamiento necesarias para compensar 30 kg de CO2
co2_absorbido_por_arbol = 30  # kg CO2 por año

# Calcular el consumo por hora basado en el tiempo de ejecución
emisiones_por_segundo = emisiones / tiempo_ejecucion
emisiones_por_hora = emisiones_por_segundo * 3600

# Calcular las horas necesarias para compensar 30 kg de CO2
horas_necesarias = co2_absorbido_por_arbol / emisiones_por_hora

#Guardar resultados en un CSV
df = pd.DataFrame({
    "Métrica": ["Precisión del modelo", "Emisiones de carbono (kg CO₂)", "Emisiones por hora (kg CO₂)", "Horas necesarias para compensar 30 kg de CO₂"],
    "Valor": [round(accuracy, 4), round(emissions, 7), round(emisiones, 7), round(horas_necesarias, 2)]
})

df.to_csv("resultados.csv", index=False)

# Imprimir el resultado
print(f'Emisiones por hora: {emisiones_por_hora:.2f} kg CO₂')
print(f'Horas de procesamiento necesarias para compensar lo que absorbe un árbol en un año: {horas_necesarias:.2f} horas')
print('Resultados guardados en "resultados.csv"')