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
prompt = ""
while prompt != "exit":
    prompt = input("\nEscribe 'exit' para salir o cualquier otra cosa para continuar: ")
    if prompt != "exit":
        response = get_llm_response(prompt)
        print(f"Respuesta del modelo: {response}\n\n")

#Detener el rastreador y obtener las emisiones de carbono
emissions = tracker.stop()

#Verificar si emissions es None
if emissions is None:
    emissions = 0.0

#Guardar resultados en un CSV
df = pd.DataFrame({
    "Métrica": ["Precisión del modelo", "Emisiones de carbono (kg CO₂)"],
    "Valor": [round(accuracy, 4), round(emissions, 7)]
})

df.to_csv("resultados.csv", index=False)

#Imprimir resultados
print(f'Precisión del modelo: {accuracy:.4f}')
print(f'Emisiones totales de carbono: {round(emissions, 7)} kg CO₂')
print('Resultados guardados en "resultados.csv"')